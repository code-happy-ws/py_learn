"""简单工厂模式:定义了一个创建对象的类,由这个类来封装实例化对象的行为;
    用来生产同一等级结构中的固定产品(不支持拓展增加产品)"""
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


class PayFactory:
    @staticmethod
    def create_pay(method):
        if method == 'apple':
            return ApplePay()
        elif method == 'wechat':
            return ApplePay()


if __name__ == '__main__':
    pay_factory = PayFactory()
    PAY = pay_factory.create_pay(method='wechat')
    PAY.pay('100')
