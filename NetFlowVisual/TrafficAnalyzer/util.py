import time
from threading import Thread

threads = []        # 一个存储线程函数的列表
threads_status = [] # 一个存储线程对象的列表，用于维护线程的状态
crontab = []        # 一个存储定时任务的列表，每个定时任务包含要执行的函数、时间间隔和计数器

'''
向threads列表中添加线程函数
'''
def add_thread(func):
    global threads
    threads.append(func)

'''
启动threads列表中的所有线程函数
创建线程对象并启动线程
'''
def start_all_thread():
    for thread_func in threads:
        print("[util.thread] start ", thread_func)
        threads_status.append(Thread(target=thread_func))

    for thread in threads_status:
        thread.start()

'''
用于向crontab列表中添加定时任务
指定要执行的函数和时间间隔
'''
def add_cron(func, intval):
    print("[util.crond] add {} intval {}".format(func, intval))
    crontab.append({
        "func": func,
        "intval": intval,
        "_": 0
    })


def crond():
    while True:
        time.sleep(1)
        # try:
        for cron in crontab:
            cron["_"] += 1
            if cron["_"] >= cron["intval"]:
                cron["_"] = 0
                try:
                    cron['func']()
                except:
                    continue
        # except Exception as e:
        #     print("[crond] ", e)


add_thread(crond)
