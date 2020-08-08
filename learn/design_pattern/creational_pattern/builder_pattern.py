"""
建造者模式：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
    复杂对象是指那些包含多个成员属性的对象,例如汽车包括车身、底盘、轮子等;
优点：
    客户端不必知道产品内部组成的细节，将产品本身与产品的创建过程解耦，使得相同的创建过程可以创建不同的产品对象；
    每个具体建造者都相对独立, 符合 “开闭原则”;
缺点：
    如果产品的内部变化复杂，可能会导致需要定义很多具体建造者来实现这种变化，导致系统变得很庞大；
"""
from abc import ABC, abstractmethod

"""产品角色"""


class Actor:
    def __init__(self):
        self.type = None
        self.sex = None
        self.face = None
        self.hair_style = None

    def set_type(self, type):
        self.type = type

    def set_sex(self, sex):
        self.sex = sex

    def set_face(self, face):
        self.face = face

    def set_hair_style(self, hair_style):
        self.hair_style = hair_style

    def display(self):
        print([self.type, self.face, self.sex, self.hair_style])


"""抽象建造者"""


class AbstractActorBuilder(ABC):
    def __init__(self):
        self.actor = Actor()

    @abstractmethod
    def build_type(self):
        pass

    @abstractmethod
    def build_sex(self):
        pass

    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_hair_style(self):
        pass

    def creat_actor(self):
        return self.actor


"""具体建造者"""


class AngleActorBuilder(AbstractActorBuilder):
    def __init__(self):
        super().__init__()

    def build_type(self):
        self.actor.type = '天使'

    def build_sex(self):
        self.actor.sex = '女'

    def build_face(self):
        self.actor.face = '漂亮'

    def build_hair_style(self):
        self.actor.hair_style = '披肩长发'


class HeroActorBuilder(AbstractActorBuilder):
    def __init__(self):
        super().__init__()

    def build_type(self):
        self.actor.set_type('英雄')

    def build_sex(self):
        self.actor.set_sex('男')

    def build_face(self):
        self.actor.set_face('英俊')

    def build_hair_style(self):
        self.actor.set_hair_style('帅气短发')


"""指挥者"""


class ActorControl:

    @staticmethod
    def construct(builder):
        builder.build_type()
        builder.build_sex()
        builder.build_face()
        builder.build_hair_style()
        return builder.creat_actor()


if __name__ == '__main__':
    control = ActorControl()

    angle_1 = control.construct(AngleActorBuilder())
    angle_1.display()

    angle_2 = control.construct(HeroActorBuilder())
    angle_2.display()
