from inspect import getgeneratorstate
import asyncio
# # GEN_CREATED 等待开始执行; 'GEN_RUNNING' 解释器正在执行,多线程才能看到这个状态；
# # 'GEN_SUSPENDED'，在 yield 表达式处暂停， 'GEN_CLOSED'，　执行结束。
#
# yield ---------------------------------------------
def coroutine(a):
    print('a=',a)
    b=yield a
    print('b=',b)
    c=yield a+b
    print('c=',c)
co=coroutine(10)
print(getgeneratorstate(co))  # GEN_CREATED

#  协程预激，使协程运行到第一个yield处，=右侧yield已运行，向左侧赋值未完成，待send（）参数非None赋值；即在赋值语句中，=右边的代码在赋值之前执行
print('NEXT',next(co))
# next(co)   # 等同于co.send(None)
# print('11111')
print(co.send(5))  # 10
print(co.send(6))  # 10
# # print(getgeneratorstate(co))  # GEN_SUSPENDED
#
# # # send 方法的参数会成为暂停的 yield 表达式的值，赋值给左侧变量
# co.send(20) # b=20
# # co.send(100)
# # next(co)

# yield from----------------------------------
@asyncio.coroutine
def task(b):
    print('1')
    yield from asyncio.sleep(5)
    yield from b

    # yield from c
    # print('2')


# if __name__ == '__main__':
    # m=task('abc')
    # n=task('ABC')
    # to_do=[m,n]
    # to_do_iter = asyncio.as_completed(to_do)
    # loop=asyncio.get_event_loop()
    # loop.create_task(task('456'))
    # n=loop.run_until_complete(asyncio.wait(to_do))
    # print(m.__next__())
    # print(m.__next__())
    # print(m.__next__())
    # print(m.__next__())
    # print(list(a('abc','123')))