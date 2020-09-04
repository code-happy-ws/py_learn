"""策略模式(Strategy Pattern)：定义一系列算法类，将每一个算法封装起来，并让它们可以相互替换"""

from abc import ABC, abstractmethod

"""抽象策略"""


class Payment(ABC):
    """规定了一个兼容接口"""

    @abstractmethod
    def pay(self, money):
        pass


"""具体策略"""


class WeChatPay(Payment):
    """微信支付"""

    def pay(self, money):
        print('微信支付了%s' % money)


"""具体策略"""


class ApplePay(Payment):
    """苹果支付"""

    def pay(self, money):
        print('苹果支付了%s' % money)


class Pay:
    """环境类，对比简单工厂模式：策略模式强调对象的行为替换，简单工厂强调对象的生产"""
    def __init__(self, pay_object):
        self.pay_object = pay_object

    def pay(self, money):
        self.pay_object.pay(money)

if __name__ == '__main__':

    Pay(WeChatPay()).pay(10)
