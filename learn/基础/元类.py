class Meta(type):
    def __new__(meta, name, bases, class_dict):
        """可基于元类进行子类验证"""
        print(meta, name, bases, class_dict)
        if class_dict.get('hws')=='my love':
            print('hws is my love')
        else:
            print("hws is zzw's love")
        return type.__new__(meta, name, bases, class_dict)


class MyClass(metaclass=Meta):
    hws = 'my love'

    def foo(self):
        pass


if __name__ == '__main__':
    myclass = MyClass()
