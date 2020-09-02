"""协程遇到IO操作自动切换到其它协程（如何实现检测IO，yield、greenlet都无法实现，就用到了gevent模块（select机制））"""
from gevent import spawn, joinall, monkey

monkey.patch_all()

import time


def task(pid):
    """
    Some non-deterministic task
    """
    time.sleep(1)
    print('Task %s done' % pid)


def synchronous():
    for i in range(10):
        task(i)


def asynchronous():
    g_l = [spawn(task, i) for i in range(10)]  # 创建批量协程对象
    joinall(g_l)  # 等待g_l中所有协程对象结束


if __name__ == '__main__':
    print('Synchronous:')
    s1 = time.time()
    synchronous()
    s2 = time.time()
    print('Asynchronous:')
    asynchronous()
    s3 = time.time()
    print('Synchronous_time:', s2 - s1)
    print('Asynchronous:_time:', s3 - s2)
