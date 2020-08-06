""" 桥接（Bridge）是用于把抽象化与实现化解耦，使得二者可以独立变化。
    这种类型的设计模式属于结构型模式，它通过提供抽象化和实现化之间的桥接结构，来实现二者的解耦;
    使用场景： 1、如果一个系统需要在构件的抽象化角色和具体化角色之间增加更多的灵活性，避免在两个层次之间建立静态的继承联系，
                 通过桥接模式可以使它们在抽象层建立一个关联关系。
              2、对于那些不希望使用继承或因为多层次继承导致系统类的个数急剧增加的系统，桥接模式尤为适用。
              3、一个类存在两个独立变化的维度，且这两个维度都需要进行扩展。
    优点： 1、抽象和实现的分离。 2、优秀的扩展能力。 3、实现细节对客户透明。
    缺点：桥接模式的引入会增加系统的理解与设计难度，由于聚合关联关系建立在抽象层，
          要求开发者针对抽象进行设计与编程。"""
from abc import ABC,abstractmethod


class Image(ABC):
    """抽象类"""

    def __init__(self):
        pass

    def set_image_os(self, os):
        self.os = os

    @abstractmethod
    def parse(self, filename):
        pass


class ImageImplement:
    """实现类接口"""

    def __init__(self):
        pass

    def show_image(self):
        pass


class JGPImage(Image):
    """扩充抽象类"""

    def parse(self, filename):
        self.os.show_os()
        print('格式为JPG')


class GIFImage(Image):
    """扩充抽象类"""

    def parse(self, filename):
        self.os.show_image()
        print(f'{filename}显示格式为GIF')


class WindowsImageOS(ImageImplement):
    """具体类实现"""

    def show_image(self):
        print('在windows系统显示图片')


class UnixImageOS(ImageImplement):
    """具体类实现"""

    def show_image(self):
        print('在Unix系统显示图片')

if __name__ == '__main__':
    image = GIFImage()
    image.set_image_os(UnixImageOS())
    image.parse('abc.gif')