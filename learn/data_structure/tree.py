class Node:
    """节点类"""
    def __init__(self,elem=-1,l_child=None,r_child=None):
        self.elem=elem
        self.l_child=l_child
        self.r_child=r_child

class Tree:
    """二叉树类"""
    def __init__(self):
        self.root=Node()
        # 备份存储左右子节点不全的节点，若两节点已满则删除该节点,
        self.my_quene=[]

    def add(self,elem):
        """为树添加节点"""
        node=Node(elem)
        if self.root.elem==-1:
            # elem默认-1可以防止误判0
            self.root=node
            self.my_quene.append(self.root)
        else:
            tree_node=self.my_quene[0]
            if not tree_node.l_child:
                tree_node.l_child=node
                self.my_quene.append(tree_node.l_child)
            else:
                tree_node.r_child=node
                self.my_quene.append(tree_node.r_child)
                self.my_quene.pop(0) #左右子节点已满，删除该节点备份



class HandleTree():
    def __init__(self):
        self.front_list = []
        self.mid_list = []
        self.last_list = []

    def front_digui(self,root):
        """递归实现前序遍历
        结束条件：该节点无子节点
        """
        if not root:
            return
        self.front_list.append(root.elem)
        self.front_digui(root.l_child)
        self.front_digui(root.r_child)
        return self.front_list

    def front_stack(self,root):
        ret=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                ret.append(root.elem)
                root=root.l_child
            else:
                node=stack.pop()
                root=node.r_child
        return ret

    #
    # def front_stack2(self,root):
    #     """非递归实现前序遍历:栈和队列
    #     思路：先入右节点，再入左节点，取出时从右边取出；
    #         通过栈暂存遍历过的节点，pop取出处理的节点，栈中保存未处理的节点；
    #     """
    #     ret=[]
    #     stack=[root]
    #     while stack:
    #         node=stack.pop()
    #         ret.append(node.elem)
    #         if node.r_child:
    #             stack.append(node.r_child)
    #         if node.l_child:
    #             stack.append(node.l_child)
    #     return ret


    def mid_digui(self,root):
        """递归实现中序遍历
        结束条件：该节点无子节点
        """
        if not root:
            return
        self.mid_digui(root.l_child)
        self.mid_list.append(root.elem)
        self.mid_digui(root.r_child)
        return self.mid_list

    def mid_stack(self,root):
        """非递归实现中序遍历:栈和队列
        思路：依此遍历左子树至最底层节点，并保存至栈，弹出左子树最底层节点并将该节点值保存至数组，如果左子树最底层节点的右子节点为空，
        则弹出栈顶元素（最底层节点的父节点）并将该节点值保存至数组，再处理其右子节点（处理方式同上），如果右子节点不为空，则赋给root重新处理；
        """
        ret=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.l_child
            else:
                node=stack.pop()
                ret.append(node.elem)
                root = node.r_child
        return ret

    def last_digui(self,root):
        """递归实现后序遍历
        结束条件：该节点无子节点
        """
        if not root:
            return
        self.last_digui(root.l_child)
        self.last_digui(root.r_child)
        self.last_list.append(root.elem)
        return self.last_list

    def last_stack(self,root):
        """非递归实现后序遍历:栈和队列
        思路：依此遍历右子树至最底层节点，并保存至栈，遍历时将值自左边依此插入数组，如果右子树最底层节点的右子节点为空，
        则弹出栈顶元素（最底层节点的父节点）并将该节点值保存至数组，再处理其左子节点（处理方式同上），如果左子节点不为空，则赋给root重新处理；
        """
        ret=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                ret.insert(0,root.elem)
                root=root.r_child
            else:
                node=stack.pop()
                root=node.l_child

        return ret


    def mirror(self,root):
        """镜像化二叉树
        思路：递归
        """
        if not root:
            return
        if root:
            root.l_child,root.r_child=root.r_child,root.l_child
            self.mirror(root.l_child)
            self.mirror(root.r_child)

    def print_tree_uptodown(self,root):
        """广度遍历二叉树，从上向下，自左向右
        思路：双向队列，左端弹出要处理的节点，右边加入待处理的节点，直至队列为空"""
        if not root:
            return
        deque=[root]
        ret=[root.elem]
        while deque:
            node=deque.pop(0)
            if node.l_child:
                deque.append(node.l_child)
                ret.append(node.l_child.elem)
            if node.r_child:
                deque.append(node.r_child)
                ret.append(node.r_child.elem)
        return ret

    def find_path(self,tree, num):
        """输入一棵二叉树和一个值，求从根结点到叶结点的和等于该值的路径
        思路：深度优先搜索变形
            关键点1.

            """
        ret = []
        if not tree:
            return ret
        path = [tree.elem]
        def dfs(tree,path):
            if tree.l_child:
                dfs(tree.l_child,path+[tree.l_child.elem])
            if tree.r_child:
                dfs(tree.r_child,path+[tree.r_child.elem])
            if not tree.l_child and not tree.r_child and sum(path) == num:
                    ret.append(path)
        dfs(tree,path)
        return ret


    def get_depth(self,root):
        """获取树的深度
        思路：递归
        """
        if not root:
            return 0
        if not root.l_child and not root.r_child:
            return 1
        return 1+max(self.get_depth(root.l_child),self.get_depth(root.r_child))

    def is_search_tree(self,root):
        """判断是否为二叉搜索树
        思路：中序遍历情况下，值递增则为二叉树;用一中间值保存上一遍历结果，并与下轮结果比较"""
        flag=True
        deque=[]
        ret=0
        while deque or root:
            if root:
                deque.append(root)
                root=root.l_child
            else:
                node=deque.pop()
                if node.elem<ret:
                    flag=False
                    break
                ret=node.elem
                root=node.r_child
        return flag

    def is_complete_tree(self,root):
        """判断是否为完全二叉树
        左有右有 继续遍历
        左有右无或者左无右无 余下必须全为叶节点 否则非完全二叉树
        左无右有 非完全二叉树
        """
        flag=True
        switch=True
        deque=[root]
        while deque:
            node=deque.pop()
            if node.l_child:
                if not switch:
                    break
                deque.append(node.l_child)
                # 左有右有 继续遍历
                if node.r_child:
                    if not switch:
                        break
                    deque.append(node.r_child)
                # 左有右无,余下必须全为叶节点
                else:
                    switch=False
            else:
                #  左无右有 非完全二叉树
                if node.r_child:
                    flag=False
                    break
                # 左无右无, 余下必须全为叶节点
                else:
                    switch=False
        return flag

    def is_avl_tree(self,root):
        """判断是否为平衡二叉树（左右子树深度差不超过1的二叉树）
        思路：先判断当前节点是否平衡，再递归判断左右子节点是否平衡"""
        if not root:
            return True
        l_deep=self.get_depth(root.l_child)
        r_deep=self.get_depth(root.r_child)
        if abs(l_deep-r_deep)<=1:
            return self.is_avl_tree(root.l_child) and self.is_avl_tree(root.r_child)
        else:
            return False





if __name__ == '__main__':
    tree=Tree()
    handle=HandleTree()

    for elem in [6,4,8,3,5,7,9]:
    # for elem in range(1,8):
        tree.add(elem)
    # print(handle.front_stack2(tree.root))
    # print(handle.find_path(tree.root,5))
    print("获取树的深度 —————————————————————")
    print(handle.get_depth(tree.root))
    print(handle.is_search_tree(tree.root))

    # print("非递归实现前序遍历（深度遍历）——————————————————————")
    # print(handle.front_stack(tree.root))

    # print("递归实现前序遍历（深度遍历）——————————————————————")
    # print(handle.front_digui(tree.root))

    # print("递归实现中序遍历（深度遍历）——————————————————————")
    # print(handle.mid_digui(tree.root))

    # print("非递归实现中序遍历（深度遍历）——————————————————————")
    # print(handle.mid_stack(tree.root))

    # print("递归实现后序遍历（深度遍历）——————————————————————")
    # print(handle.last_digui(tree.root))

    # print("递归实现后序遍历（深度遍历）——————————————————————")
    # print(handle.last_stack(tree.root))

    # print("广度遍历——————————————————————")
    # print(handle.print_tree_uptodown(tree.root))
    #
    # print("镜像二叉树——————————————————————")
    # handle.mirror(tree.root)
    # handle.front_list=[]
    # print(handle.front_digui(tree.root))
    #


