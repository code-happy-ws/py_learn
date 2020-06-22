"""工厂方法模式"""
from abc import ABC, abstractmethod


class Payment(ABC):
    """规定了一个兼容接口"""

    @abstractmethod
    def pay(self):
        pass


class WeChatPay(object):
    """微信支付"""

    def pay(self, money):
        print('微信支付了%s' % money)


class ApplePay(object):
    """苹果支付"""

    def pay(self, money):
        print('苹果支付了%s' % money)


class PayFactory(ABC):
    @abstractmethod
    def create_pay(self, method):
        pass


class WeChatPayFactory(PayFactory):
    def create_pay(self):
        return ApplePay()


class ApplePayFactory(PayFactory):
    def create_pay(self):
        return WeChatPay()


if __name__ == '__main__':
    pay_factory = WeChatPayFactory()
    PAY = pay_factory.create_pay()
    PAY.pay('100')
