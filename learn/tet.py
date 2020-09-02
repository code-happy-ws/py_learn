import time

def func1():
    while True:
        print('func1')
        yield

def func2():
    g = func1()
    for i in range(10):
        next(g)
        time.sleep(3)
        print('func2')

start = time.time()
func2()
stop = time.time()
print(stop - start)