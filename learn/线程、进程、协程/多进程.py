import multiprocessing
import os

num=11

def run_2():
    print("*" * 20)
    print(__name__)
    print("孙子进程启动")
    global num
    num+=1
    print(num)
    print('孙子进程结束')

def run_proc(name):
    print("-"*20)
    print(__name__)
    print('Child process {0} {1} Running, 父进程为{2} '.format(name, os.getpid(),os.getppid()))
    print(name*10)
    global num
    num+=1
    p = multiprocessing.Process(target=run_2)
    p.start()
    p.join()


#不可省略，防止子进程调用；
if __name__ == '__main__':
    print('Parent process {0} is Running'.format(os.getpid()))
    # 所有进程（包括父进程）对全局变量的修改不会影响其他进程
    a=100
    for i in range(5):
        print(num)
        p = multiprocessing.Process(target=run_proc, args=(str(i)),)
        print('process start')
        p.start()
    print(num)
    # 子进程结束后父进程才结束
    p.join()
    print('Process close')
