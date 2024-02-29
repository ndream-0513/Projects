import functools

import db
from scapy.layers.dns import DNSRR, DNSQR, DNS
from scapy.layers.l2 import Ether

'''
存储dns请求报文、dns响应报文的sql语句
'''
dns_query_sql = "INSERT INTO `log_dns` (`client_mac`, `domain`, `time`) VALUE (" \
                "'{client_mac}', '{domain}', {time})"
dns_response_sql = "INSERT INTO `log_dns` (`type`, `client_mac`, `domain`, `rdata`, `time`) VALUE (" \
                   "{type}, '{client_mac}', '{domain}', '{rdata}', {time})"

g_rdata = ""
g_qdata = ""
g_dns_reverse_db_conn = db.get_db_instance()
g_dns_reverse_db_cur = g_dns_reverse_db_conn.cursor()


@functools.lru_cache(10000)
def _dns_reverse(rdata):
    if rdata == g_rdata:
        return g_qdata
    sql = "SELECT `domain` FROM `log_dns` WHERE `rdata`='{}' ORDER BY `id` DESC LIMIT 1"
    if g_dns_reverse_db_cur.execute(sql.format(rdata)):
        return g_dns_reverse_db_cur.fetchall()[0][0]
    return None


def reg_dns_rev_cache(rdata, qdata):
    global g_rdata, g_qdata
    g_rdata = rdata
    g_qdata = qdata
    _dns_reverse(rdata)


def dns_reverse(rdata):
    max_depth = 10
    while True:
        if max_depth == 0:
            return rdata
        _rdata = _dns_reverse(rdata)
        if _rdata is None:
            return rdata
        rdata = _rdata
        max_depth -= 1

'''
isinstance(s, str)，python的内置函数，用于检查变量s是否为字符串类型
'''
def byte2str(s):
    return s if isinstance(s, str) else s.decode()

'''
在DNS协议中，域名以.结尾表示域名的结束，在使用 Scapy 进行 DNS 数据包解析时，
p[DNSQR].qname 返回的是 DNS 查询记录的域名字段。如果域名字段以点号结尾，
则 Scapy 会保留该点号作为域名的一部分。可使用下面的切片操作去除下面的点
'''
def clean_dns(s):
    if s[-1] == '.':
        return s[:-1]
    return s

'''
对dns请求报文进行处理：
首先对报文的qname进行处理得到处理后的域名(先转化为字符串，然后再去掉域名后多余的点
'''
def deal_dns_query(pkt, timestamp):
    qname = clean_dns(byte2str(pkt[DNSQR].qname))
    reg_dns_rev_cache(qname, None)
    res = {
        "client_mac": pkt[Ether].src,
        "domain": qname,
        "time": timestamp
    }
    sql = dns_query_sql.format(**res)
    db.query(sql)
    return True

'''
ancount: answer count回答资源记录的数量，每个回答资源记录对应着一个查询的域名所对应的IP地址或其他信息
an[i]: dns的回答部分的第i个回答资源记录的内容
'''
def deal_dns_response(pkt, timestamp):
    for i in range(pkt[DNS].ancount):
        dnsrr = pkt[DNS].an[i]
        rdata = clean_dns(byte2str(dnsrr.rdata))
        rrname = clean_dns(byte2str(dnsrr.rrname))
        reg_dns_rev_cache(rdata, rrname)
        res = {
            "type": pkt[DNS].an[i].type,
            "client_mac": pkt[Ether].dst,
            "domain": rrname,
            "rdata": rdata,
            "time": timestamp
        }
        sql = dns_response_sql.format(**res)
        db.query(sql)
    return True

'''
main.py中的deal_pkt调用dns的read函数来对dns报文进行处理：
首先判断数据包中是否有dns层(haslyer是scapy中的一个函数，haslayer(DNS)用来判断数据包中是否存在DNS层)
没有则返回false，有则继续执行，判断该dns报文是dns请求报文还是dns响应报文
DNSQR是scapy中表示DNS查询记录的类
DNSRR是scapy中表示DNS响应记录的类
'''
def read(pkt, timestamp):
    try:
        if not pkt.haslayer(DNS):
            return False
        if DNSQR in pkt and pkt.dport == 53:
            return deal_dns_query(pkt, timestamp)
        elif DNSRR in pkt and pkt.sport == 53:
            return deal_dns_response(pkt, timestamp)
        return False
    except Exception as e:
        print("[DNS] ", e)
        return False
