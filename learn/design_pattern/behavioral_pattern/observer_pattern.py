""" 观察者模式(Observer Pattern)：定义对象之间的一种一对多依赖关系，使得每当一个对象状态发生改变时，
        其相关依赖对象皆得到通知并被自动更新。
    观察者模式的别名包括发布-订阅（Publish/Subscribe）模式、模型-视图（Model/View）模式、
        源-监听器（Source/Listener）模式或从属者（Dependents）模式。
    观察者模式是一种对象行为型模式。
"""
from abc import ABC, abstractmethod

"""抽象目标:指被观察的对象。在目标中定义了一个观察者集合，一个观察目标可以接受任意数量的观察者来观察，
            它提供一系列方法来增加和删除观察者对象"""


class AbstractAllyControl(ABC):
    def __init__(self, ally_name):
        self.ally_members = []
        self.ally_name = ally_name

    def join(self, member):
        self.ally_members.append(member)
        print(f'{member.name}加入{self.ally_name}战队')

    @abstractmethod
    def notify_observer(self, member_name):
        pass


"""抽象观察者:观察者将对观察目标的改变做出反应"""


class AbstractObserver(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def be_attacked(self, ally):
        pass


"""具体目标:具体目标是目标类的子类，通常它包含有经常发生改变的数据，
           当它的状态发生改变时，向它的各个观察者发出通知,
           同时它还实现了在目标类中定义的抽象业务逻辑方法;
"""


class AllyControl(AbstractAllyControl):
    def notify_observer(self, member_name):
        print(f'{self.ally_name}紧急通知，{member_name}正遭受bug攻击！')
        for m in self.ally_members:
            if m.name != member_name:
                print(f'坚持住，{m.name}马上来救你！')


"""具体观察者:在具体观察者中维护一个指向具体目标对象的引用"""


class Observer(AbstractObserver):
    def __init__(self, name):
        super().__init__(name)

    def be_attacked(self, ally):
        ally.notify_observer(self.name)


if __name__ == '__main__':
    ally = AllyControl("自动化工程")
    member1, member2, member3 = Observer('伍威'), Observer('梁树明'), Observer('吴文松')
    ally.join(member1)
    ally.join(member2)
    ally.join(member3)
    member1.be_attacked(ally)
