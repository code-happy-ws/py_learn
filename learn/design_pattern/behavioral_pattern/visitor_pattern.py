"""访问者模式(Visitor Pattern):提供一个作用于某对象结构中的各元素的操作表示，
它使我们可以在不改变各元素的类的前提下定义作用于这些元素的新操作。
优点：
    1. 增加新的访问操作很方便。使用访问者模式，增加新的访问操作就意味着增加一个新的具体访问者类，
        实现简单，无须修改源代码，符合“开闭原则”。
    2. 将有关元素对象的访问行为集中到一个访问者对象中，而不是分散在一个个的元素类中。
        类的职责更加清晰，有利于对象结构中元素对象的复用，相同的对象结构可以供多个不同的访问者访问。
    3. 让用户能够在不修改现有元素类层次结构的情况下，定义作用于该层次结构的操作。
缺点：
    1. 增加新的元素类很困难。在访问者模式中，每增加一个新的元素类都意味着要在抽象访问者角色中增加一个新的抽象操作，
        并在每一个具体访问者类中增加相应的具体操作，这违背了“开闭原则”的要求。

    2. 破坏封装。访问者模式要求访问者对象访问并调用每一个元素对象的操作，
        这意味着元素对象有时候必须暴露一些自己的内部操作和内部状态，否则无法供访问者访问。
适用场景：
1. 一个对象结构包含多个类型的对象，希望对这些对象实施一些依赖其具体类型的操作。
2. 需要对一个对象结构中的对象进行很多不同的并且不相关的操作，而需要避免让这些操作“污染”这些对象的类，
    也不希望在增加新操作时修改这些类。访问者模式使得我们可以将相关的访问操作集中起来定义在访问者类中，
    对象结构可以被多个不同的访问者类所使用，将对象本身与对象的访问操作分离。
3. 对象结构中对象对应的类很少改变，但经常需要在此对象结构上定义新的操作。
        """

from abc import ABC, abstractmethod
from functools import singledispatch

"""抽象元素：抽象元素一般是抽象类或者接口，它定义一个accept()方法，该方法通常以一个抽象访问者作为参数"""


class Employee(ABC):
    def __init__(self, name, work_hours):
        self._name = name
        self._work_hours = work_hours

    @property
    def name(self):
        return self._name

    @property
    def work_hours(self):
        return self._work_hours

    def accept(self, department):
        pass


"""具体元素：具体元素实现了accept()方法，在accept()方法中调用访问者的访问方法以便完成对一个元素的操作。"""


class FullTimeEmployee(Employee):

    def accept(self, department):
        department.visit(self)


class PartTimeEmployee(Employee):

    def accept(self, department):
        department.visit(self)


"""抽象访问者：抽象访问者为对象结构中每一个具体元素类ConcreteElement声明一个访问操作"""


class Department(ABC):
    """规定了一个兼容接口"""

    @abstractmethod
    def visit(employee):
        """访问员工"""
        pass

    @abstractmethod
    def visit_full_time(self, employee):
        """访问全职员工"""
        pass

    @abstractmethod
    def visit_part_time(self, employee):
        """访问兼职员工"""
        pass


"""具体访问者：具体访问者实现了每个由抽象访问者声明的操作，每一个操作用于访问对象结构中一种类型的元素。"""


class FinanceDeparment(Department):
    """财务部"""

    @singledispatch
    def visit(employee):
        print('财务部处理员工类型异常', type(employee))

    @visit.register(FullTimeEmployee)
    def _(employee):
        print(f'财务部处理全职员工{employee.name}工资:{employee.work_hours * 100}')

    @visit.register(PartTimeEmployee)
    def _(employee):
        print(f'财务部处理兼职员工{employee.name}工资:{employee.work_hours * 80}')

    def visit_full_time(self, employee):
        print(f'财务部处理全职员工{employee.name}工资:{employee.work_hours * 100}')

    def visit_part_time(self, employee):
        print(f'财务部处理兼职员工{employee.name}工资:{employee.work_hours * 80}')


class HRDeparment(Department):
    """财务部"""

    @singledispatch
    def visit(employee):
        print('人力资源部处理员工类型异常', type(employee))

    @visit.register(FullTimeEmployee)
    def _(employee):
        print(f'人力资源部处理全职员工{employee.name}工时:{employee.work_hours}')

    @visit.register(PartTimeEmployee)
    def _(employee):
        print(f'人力资源部处理兼职员工{employee.name}工时:{employee.work_hours}')


"""对象结构：对象结构是一个元素的集合，它用于存放元素对象，并且提供了遍历其内部元素的方法。"""


class EmployeeList:
    def __init__(self):
        self.all_employee = []

    def add_employee(self, employee):
        self.all_employee.append(employee)

    def accept(self, department):
        for employee in self.all_employee:
            employee.accept(department)


if __name__ == '__main__':
    person_1 = FullTimeEmployee('a', 40)
    person_2 = FullTimeEmployee('b', 50)
    person_10 = PartTimeEmployee('c', 100)
    person_20 = PartTimeEmployee('d', 200)

    EMPLOYEE = EmployeeList()
    EMPLOYEE.add_employee(person_1)
    EMPLOYEE.add_employee(person_2)
    EMPLOYEE.add_employee(person_10)
    EMPLOYEE.add_employee(person_20)

    EMPLOYEE.accept(HRDeparment)
    EMPLOYEE.accept(FinanceDeparment)
