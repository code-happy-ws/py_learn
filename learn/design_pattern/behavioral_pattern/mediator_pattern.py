""" 中介者模式(Mediator Pattern)：用一个中介对象（中介者）来封装一系列的对象交互，
        中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互，
        将一个网状的系统结构变成一个以中介者对象为中心的星形结构；
    优点：简化了对象之间的交互；可将各同事对象解耦；
    缺点：可能会导致具体中介者类非常复杂，使得系统难以维护；
    适用场景：
        1.系统中对象之间存在复杂的引用关系；
        2.一个对象由于引用了其他很多对象并且直接和这些对象通信，导致难以复用该对象；
        3.通过一个中间类来封装多个类中的行为，而又不想生成太多的子类；
"""
from abc import ABC, abstractmethod

"""抽象中介者:它定义一个接口，该接口用于与各同事对象之间进行通信"""


class AbstractMediator(ABC):

    @abstractmethod
    def interactive(self, component):
        pass


"""具体中介者:它是抽象中介者的子类，通过协调各个同事对象来实现协作行为，它维持了对各个同事对象的引用"""


class ConcreteMediator(AbstractMediator):
    def __init__(self):
        self.button = None
        self.combo_box = None
        self.list_box = None
        self.text_box = None

    def interactive(self, component):
        if component == self.button:
            print('点击增加按钮')
            self.combo_box.update()
            self.list_box.update()
            self.text_box.update()
        elif component == self.list_box:
            print('从列表框中选择一项')
            self.combo_box.select()
            self.text_box.select()
        elif component == self.combo_box:
            print('从组合框选中一项')
            self.combo_box.select()
            self.text_box.select()


"""抽象同事类：它定义各个同事类公有的方法，并声明了一些抽象方法来供子类实现，同
    时它维持了一个对抽象中介者类的引用，其子类可以通过该引用来与中介者通信"""


class AbstractComponent(ABC):
    def set_mediator(self, mediator):
        self.mediator = mediator

    def changed(self):
        self.mediator.interactive(self)

    def update(self):
        pass


"""具体同事类：它是抽象同事类的子类；每一个同事对象在需要和其他同事对象通信时，
    先与中介者通信，通过中介者来间接完成与其他同事类的通信"""


class AddButton(AbstractComponent):
    pass


class ListBox(AbstractComponent):
    def update(self):
        print("列表框增加一项")

    def select(self):
        print("列表框选中一项")


class ComboBox(AbstractComponent):
    def update(self):
        print("组合框增加一项")

    def select(self):
        print("组合框选中一项")


class TextBox(AbstractComponent):
    def update(self):
        print("客户信息增加后清空文本框")

    def select(self):
        print("文本框显示")


"""客户端"""
if __name__ == '__main__':
    # 中介者对象
    mediator = ConcreteMediator()

    # 同事对象
    button = AddButton()
    combo_box = ComboBox()
    list_box = ListBox()
    text_box = TextBox()

    # 为同事对象引入中介者
    button.set_mediator(mediator)
    combo_box.set_mediator(mediator)
    list_box.set_mediator(mediator)
    text_box.set_mediator(mediator)
    mediator.button = button
    mediator.combo_box = combo_box
    mediator.list_box = list_box
    mediator.text_box = text_box

    # 行为交互
    button.changed()
    print('---------------------------')
    list_box.changed()
