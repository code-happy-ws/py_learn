"""迷宫伪码"""
from collections import deque


class Node:
    def __init__(self, state, parent, cost=0):
        self.state = state  # 位置状态[行号，列号]
        self.parent = parent
        self.cost = cost

    def dfs(self, initial, goal_test):
        """ 栈实现dfs(结果非最短路径)
        :param initial: 初始元素
        :param goal_test: 判断是否为目标元素
        :return:
        """
        # 栈存放已使用的元素
        used_node = [Node(initial, None)]
        used_state = {initial}

        while len(used_node) > 0:
            # 栈：先进后出
            current_node = used_node.pop()
            if goal_test(current_node):
                return current_node
            for child in [[current_node.state.row + 1, current_node.state.column],
                          [current_node.state.row - 1, current_node.state.column],
                          [current_node.state.row, current_node.state.column + 1],
                          [current_node.state.row, current_node.state.column - 1]]:
                if child in used_state:
                    continue
                used_node.append(Node(child, current_node))
                used_state.add(child)
        return None

    def bfs(self, initial, goal_test):
        """ 队列实现bfs，离起点最近的状态最先被搜索到(结果为最短路径)
        :param initial: 初始元素
        :param goal_test: 判断是否为目标元素
        :return:
        """
        # 队列存放已使用的元素
        used_node = deque([Node(initial, None)])
        used_state = {initial}

        while len(used_node) > 0:
            # 队列：先进先出
            current_node = used_node.popleft()
            if goal_test(current_node):
                return current_node
            for child in [[current_node.state.row + 1, current_node.state.column],
                          [current_node.state.row - 1, current_node.state.column],
                          [current_node.state.row, current_node.state.column + 1],
                          [current_node.state.row, current_node.state.column - 1]]:
                if child in used_state:
                    continue
                used_node.append(Node(child, current_node))
                used_state.add(child)
        return None

    def node_to_path(self, node):
        """打印路径"""
        path = [node.state]
        while node.path is not None:
            node = node.parent
            path.append(node.state)
        path.reverse()
        return path
