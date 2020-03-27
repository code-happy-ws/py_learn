# -*- coding: utf-8 -*-
import multiprocessing as mp
import os
import random
from signal import signal, SIGINT, SIG_IGN, siginterrupt
import time

def data_source():
    """数据源。

    随机选择一个浮点数，作为worker进程的sleep时间，
    具体实践时可以将这部分实现改为读取数据库。
    """
    dataset = [0.1, 0.2, 0.3, 0.4, 0.5]
    while True:
        time.sleep(0.2)
        yield random.choice(dataset)

def proc_proxy(cntl_q, data_q, exit_flag):
    """从数据源读取数据。

    先通过cntl_q通知主进程，
    再将数据通过data_q发给worker。
    """
    for item in data_source():
        cntl_q.put({'event': 'data'})
        data_q.put(item)
        if exit_flag.is_set():
            cntl_q.put({'event': 'exit', 'pid': os.getpid()})
            break


def proc_worker(cntl_q, data_q):
    """处理数据。

    从data_q获取数据，处理完毕后通过cntl_q通知主进程，
    然后退出。
    """
    item = data_q.get()
    time.sleep(item)
    cntl_q.put({'event': 'exit', 'pid': os.getpid()})

def main():
    proc_pool = {} # 记录创建的所有子进程
    cntl_q = mp.Queue() # 控制信息传递队列
    data_q = mp.Queue() # 具体数据传递队列
    exit_flag = mp.Event() # 退出标记，初始值为False

    # 收到SIGINT，通知proxy停止读取数据
    signal(SIGINT, lambda x, y: exit_flag.set())
    siginterrupt(SIGINT, False)

    # 启动proxy进程，后续按需启动woker进程
    print('main {} started'.format(os.getpid()))
    proc = mp.Process(target=proc_proxy, args=(cntl_q, data_q, exit_flag))
    proc.start()
    proc_pool[proc.pid] = proc
    print('proxy {} started'.format(proc.pid))

    while True:
        item = cntl_q.get()
        if item['event'] == 'data':
            proc = mp.Process(target=proc_worker, args=(cntl_q, data_q))
            proc.start()
            proc_pool[proc.pid] = proc
            print('worker {} started'.format(proc.pid))
        elif item['event'] == 'exit':
            proc = proc_pool.pop(item['pid'])
            proc.join()
            print('child {} stopped'.format(item['pid']))
        else:
            print('It\'s impossible !')

        if not proc_pool: # 所有子进程均已退出
            break

    print('main {} stopped'.format(os.getpid()))

if __name__ == '__main__':
    main()