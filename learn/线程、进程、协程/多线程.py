import threading,time

lock=threading.Lock()

# current_thread()返回一个当前工作实例
a=0
sem=threading.Semaphore(3) # 信号量

def run(num):
    print('子线程%s开始'%(threading.current_thread().name))
    global a

    for i in range(1000000):
        lock.acquire() # 加锁 ， 确保以下代码只有一个线程从头到尾执行 ，但是阻止并发，运行效率下降
        a+=5
        a-=5
        lock.release() # 解锁
        # 另一种写法
        # with lock:
        #     a += 5
        #     a -= 5
    print(a)
    time.sleep(2)
    print('子进程%s结束' % (threading.current_thread().name))

def run1():
    with sem: # 信号量为3，只运行同时运行3个多线程
        for i in range(5):
            print('%s---%d' % (threading.current_thread().name,i))
            time.sleep(1)

if __name__ == '__main__':
    print('主线程%s开始'%(threading.current_thread().name))

    # 多个线程共享空间，容易冲突，可通过互斥锁解决
    t=threading.Thread(target=run,args=(1,),name='runThread')
    t1 = threading.Thread(target=run, args=(1,), name='runThread1')
    t.start()
    t1.start()
    t.join()
    t1.join()

    for i in range(5):
        t=threading.Thread(target=run1)
        t.start()
        # t.join()  # join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程再终止

    print('主线程结束')