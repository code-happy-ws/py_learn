""" 外观模式：为子系统中的一组接口提供一个统一的入口。外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。

    外观模式是迪米特法则的一种具体实现，通过引入一个新的外观角色可以降低原有系统的复杂度，同时降低客户类与子系统的耦合度。

    示例：web页面的导航栏即为外观模式的体现；

    在以下情况下可以考虑使用外观模式：
       (1) 当要为访问一系列复杂的子系统提供一个简单入口时可以使用外观模式。
       (2) 客户端程序与多个子系统之间存在很大的依赖性。引入外观类可以将子系统与客户端解耦，
           从而提高子系统的独立性和可移植性。
       (3) 在层次化结构中，可以使用外观模式定义系统中每一层的入口，层与层之间不直接产生联系，
           而通过外观类建立联系，降低层之间的耦合度。
"""

"""子系统"""
class SubSystemA:
    def method_a(self):
        print('生火')

class SubSystemB:
    def method_b(self):
        print('放肉')

class SubSystemC:
    def method_c(self):
        print('加盐')

class SubSystemD:
    def method_d(self):
        print('烤箱')


"""外观类"""
class Cook:
    def __init__(self):
        self.system_a = SubSystemA()
        self.system_b = SubSystemB()
        self.system_c = SubSystemC()
        self.system_d = SubSystemD()

    def cook_a(self):
        self.system_a.method_a()
        self.system_b.method_b()
        self.system_c.method_c()
        print('香喷喷的的炒肉')

    def cook_b(self):
        self.system_d.method_d()
        self.system_b.method_b()
        print('香喷喷的烤肉')


if __name__ == '__main__':
    facade = Cook()
    facade.cook_a()
