""" 工厂方法模式:定义了一个创建对象的抽象方法，由子类决定要实例化的类；工厂方法模式将对象的实例化推迟到关联子类;
                用来生产同一等级结构中的任意产品(支持拓展增加产品)；
    优点：1.工厂方法用来创建客户所需要的产品，同时还向客户隐藏了哪种具体产品类将被实例化这一细节，
            用户只需要关心所需产品对应的工厂，无须关心创建细节；
         2.在系统中加入新产品时，无须修改抽象工厂和抽象产品提供的接口，无须修改客户端，
            也无须修改其他的具体工厂和具体产品，而只要添加一个具体工厂和具体产品就可以；
    缺点：在添加新产品时，需要编写新的具体产品类，而且还要提供与之对应的具体工厂类，
         系统中类的个数将成对增加，在一定程度上增加了系统的复杂度
"""
from abc import ABC, abstractmethod

"""抽象产品"""


class Payment(ABC):
    """规定了一个兼容接口"""

    @abstractmethod
    def pay(self):
        pass


"""具体产品"""


class WeChatPay(object):
    """微信支付"""

    def pay(self, money):
        print('微信支付了%s' % money)


"""具体产品"""


class ApplePay(object):
    """苹果支付"""

    def pay(self, money):
        print('苹果支付了%s' % money)


"""抽象工厂"""


class PayFactory(ABC):
    @abstractmethod
    def create_pay(self, method):
        pass


"""具体工厂"""


class WeChatPayFactory(PayFactory):
    def create_pay(self):
        return ApplePay()


"""具体工厂"""


class ApplePayFactory(PayFactory):
    def create_pay(self):
        return WeChatPay()


if __name__ == '__main__':
    pay_factory = WeChatPayFactory()
    PAY = pay_factory.create_pay()
    PAY.pay('100')
