class LNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class Link:
    def __init__(self,data):
        self.data=data
        self.head=None
        self.init(self.data)

    def init(self,datas):
        self.head=LNode(datas[0])
        p=self.head
        for d in datas[1:]:
            p.next=LNode(d)
            p=p.next

    def show_link(self):
        result=[]
        p=self.head
        while p:
            result.append(p.data)
            p=p.next
        print(result)

    def revert(self):
        """链表反转"""
        p_head=None
        p=self.head
        while p.next:
            s = p.next
            p.next=p_head
            p_head=p
            p=s
        # 处理链头
        p.next=p_head
        self.head=p
        self.show_link()

class HandleLink:
    def __init__(self):
        pass

    def revert_print(self,p):
        """递归倒序打印
        思路：明确递归总体思路：当该节点不为尾节点时，递归查看下一节点
             关键点1：递归参数：节点->下一节点
             关键点2：最底层递归结束条件：节点为空（尾节点）
             关键点3：每次递归返回到上层时动作：打印该层值，
        """
        if p.next:
            self.revert_print(p.next)
        print(p.data)

    def merge_link(self,linkHead1,linkHead2):
        """合并两个有序链表
        思路：每次把两个链表头部较小的一个与剩下的元素的 merge 操作结果合并
            关键点1：递归参数：（l1节点，l2节点）->(l1.next,l2节点) 或（l1节点，l2.next）
            关键点2：最底层递归结束条件：l1节点为None时，表明L2剩余节点都比l1大了，故返回l2目前节点，作为l1尾节点的后驱节点
            关键点3：每次递归返回到上层时动作：返回递归时较小的节点给上一次层递归（return），即上一次递归的节点后驱节点为当前递归返回值（l1 l2中较小节点）；
        """
        if not linkHead1:
            return linkHead2
        if not linkHead2:
            return linkHead1


        if linkHead1.data < linkHead2.data:
            linkHead1.next=self.merge_link(linkHead1.next,linkHead2)
            return linkHead1
        else:
            linkHead2.next=self.merge_link(linkHead1,linkHead2.next)
            return linkHead2

    def merge_link2(self,linkHead1,linkHead2):
        """非递归:建一个虚拟节点，并移动依次连上两链表中较小的那个节点
        """
        p = LNode(-1)
        head=LNode(-1)
        while linkHead1 and linkHead2:
            if linkHead1.data < linkHead2.data:
                head.next=linkHead1
                head=linkHead1
                linkHead1=linkHead1.next
            else:
                head.next=linkHead2
                head=linkHead2
                linkHead2=linkHead2.next

        # 连接上后续节点
        head.next=linkHead2 or linkHead1
        return p.next



if __name__ == '__main__':
    handle=HandleLink()
    data=[1,3,5,7,8]
    l1=Link(data)

    data2=[2,4,5,6]
    l2 = Link(data2)
    print('合并两个有序链表_________')
    handle.merge_link(l1.head,l2.head)
    l1.show_link()
    # handle.merge_link2(l1.head,l2.head)
    # l1.show_link()
    # print('反转打印链表————————————————')
    # handle.revert_print(l1.head)
