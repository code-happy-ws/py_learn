"""
引子：室内设计时，一个开关可以控制各种电器，只需修改电线；
命令模式:将一个请求封装为一个对象，从而让我们可用不同的请求对客户进行参数化；
        可支持请求排队或者记录请求日志，以及可撤销的操作。
        命令模式是一种对象行为型模式，其别名为动作(Action)模式或事务(Transaction)模式。
        命令模式可以将请求发送者和接收者完全解耦，发送者与接收者之间没有直接引用关系，
        发送请求的对象只需要知道如何发送请求，而不必知道如何完成请求。
"""
from abc import ABC, abstractmethod


# 场景：窗口按钮添加快捷键

class FunctionButtonsSettingWindows:
    def __init__(self, title):
        self.title = title
        self.buttons = []

    def add_button(self, button):
        self.buttons.append(button)

    def display(self):
        print('显示窗口功能键：')
        print(f"{' '.join([button.name for button in self.buttons])}")


"""抽象命令类:抽象命令类一般是一个抽象类或接口，在其中声明了用于执行请求的execute()等方法，
             通过这些方法可以调用请求接收者的相关操作。"""


class AbstractCommond(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass


"""具体命令类:具体命令类是抽象命令类的子类，实现了在抽象命令类中声明的方法，它对应具体的接收者对象，将接收者对象的动作绑定其中。
             在实现execute()方法时，将调用接收者对象的相关操作(Action)"""


class HelpCommond(AbstractCommond):
    def __init__(self):
        self.Handler = HelpHandler()
        super().__init__()

    def execute(self):
        self.Handler.display()


class MinimizeWindowsCommond(AbstractCommond):
    def __init__(self):
        self.Handler = MinimizeWindowsHandler()
        super().__init__()

    def execute(self):
        self.Handler.minimize()


"""调用者:调用者即请求发送者，它通过命令对象来执行请求。
         一个调用者并不需要在设计时确定其接收者，因此它只与抽象命令类之间存在关联关系。
         在程序运行时可以将一个具体命令对象注入其中，再调用具体命令对象的execute()方法，
         从而实现间接调用请求接收者的相关操作。"""


class FunctionButton:
    def __init__(self, name):
        self.name = name
        self.commond = None

    def set_commond(self, commond):
        self.commond = commond

    def on_click(self):
        self.commond.execute()


"""接收者:接收者执行与请求相关的操作，它具体实现对请求的业务处理。"""


class HelpHandler:
    def display(self):
        print('显示帮助文档！')


class MinimizeWindowsHandler:
    def minimize(self):
        print('最小化窗口！')

if __name__ == '__main__':
    windows = FunctionButtonsSettingWindows('快捷键窗口')
    button1, button2 = FunctionButton('快捷键1'), FunctionButton('快捷键2')
    commond1,commond2 = HelpCommond(), MinimizeWindowsCommond()
    windows.add_button(button1)
    windows.add_button(button2)

    windows.display()

    button1.set_commond(commond1)
    button2.set_commond(commond2)

    button1.on_click()
    button2.on_click()
