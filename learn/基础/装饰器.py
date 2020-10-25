from functools import singledispatch, wraps
from collections import abc
import numbers

print('基础装饰器---------------------------------------------------------')


def clear(func, name='zzw'):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(name)
        print('start')
        func(*args, **kwargs)
        print('end')
    return wrapper


@clear  # a=clear(a)
def a(m):  # 参数将传递至wrapper中
    print('aa' + m)


# a('bb')

print('装饰器类---------------------------------------------------------')


class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass


@logit()
def myfunc1():
    pass


print('派发装饰器--函数使用---------------------------------------------------------')


@singledispatch
def show_type(object):
    print('type:', type(object))


@show_type.register(str)
def _(text):
    print('i am text')


@show_type.register(tuple)
def _(n):
    print('i am tuple')


@show_type.register(numbers.Integral)
def _(n):
    print('i am Integral')


"""只要可能，注册的专门函数应该处理抽象基类（如 numbers.Integral 和
abc.MutableSequence），不要处理具体实现（如 int 和 list）。这样，代码支持的
兼容类型更广泛。"""


@show_type.register(abc.MutableSequence)
def _(n):
    print('i am MutableSequence')


show_type('a')
show_type(1)
show_type((1,))
show_type([1, 2])

print('派发装饰器--类使用---------------------------------------------------------')

class A:
    pass

class B:
    pass

class C:
    @singledispatch
    def visit(t):
        """其他未知类型处理"""
        print('财务部处理员工类型异常')

    @visit.register
    def _(t: int):
        """等同于
            @visit.register(int)
            def _(t):
                print(f'财务部处理全职员工')
        """
        print(f'财务部处理全职员工')

    @visit.register
    def _(t: str):
        print(f'财务部处理兼职员工')

# 不能实例化调用，只能通过类调用，singledispatch源码分析只能取第一个参数类型进行派分
C.visit(1)
