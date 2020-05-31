class A:
    def __init__(self):
        pass

    def __repr__(self):
        # 用于交互模式下提示回应以及repr函数，如果没有实现__str__，print才会执行
        # 实际上__str__只是覆盖了__repr__以得到更友好的用户显示
        # 推荐实现这个
        return '__repr__ is called'

    def __str__(self):
        # 打印操作会首先尝试__str__和str内置函数,然后才会尝试__repr__
        return '__str__ is called'


a=A()
print(a)