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
        """非递归实现前序遍历:栈和队列
        思路：先入右节点，再入左节点，取出时从右边取出；
            通过栈暂存遍历过的节点，pop取出处理的节点，栈中保存未处理的节点；
        """
        ret=[]
        stack=[root]
        while stack:
            node=stack.pop()
            ret.append(node.elem)
            if node.r_child:
                stack.append(node.r_child)
            if node.l_child:
                stack.append(node.l_child)
        return ret

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
        """输入一棵二叉树和一个值，求从根结点到叶结点的和等于该值的路径"""
        ret = []
        if not tree:
            return ret
        path = [tree]
        sums = [tree.val]
        def dfs(tree):
            if tree.left:
                path.append(tree.left)
                sums.append(sums[-1] + tree.left.val)
                dfs(tree.left)
            if tree.right:
                path.append(tree.right)
                sums.append(sums[-1] + tree.right.val)
                dfs(tree.right)
            if not tree.left and not tree.right:
                if sums[-1] == num:
                    ret.append([p.val for p in path])
            path.pop()
            sums.pop()
        dfs(tree)
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


if __name__ == '__main__':
    tree=Tree()
    handle=HandleTree()

    for elem in range(7):
        tree.add(elem)
    print("获取树的深度 —————————————————————")
    print(handle.get_depth(tree.root))

    print("非递归实现前序遍历（深度遍历）——————————————————————")
    print(handle.front_stack(tree.root))

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


