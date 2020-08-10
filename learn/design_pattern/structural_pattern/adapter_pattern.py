"""适配器模式(Adapter Pattern)：将一个接口转换成客户希望的另一个接口，
使接口不兼容的那些类可以一起工作，其别名为包装器(Wrapper)。
适配器模式既可以作为类结构型模式(适配器和适配者为继承关系)，也可以作为对象结构型模式（适配器和适配者为关联关系  推荐）。

作用：可实现在不修改适配者代码前提下使用适配者提供接口功能；

注：
Adapter模式用于填补不同接口（API）之间的缝隙，
而Decorator模式则是在不改变接口（API）的前提下增加功能；

Adapter模式用于连接接口（API）不同的类，
而Bridge模式则用于连接类的功能层次结构与实现层次结构。

使用场景： 系统需要使用一些现有的类，而这些类的接口（如方法名）不符合系统的需要，甚至没有这些类的源代码。
"""


class Target:
    """目标抽象类：定义客户所需接口"""

    def __init__(self):
        pass

    def request(self):
        pass


class Adaptee:
    """适配者:被适配的角色，它定义了一个已经存在的接口，这个接口需要适配"""

    def __init__(self):
        pass

    def specific_request(self):
        pass


class ObjectAdapter(Target):
    """对象适配器：适配器可以调用另一个接口，作为一个转换器，
    对Adaptee和Target进行适配，适配器类是适配器模式的核心，
    在对象适配器中，它通过继承Target并关联一个Adaptee对象使二者产生联系。"""

    def __init__(self):
        self.adaptee = Adaptee()
        super().__init__()

    def request(self):
        print('我是对象适配器')
        return self.adaptee.specific_request()


class ClassAdapter(Target, Adaptee):
    """类适配器：
    在类适配器中，它通过继承Target和Adaptee对象使二者产生联系。"""

    def request(self):
        print('我是类适配器')
        return self.specific_request()


if __name__ == '__main__':
    target = ObjectAdapter()
    target.request()
