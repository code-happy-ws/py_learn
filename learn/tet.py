

# from multiprocessing import Process, current_process
# import logging
# import os
# import time
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)-15s - %(levelname)s - %(message)s'
# )
#
#
# def run():
#     logging.info('exit child process %s', current_process().pid)
#     os._exit(3)
#
#
# p = Process(target=run)
# p.start()
# time.sleep(100)

import errno
from multiprocessing import Process, current_process
import logging
import os
import signal
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s - %(levelname)s - %(message)s'
)


def run():
    exitcode = 3
    logging.info('exit child process %s with exitcode %s',
                 current_process().pid, exitcode)
    os._exit(exitcode)


def wait_child(signum, frame):
    logging.info('receive SIGCHLD')
    try:
        while True:
            # -1 表示任意子进程
            # os.WNOHANG 表示如果没有可用的需要 wait 退出状态的子进程，立即返回不阻塞
            cpid, status = os.waitpid(-1, os.WNOHANG)
            if cpid == 0:
                logging.info('no child process was immediately available')
                break
            exitcode = status >> 8
            logging.info('child process %s exit with exitcode %s', cpid, exitcode)
    except OSError as e:
        if e.errno == errno.ECHILD:
            logging.error('current process has no existing unwaited-for child processes.')
        else:
            raise
    logging.info('handle SIGCHLD end')


signal.signal(signal.SIGCHLD, wait_child)

p = Process(target=run)
p.start()

while True:
    time.sleep(100)