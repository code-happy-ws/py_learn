#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
原型模式(Prototype Pattern):用原型实例指定创建对象的种类,并且通过拷贝这些原型创建新的对象;
原型模式是用场景需要大量的基于某个基础原型进行微量修改而得到新原型时使用; （以修改简历为例）
可利用copy/deepcopy模块实现
    copy:浅复制，顶层复制，内部引用；修改互相影响
    deepcopy:深复制，递归复制；修改彼此独立
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

    def get_work_experience(self):
        return self.work_experience

    def set_person_info(self, sex, age):
        self.sex = sex
        self.age = age

    def set_work_experience(self, time_area, company):
        self.work_experience.set_work_experience(time_area, company)

    def display(self):
        print(self.name)
        print(self.sex, self.age)
        print('工作经历', self.work_experience.time_area, self.work_experience.company)
        print('-----' * 5)

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

    obj2.set_work_experience('2016-2017', 'AA')  # 修改浅拷贝的对象的工作经历

    print(id(obj1.get_work_experience()),
          id(obj2.get_work_experience()),
          id(obj3.get_work_experience()))  # 对比可发现，浅复制对象复制引用，深复制对象做完全复制；

    obj3.set_work_experience('2018-2020', 'AA')  # 修改深拷贝的对象的工作经历

    obj1.display()
    obj2.display()
    obj3.display()
