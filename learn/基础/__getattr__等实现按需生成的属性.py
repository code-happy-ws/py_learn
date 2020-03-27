
class Food:
    """

    """
    A=1
    def __init__(self):
        self.exist = 1

    def __getattr__(self, item):
        """
        如果类中定义了__getattr__方法，系统在该类的实例字典中找不到待查询的属性时，会调用该方法；
        这种行为非常适合实现无结构数据的按需访问
        hasattr方法会调用__getattr__
        item：
        return；
        """
        print('getattr')
        value = 'value ' + item
        setattr(self, item, value)
        return value


    # def __getattribute__(self, item):
    #     """每次访问对象属性时，都会自动调用该方法，无论属性字典里是否存在该字典。不要和__getattr__一起存在"""
    #     # print('getattribute')
    #     return 'getattribute'

    def __setattr__(self, key, value):
        """为属性赋值时会触发调用"""
        print('setattr')
        # 不加super（）会无限循环递归调用
        super().__setattr__(key, value)


if __name__ == '__main__':
    food = Food()
    print(food.exist)
    print('before', food.__dict__, hasattr(food, 'exist'))
    print(food.noexist)
    print('------------')
    print('after', food.__dict__)
    print(hasattr(food, 'noexist'))
    print('------------')
    food.exist = 2
