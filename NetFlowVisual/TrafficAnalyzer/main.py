import queue

import config
import db
import util
from protocol import dns, tcp, udp, app
from scapy.all import *

# 创建pkt队列，用于存储网络数据包
pkt_queue = queue.Queue()

# func: 处理队列中的数据包，根据数据包的协议类型调用相应的处理函数
def deal_pkt():
    cnt = 0
    while True:
        try:
            pkt, timestamp = pkt_queue.get()
            if not dns.read(pkt, timestamp):
                udp.read(pkt, timestamp)
                tcp.read(pkt, timestamp)
        except Exception as e:
            print("[deal_pkt] ", e)

# 使用sniff捕获网络数据包，并将捕获到的数据及其时间戳放入pkt队列中
def _sniff():
    while True:
        sniff(iface=config.interface, prn=lambda pkt: pkt_queue.put((pkt, int(time.time()))), count=100)

# 创建并启动两个线程：一个线程用于处理队列中的数据包，另一个线程用于捕获数据包
if __name__ == '__main__':
    util.add_thread(deal_pkt)
    util.add_thread(_sniff)
    util.start_all_thread()

# 在主循环中，每隔10秒打印队列大小以及TCP、UDP和应用层会话的数量
try:
    while True:
        time.sleep(10)
        print("queue size: {} , TCP sess: {}, UDP sess: {}, APP sess: {}"
              .format(pkt_queue.qsize(), len(tcp.sessions), len(udp.sessions), len(app.sessions)))

# 如果捕获到KeyboardInterrupt异常，则关闭数据库连接，打印结束信息，并退出程序
except KeyboardInterrupt:
    db.close()
    print("Bye")
    exit()
