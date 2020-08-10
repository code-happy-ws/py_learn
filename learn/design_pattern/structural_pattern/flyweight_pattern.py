""" 享元模式：运用共享技术有效地支持大量细粒度对象的复用。
             系统只使用少量的对象，而这些对象都很相似，状态变化很小，可以实现对象的多次复用(例 五子棋状态)。
             由于享元模式要求能够共享的对象必须是细粒度对象，因此它又称为轻量级模式；

    享元对象能做到共享的关键是区分了内部状态(Intrinsic State)和外部状态：
             内部状态：存储在享元对象内部并且不会随环境改变而改变的状态，内部状态可以共享；
             外部状态：外部状态是随环境改变而改变的、不可以共享的状态；

    享元池： 在享元模式中，存储共享实例对象的地方称为享元池（例如26个字母）；

    优点: 1.可以极大减少内存中对象的数量,可以节约系统资源，提高系统性能。
         2.享元模式的外部状态相对独立，而且不会影响其内部状态，从而使得享元对象可以在不同的环境中被共享。

    缺点：系统变得复杂；

    应用场景: 1.一个系统有大量相同或者相似的对象，造成内存的大量耗费；
             2.需要多次重复使用享元对象；
             3.对象的大部分状态都可以外部化，可以将这些外部状态传入对象中。
"""
from abc import ABC, abstractmethod
from threading import Lock

"""抽象享元类"""


class AbstractChessman(ABC):

    def display(self, coordinate):
        print(f'此棋子为{self.get_color()}棋子,坐标为{coordinate.x, coordinate.y}')

    @abstractmethod
    def get_color(self):
        pass


"""具体享元类"""


class BlackChessman(AbstractChessman):

    def get_color(self):
        return '黑色'


class WhiteChessman(AbstractChessman):

    def get_color(self):
        return '白色'


"""享元工厂类：在实现享元工厂类时我们使用了单例模式和简单工厂模式，
             确保了享元工厂对象的唯一性，并提供工厂方法来向客户端返回享元对象。
"""


class ChessmanFactory:
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(ChessmanFactory, '_instance'):
            with cls._lock:
                if not hasattr(ChessmanFactory, '_instance'):
                    cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # 充当享元池
        self.flyweight_pool = {}
        self.__make_factory()

    def __make_factory(self):
        black_chessman = BlackChessman()
        white_chessman = WhiteChessman()
        self.flyweight_pool['black'] = black_chessman
        self.flyweight_pool['white'] = white_chessman

    def get_chessman(self, color):
        return self.flyweight_pool.get(color)


"""外部状态类"""


class Coordinate:
    """坐标"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


"""非共享具体享元类: 需要时使用"""

if __name__ == '__main__':
    factory = ChessmanFactory()
    chessman1 = factory.get_chessman('white')
    chessman2 = factory.get_chessman('white')
    chessman3 = factory.get_chessman('black')
    chessman4 = factory.get_chessman('black')

    print(chessman1 is chessman2)

    chessman1.display(Coordinate(1, 3))
    chessman3.display(Coordinate(2, 4))
