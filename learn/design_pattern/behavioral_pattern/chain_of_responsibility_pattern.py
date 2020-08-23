""" 职责链模式：避免请求发送者与接收者耦合在一起，让多个对象都有可能接收请求，将这些对象连接成一条链，
                并且沿着这条链传递请求，直到有对象处理它为止。
    注：职责链模式并不创建职责链，职责链的创建工作必须由系统的其他部分来完成，一般是在使用该职责链的客户端中创建职责链，
        职责链模式降低了请求的发送端和接收端之间的耦合，使多个对象都有机会处理这个请求；
    优点：
        1.职责链模式使得一个对象无须知道是其他哪一个对象处理其请求，对象仅需知道该请求会被处理即可；
          接收者和发送者都没有对方的明确信息，且链中的对象不需要知道链的结构，由客户端负责链的创建，降低了系统的耦合度
        2.请求处理对象仅需维持一个指向其后继者的引用，而不需要维持它对所有的候选处理者的引用，可简化对象的相互连接；
        3.在给对象分派职责时，职责链可以给我们更多的灵活性，可以通过在运行时对该链进行动态的增加或修改来增加或改变处理一个请求的职责；
        4.在系统中增加一个新的具体请求处理者时无须修改原有系统的代码，符合开闭原则；
    缺点：
        1.一个请求也可能因职责链没有被正确配置而得不到处理；
        2.链过长调试困难；
        3.如果建链不当，可能会造成循环调用，将导致系统陷入死循环；
"""
from abc import ABC, abstractmethod

"""抽象处理者"""


class AbstractApprover(ABC):
    def __init__(self):
        pass

    def set_successor(self, successor):
        self.successor = successor


"""具体处理者"""


class Manager(AbstractApprover):
    def handle_request(self, request):
        if request < 5000:
            print(f'经理处理中，金额为{request}元')
        else:
            self.successor.handle_request(request)


class VicePresident(AbstractApprover):
    def handle_request(self, request):
        if 10000 >= request >= 5000:
            print(f'副董事长处理中，金额为{request}元')
        else:
            self.successor.handle_request(request)


class President(AbstractApprover):
    def handle_request(self, request):
        print(f'董事长处理中，金额为{request}元')

if __name__ == '__main__':
    C = Manager()
    B = VicePresident()
    A = President()

    C.set_successor(B)
    B.set_successor(A)

    C.handle_request(1000)

