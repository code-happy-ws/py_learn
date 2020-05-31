from multiprocessing import Event

e = Event()  # 创建事件对象,这个对象的初识状态为False
print('e的状态是:', e.is_set())  # False

print('进程运行到这里了')
e.set()  # 将e的状态改为True
print('e的状态是:', e.is_set())  # True

e.clear()  # 将e的状态改为False

e.wait()  # 当事件对象e的状态为false的时候,在wait的地方会阻塞程序,当对象状态为true的时候,直接在这个wait地方继续往下执行

print('进程过了wait')
