"""
|-B
A
|-B
|-|-C
|-|-D
|-|-|-|-D
|-|-D
|-|-|-E
|-|-F
|-G
Z
|-X
"""
from collections import OrderedDict


class DirManage():
    def __init__(self):
        self.level_flag = '|-'

    def del_all_dir(self, dir_tree):
        """思路：深度优先搜索变形(回溯)
        {'A':['B','G'],'B':['C','D','F'],'D':['E']}
        :param dir_tree:
        :return: [C,E,D,F,B,G,A]
        """
        root = list(dir_tree.keys())[0]
        result = []

        def dfs(dir):
            dir_list = dir_tree.get(dir)
            if not dir_list:
                result.append(dir)
                return
            for dir_name in dir_list:
                dfs(dir_name)
            result.append(dir)

        dfs(root)
        print('res:', result)
        return result

    def clean(self, tree):
        """
        |-B
        A
        |-B
        |-|-C
        |-|-D
        |-|-|-|-D
        |-|-D
        |-|-|-E
        |-|-F
        |-G


        {A:[B,G],B:[C,D,F],D:[E]}
        """
        start = 0
        for pos, elem in enumerate(tree):
            if not elem.startswith(self.level_flag):
                start = pos
                break
        handle_tree = tree[start:]

    def get(self, tree):
        """
        [(0,'A'),(1,'B'),(2,'C'),(2,'D'),(3,'E'),(2,'F'),(1,'G'),(2,'H')]
        {A:[B,G],B:[C,D,F],D:[E],g:[H]}
        """
        dir_level_list = [0] * len(tree)
        dir_dict = OrderedDict()
        dir_last = tree[0][0]
        dir_dict[tree[0][1]] = []
        for pos in range(1, len(tree)):
            level = tree[pos][0]
            dir_name = tree[pos][1]
            if level == tree[pos - 1][0] + 1:
                if dir_dict.get(tree[pos - 1][1]):
                    dir_dict[tree[pos - 1][1]].append(dir_name)
                else:
                    dir_dict[tree[pos - 1][1]] = [dir_name]
                dir_last = tree[pos - 1][1]
                dir_level_list[level - 1] = tree[pos - 1][1]
            if level == tree[pos - 1][0]:
                if dir_dict.get(dir_last):
                    dir_dict[dir_last].append(dir_name)
                else:
                    dir_dict[dir_last] = [dir_name]
            if level < tree[pos - 1][0]:
                father_dir = dir_level_list[level - 1]
                dir_dict[father_dir].append(dir_name)
        return dir_dict



if __name__ == '__main__':
    # num = int(input().strip())
    # dir_tree_lines = [input().strip() for _ in range(num)]
    dir_tree_lines = {'A': ['B', 'G'], 'B': ['C', 'D', 'F'], 'D': ['E']}
    function = DirManage()
    result = function.del_all_dir(dir_tree_lines)
    print(' '.join(result))
