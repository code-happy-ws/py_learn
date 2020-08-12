"""状态模式：允许一个对象在其内部状态改变时改变它的行为,用于解决系统中复杂对象的状态转换以及不同状态下行为的封装问题;

   优点:
        封装了状态的转换规则，在状态模式中可以将状态的转换代码封装在环境类或者具体状态类中，
        可以对状态转换代码进行集中管理，而不是分散在一个个业务方法中；
    缺点：
        1.状态模式的使用必然会增加系统中类和对象的个数，导致系统运行开销增大；
        2.状态模式的结构与实现都较为复杂，如果使用不当将导致程序结构和代码的混乱，增加系统设计的难度；
        3.状态模式对“开闭原则”的支持并不太好，增加新的状态类需要修改那些负责状态转换的源代码；

"""
from abc import ABC, abstractmethod


"""环境类"""


class Account:
    """银行账户"""
    def __init__(self, owner):
        self.owner = owner
        # 余额初始化为0
        self.balance = 0
        self.state = NormalState(self)
        print(f'{self.owner}开户成功！')
        print('---' * 20)

    def set_state(self, state):
        self.state = state

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def desposit(self, amount):
        """存款"""
        print('存款请求中...')
        self.state.desposit(amount)
        print('现在余额为：', self.balance)
        print(f'当前状态为{self.state.__class__.__name__}')
        print('---'*20)

    def withdraw(self, amount):
        """取款"""
        print('取款请求中...')
        self.state.withdraw(amount)
        print('现在余额为：', self.balance)
        print(f'当前状态为{self.state.__class__.__name__}')
        print('---'*20)


"""抽象状态类"""

class AbstractState(ABC):
    def __init__(self, account):
        self.account = account

    @abstractmethod
    def desposit(self, amount):
        """存款"""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """取款"""
        pass

    @abstractmethod
    def state_check(self):
        """状态检查"""
        pass


"""具体状态类"""

class NormalState(AbstractState):
    """正常状态"""
    def desposit(self, amount):
        self.account.set_balance(self.account.balance + amount)
        print(f"{self.account.owner}在正常状态存款{amount}元")
        self.state_check()

    def withdraw(self, amount):
        self.account.set_balance(self.account.balance - amount)
        print(f"{self.account.owner}在正常状态取款{amount}元")
        self.state_check()

    def state_check(self):
        if -2000 < self.account.balance < 0:
            self.account.set_state(OverdraftState(self.account))
        elif self.account.balance <= -2000:
            self.account.set_state(RestrictedState(self.account))


class OverdraftState(AbstractState):
    """透支状态"""
    def desposit(self, amount):
        self.account.set_balance(self.account.balance + amount)
        print(f"{self.account.owner}在透支状态存款{amount}元")
        self.state_check()

    def withdraw(self, amount):
        self.account.set_balance(self.account.balance - amount)
        print(f"{self.account.owner}在透支状态取款{amount}元")
        self.state_check()

    def state_check(self):
        if self.account.balance >= 0:
            self.account.set_state(NormalState(self.account))
        elif self.account.balance <= -2000:
            self.account.set_state(RestrictedState(self.account))


class RestrictedState(AbstractState):
    """受限状态"""
    def desposit(self, amount):
        self.account.set_balance(self.account.balance + amount)
        print(f"{self.account.owner}在受限状态存款{amount}元")
        self.state_check()

    def withdraw(self, amount):
        print(f"{self.account.owner}在受限状态无法取款！")

    def state_check(self):
        if self.account.balance >= 0:
            self.account.set_state(NormalState(self.account))
        elif -2000 < self.account.balance < 0:
            self.account.set_state(OverdraftState(self.account))

if __name__ == '__main__':
    person = Account('振威')
    person.desposit(5000)
    person.withdraw(6000)
    person.withdraw(2000)
    person.withdraw(1000)
    person.desposit(5000)
