# coding:utf-8
# 抽象类虚拟子类

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

@Shape.register # 注册虚拟子类
class House():
    def __init__(self, area):
        self.area = area

    def showArea(self):
        return self.area

# Shape.register(House)  # 注册虚拟子类

house = House(100)  # 重新定义变量
print(house.showArea())
print(issubclass(House, Shape))
print(isinstance(house, Shape))
