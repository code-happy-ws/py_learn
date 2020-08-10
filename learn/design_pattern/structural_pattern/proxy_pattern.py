""" 代理模式：给某一个对象提供一个代理或占位符，并由代理对象来控制对原对象的访问。
    分类：
        远程代理：为一个位于不同的地址空间的对象提供一个本地的代理对象（例ssh操作远端设备）;
        虚拟代理：如果需要创建一个资源消耗较大的对象，先创建一个消耗相对较小的对象来表示，真实对象只在需要时才会被真正创建;
        保护代理：控制对一个对象的访问，可以给不同的用户提供不同级别的使用权限;
        缓冲代理：某一个目标操作的结果提供临时的存储空间，以便多个客户端可以共享这些结果(例如缓存数据库数据，优先查缓存提高性能);
        智能引用代理：当一个对象被引用时，提供一些额外的操作，例如将对象被调用的次数记录下来等。
    同适配器模式对比：代理模式完全替代了原对象，仅代理一层业务，适配器模式注重于进行匹配，填补不同接口间的缝隙；
"""
from abc import ABC, abstractmethod

"""抽象主题：声明了真实主题和代理主题的共同接口"""


class AbstractSearch(ABC):
    @abstractmethod
    def search(self, user_id, password):
        pass


"""代理主题：包含了对真实主题的引用"""


class ProxySearch(AbstractSearch):
    def __init__(self):
        self.real_search = RealSearch()
        self.user_validate = UserAccssValidate()
        self.logger = Logger()

    def search(self, user_id, password):
        self.user_validate.validate(user_id)
        self.real_search.search(user_id, password)
        self.logger.log(user_id)


"""真实主题：定义了代理角色所代表的真实对象，在真实主题角色中实现了真实的业务操作，
客户端可以通过代理主题角色间接调用真实主题角色中定义的操作"""


class RealSearch(AbstractSearch):
    # 信息查询
    def search(self, user_id, password):
        print(f'{user_id}查询操作完成')


"""以下为业务类，代理主题按需要可调用"""


class UserAccssValidate:
    """系统用户验证"""

    def validate(self, user_id):
        print(f'对{user_id}进行登陆验证')


class Logger:
    """系统用户日志记录"""

    def log(self, user_id):
        print(f'{user_id}操作日志已记录')


if __name__ == '__main__':
    proxy = ProxySearch()
    proxy.search('root', 'admin123')
