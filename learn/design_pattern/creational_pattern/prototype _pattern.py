#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
原型模式(Prototype Pattern):用原型实例指定创建对象的种类,并且通过拷贝这些原型创建新的对象;
原型模式是用场景需要大量的基于某个基础原型进行微量修改而得到新原型时使用;
可利用copy/deepcopy模块实现
"""
from copy import copy, deepcopy


class Prototype(object):
    """抽象原型类"""
    def clone(self):
        pass

    def deep_clone(self):
        pass


# 工作经历类
class WorkExperience(object):
    def __init__(self):
        self.time_area = None
        self.company = None

    def set_work_experience(self, time_area, company):
        self.time_area = time_area
        self.company = company


class Resume(Prototype):
    """具体原型类"""
    def __init__(self, name):
        self.name = name
        self.work_experience = WorkExperience()

    def get_person_info(self):
        return [self.name,self.sex,self.age]

    def set_person_info(self, sex, age):
        self.sex = sex
        self.age = age

    def set_work_experience(self, time_area, company):
        self.work_experience.set_work_experience(time_area, company)

    def display(self):
        print(self.name)
        print(self.sex, self.age)
        print('工作经历', self.work_experience.time_area, self.work_experience.company)
        print('-----'*5)

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if __name__ == '__main__':
    obj1 = Resume('andy')
    obj1.set_person_info('男', '28')
    obj1.set_work_experience('2010-2015', 'AA')

    obj2 = obj1.clone()  # 浅拷贝对象
    obj3 = obj1.deep_clone()  # 深拷贝对象


    # obj1.set_person_info('男', '27')  # 修改浅拷贝的对象年龄,保留其他属性
    # obj3.set_person_info('男', '29')
    print(obj1.get_person_info(), obj2.get_person_info(), obj3.get_person_info())
    a = obj1.get_person_info()
    b = obj2.get_person_info()
    c = obj3.get_person_info()
    print(id(a),id(b), id(c))
    print(id(obj1.get_person_info()),id(obj2.get_person_info()),id(obj3.get_person_info()))

    print(a,b,c)

    # obj3.set_work_experience('2016-2017', 'AA')  # 修改深拷贝的对象的工作经历

    obj1.display()
    obj2.display()
    obj3.display()

