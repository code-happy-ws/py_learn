"""抽象工厂模式:定义了一个接口用于创建相关或有依赖关系的对象族，而无需明确指定具体类;
              用来生产不同产品族的全部产品。（支持拓展增加产品族）；
    优点：1.隔离了具体类的生成，使得客户并不需要知道什么被创建，由于这种隔离，更换一个具体工厂就变得相对容易；
         2.增加新的产品族很方便，无须修改已有系统，符合“开闭原则”；
    缺点：
        增加新的产品等级结构麻烦，甚至需要修改抽象层代码，违背了“开闭原则”（使用时要尽量产品等级结构稳定）；
"""
from abc import ABC, abstractmethod


# -------抽象产品--------
class CPU(ABC):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(ABC):
    @abstractmethod
    def show_os(self):
        pass

# -------具体产品--------
class SnapdragonCpu(CPU):
    def show_cpu(self):
        return 'I am snapdragon CPU'


class KirinCpu(CPU):
    def show_cpu(self):
        print('I am Kirin CPU')


class AndroidOS(OS):
    def show_os(self):
        print('I am AndroidOS')


class IOS(OS):
    def show_os(self):
        print('I am IOS')


# -------抽象工厂--------
class PhoneFactory(ABC):
    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


"""具体工厂：具体工厂实现了抽象工厂，每一个具体的工厂方法可以返回一个特定的产品对象，
            而同一个具体工厂所创建的产品对象构成了一个产品族。"""
class SamsungFactory(PhoneFactory):
    def make_cpu(self):
        return SnapdragonCpu()

    def make_os(self):
        return AndroidOS()


class HuaweiFactory(PhoneFactory):
    def make_cpu(self):
        return KirinCpu()

    def make_os(self):
        return AndroidOS()

if __name__ == '__main__':
    # 客户端
    factory = HuaweiFactory()
    cpu = factory.make_cpu()
    os = factory.make_os()
    cpu.show_cpu()
    os.show_os()

