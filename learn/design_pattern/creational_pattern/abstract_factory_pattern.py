"""抽象工厂模式:定义了一个接口用于创建相关或有依赖关系的对象族，而无需明确指定具体类;
    用来生产不同产品族的全部产品。（支持拓展增加产品；支持增加产品族） """
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


# -------抽象工厂--------
class PhoneFactory(ABC):
    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# -------具体产品--------
class SnapdragonCpu(CPU):
    def show_cpu(self):
        return 'I am snapdragon CPU'


class KirinCpu(CPU):
    def show_cpu(self):
        return 'I am Kirin CPU'


class AndroidOS(OS):
    def show_os(self):
        return 'I am AndroidOS'


class IOS(OS):
    def show_os(self):
        return 'I am IOS'


# -------具体工厂--------
class VivoFactory(PhoneFactory):
    def make_cpu(self):
        return SnapdragonCpu()

    def make_os(self):
        return AndroidOS()


class HuaweiFactory(PhoneFactory):
    def make_cpu(self):
        return KirinCpu()

    def make_os(self):
        return AndroidOS()


# -------客户端--------
class Phone:
    def __init__(self, factory):
        self.factory = factory
        self.cpu = None
        self.os = None

    def make_phone(self):
        self.cpu = self.factory.make_cpu()
        self.os = self.factory.make_os()

    def show_info(self):
        print("cpu信息：", self.cpu.show_cpu())
        print("os信息：", self.os.show_os())


if __name__ == '__main__':
    PHONE = Phone(HuaweiFactory())
    PHONE.make_phone()
    PHONE.show_info()
