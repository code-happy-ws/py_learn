print('@property装饰器属性重构---------------------------------------------------------')
""" 使用@property 装饰器将一个直接访问的属性转变为函数触发式属性,可实现数值验证或额外的实时运算
    缺点：无法复用移植到其他类使用，可通过描述符改写(推荐),或者mix-in类（混合类）"""

class Person:
    def __init__(self, name):
        print('init')
        self.name = name  # 调用setter
        # print('self.name',self.name)

    @property  # getter方法
    def name(self):
        print('getter')
        return self._name

    @name.setter
    def name(self, name):
        print('setter')
        if name < 10:
            self._name = name * 10
        else:
            self._name = name / 10

class Field:
    """描述符"""
    def __init__(self,name):
        self.name=name
        self.internal_name='_'+self.name

    def __get__(self, instance, owner):
        """
        :param instance: 托管实例（Customer实例food）
        :param owner:托管类引用（Customer）,
        :return:
        """
        if not instance: return self
        return getattr(instance,self.internal_name,'')

    def __set__(self, instance, value):
        """
        :param instance: 托管实例（Customer实例food）
        :param value: 设定值
        :return:
        """
        setattr(instance,self.internal_name,value)

class Customer:
    """以描述符实现属性注解时，需重复写参数，元类可优化"""
    first_name=Field('first_name')

# 元类+描述符实现注解类属性___________________________________________________
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        """可基于元类进行子类验证"""
        # print(meta, name, bases, class_dict)
        for key,value in class_dict.items():
            if isinstance(value,FieldType):
                value.name=key
                value.internal_name='_'+key
        return type.__new__(meta, name, bases, class_dict)

class FieldType:
    """描述符"""
    def __init__(self):
        self.name=None
        self.internal_name=None

    def __get__(self, instance, owner):
        """
        :param instance: 托管实例（Customer实例food）
        :param owner:托管类引用（Customer）,
        :return:
        """
        if not instance: return self
        return getattr(instance,self.internal_name,'')

    def __set__(self, instance, value):
        """
        :param instance: 托管实例（Customer实例food）
        :param value: 设定值
        :return:
        """
        setattr(instance,self.internal_name,value)

class Book(metaclass=Meta):
    """基类"""
    pass

class RedBook(Book):
    """无需重复写参数"""
    last_name=FieldType()

    def __init__(self):
        pass
if __name__ == '__main__':
    P = Person(1000)  # 调用setter
    print(P.name)  # 调用getter

    print("描述符实现属性注解-----------------")
    food=Customer()
    food.first_name='zzw'
    print(Customer.first_name,food.__dict__)

    print("元类+描述符实现属性注解-----------------")
    book=RedBook()
    book.last_name='hws'
    print(book.last_name,book.__dict__)
