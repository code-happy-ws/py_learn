"""
    单例模式：确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，它提供全局访问的方法。
"""
from threading import Lock


class Singleton:
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):  # 加锁前初步判断是否实例化过，避免不必要的加锁开销
            with cls._lock:
                if not hasattr(Singleton, '_instance'):  # 二次判断，避免多个线程均通过第一次判断时，轮流加锁均实例化；
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, m):
        self.m = m

    def show(self):
        print(self.m)


obj1 = Singleton('a')

obj2 = Singleton('b')
print(id(obj1), id(obj2))
obj1.show()
obj2.show()
