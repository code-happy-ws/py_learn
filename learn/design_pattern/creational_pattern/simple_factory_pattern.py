"""设计原则中：开闭原则为目标，里氏代换原则为基础，依赖倒置原则为手段"""

""" 简单工厂模式:定义了一个创建对象的类,由这个类来封装实例化对象的行为;
                用来生产同一等级结构中的固定产品(不支持拓展增加产品)
    优点：1.工厂类包含必要的判断逻辑，可以决定在什么时候创建哪一个产品类的实例，客户端可以免除直接创建产品对象的职责，而仅仅“消费”产品，
            简单工厂模式实现了对象创建和使用的分离；
         2.对于一些复杂的类名，通过简单工厂模式可以在一定程度减少使用者的记忆量；
    缺点：1.由于工厂类集中了所有产品的创建逻辑，职责过重，一旦不能正常工作，整个系统都要受到影响。
         2.系统扩展困难，一旦添加新产品就不得不修改工厂逻辑，在产品类型较多时，有可能造成工厂逻辑过于复杂，不利于系统的扩展和维护（不符合开闭原则）。
    适用场景：工厂类负责创建的对象比较少；
"""
from abc import ABC, abstractmethod

"""抽象产品"""


class Payment(ABC):
    """规定了一个兼容接口"""

    @abstractmethod
    def pay(self, money):
        pass


"""具体产品"""


class WeChatPay(Payment):
    """微信支付"""

    def pay(self, money):
        print('微信支付了%s' % money)


"""具体产品"""


class ApplePay(Payment):
    """苹果支付"""

    def pay(self, money):
        print('苹果支付了%s' % money)


"""工厂角色"""


class PayFactory:
    @staticmethod
    def create_pay(method):
        if method == 'apple':
            return ApplePay()
        elif method == 'wechat':
            return ApplePay()

class Pay:
    """对比策略模式：强调对象的行为替换，简单工厂强调对象的生产"""
    def __init__(self, pay_object):
        self.pay_object = pay_object

    def pay(self, money):
        self.pay_object.pay(money)

if __name__ == '__main__':
    pay_factory = PayFactory()
    PAY = pay_factory.create_pay(method='wechat')
    PAY.pay('100')

    Pay(WeChatPay()).pay(10)
