"""状态模式：允许一个对象在其内部状态改变时改变它的行为,用于解决系统中复杂对象的状态转换以及不同状态下行为的封装问题"""
from abc import ABC,abstractmethod

"""环境类"""
class Account:
    """银行账户"""
    def __init__(self, owner):
        self.owner = owner
        # 余额初始化为0
        self.balance = 0
        self.state = AbstractState()

    def get_balance(self):
        return self.balance

    def desposit(self, amount):
        """存款"""
        print(f'{self.owner}存款{amount}元')
        print('现在余额为：', self.balance)
        print('现在状态为：', self.state)

"""抽象状态类"""
class AbstractState(ABC):
    def __init__(self):
        self.account = Account()

    def desposit(self,amount):
        """存款"""
        pass

    def withdraw(self,amount):
        """取款"""
        pass

    def compute_interest(self):
        """计算利息"""
        pass

    def state_check(self):
        """状态检查"""
        pass
"""具体状态类"""