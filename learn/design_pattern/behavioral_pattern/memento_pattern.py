"""备忘录模式(Memento Pattern)：在不破坏封装的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态，
这样可以在以后将对象恢复到原先保存的状态。"""

"""象棋悔棋设计"""

"""原发器:可以创建一个备忘录，并存储它的当前内部状态，也可以使用备忘录来恢复其内部状态，一般将需要保存内部状态的类设计为原发器"""


class Chessman:
    def __init__(self, label, x, y):
        self.x = x
        self.y = y
        self.label = label

    def set_lable(self, label):
        self.label = label

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_lable(self):
        return self.label

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def save(self):
        return ChessmanMemento(self.label, self.x, self.y)

    def restore(self, memento):
        self.label = memento.get_label()
        self.x = memento.get_x()
        self.y = memento.get_y()


"""备忘录:存储原发器的内部状态，根据原发器来决定保存哪些内部状态。备忘录的设计一般可以参考原发器的设计，根据实际需要确定备忘录类中的属性。
需要注意的是，除了原发器本身与负责人类之外，备忘录对象不能直接供其他类使用"""


class ChessmanMemento:
    def __init__(self, label, x, y):
        self.x = x
        self.y = y
        self.label = label

    def set_lable(self, label):
        self.label = label

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_lable(self):
        return self.label

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


"""负责人:负责人又称为管理者，它负责保存备忘录，但是不能对备忘录的内容进行操作或检查。在负责人类中可以存储一个或多个备忘录对象，
它只负责存储对象，而不能修改对象，也无须知道对象的实现细节。"""


class MementiCaretaker:
    def get_memento(self):
        return ChessmanMemento

    def set_memento(self, memento):
        self.memento = memento

if __name__ == '__main__':
    MC= MementiCaretaker()
    chess = Chessman('马',4,3)
    MC.set_memento(chess.save())
    chess.set_y(10)
    