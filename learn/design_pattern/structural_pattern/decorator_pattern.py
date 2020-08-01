"""装饰模式：动态地给一个对象增加一些额外的职责，就增加对象功能来说，装饰模式比生成子类实现更为灵活。
    装饰模式是一种对象结构型模式。
    装饰模式分类：
        透明模式（标准装饰模式）：具体装饰器类中只有抽象构件类声明的方法；
        半透明模式：具体装饰器类中除了抽象构件类声明的方法外，还有新增方法；
            半透明装饰模式可以给系统带来更多的灵活性，设计相对简单，使用起来也非常方便；
            但是其最大的缺点在于不能实现对同一个对象的多次装饰，而且客户端需要有区别地对待装饰之前的对象和装饰之后的对象。
    优点：
        1.对于扩展一个对象的功能，装饰模式比继承更加灵活性，不会导致类的个数急剧增加。
        2.可以对一个对象进行多次装饰，通过使用不同的具体装饰类以及这些装饰类的排列组合，可以创造出很多不同行为的组合，得到功能更为强大的对象。
        3.具体构件类与具体装饰类可以独立变化，用户可以根据需要增加新的具体构件类和具体装饰类，原有类库代码无须改变，符合“开闭原则”。
    缺点：
        装饰模式提供了一种比继承更加灵活机动的解决方案，但同时也意味着比继承更加易于出错，排错也很困难；
    适用场景：
        1.在不影响其他对象的情况下，以动态、透明的方式给单个对象添加职责；
        2.当不能采用继承的方式对系统进行扩展或者采用继承不利于系统扩展和维护时可以使用装饰模式；例如通过继承会生成大量扩展子类时；
    """

from abc import ABC, abstractmethod

"""抽象构件类：是具体构件和抽象装饰类的共同父类，声明了在具体构件中实现的业务方法，
它的引入可以使客户端以一致的方式处理未被装饰的对象以及装饰之后的对象，实现客户端的透明操作"""


class AbstractComponent(ABC):

    @abstractmethod
    def display(self):
        pass


"""具体构件类：它是抽象构件类的子类，用于定义具体的构件对象，实现了在抽象构件中声明的方法，装饰器可以给它增加额外的职责（方法）"""

class Windows(AbstractComponent):
    def display(self):
        print('显示窗体')


class TextBox(AbstractComponent):
    def display(self):
        print('显示文本框')


class ListBox(AbstractComponent):
    def display(self):
        print('显示列表框')


"""抽象装饰类：它也是抽象构件类的子类，用于给具体构件增加职责，但是具体职责在其子类中实现。
它维护一个指向构件对象的引用，通过该引用可以调用装饰之前构件对象的方法，并通过其子类扩展该方法，以达到装饰的目的。"""


class AbstractComponentDecorator(AbstractComponent):
    def __init__(self, component):
        self.component = component

    def display(self):
        self.component.display()


"""具体装饰类：它是抽象装饰类的子类，负责向构件添加新的职责。
每一个具体装饰类都定义了一些新的行为，它可以调用在抽象装饰类中定义的方法，并可以增加新的方法用以扩充对象的行为。"""


class ScrollBarDecorator(AbstractComponentDecorator):
    def display(self):
        self.set_scroll_bar()
        super().display()

    def set_scroll_bar(self):
        print('为构件增加滚动条！')


class BlackBorderDecorator(AbstractComponentDecorator):
    def __init__(self, component):
        super().__init__(component)

    def display(self):
        self.set_black_bar()
        super().display()

    def set_black_bar(self):
        print('为构件增加黑框！')

    def other_func(self):
        print('其他功能')


if __name__ == '__main__':
    component = Windows()
    # component.display()
    component_with_black_board = BlackBorderDecorator(component)
    component_with_black_board_and_scroll_bar = ScrollBarDecorator(component_with_black_board)
    # component_with_black_board.display()
    component_with_black_board_and_scroll_bar.display()
    component_with_black_board.other_func()
