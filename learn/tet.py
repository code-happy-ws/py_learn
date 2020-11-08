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

    def build_tree(self, tree):
        """{A:[0,B,G],B:[1,C,D,F],D:[2,E],Z:[0,X]}
        A.c=B B.c=C B.b=G C.b=None c.b=D D.c=E D.b=F A.b=Z Z.c=X
        :param tree:
        :return:
        """


if __name__ == '__main__':
    # num = int(input().strip())
    # dir_tree_lines = [input().strip() for _ in range(num)]
    dir_tree_lines = {'A': ['B', 'G'], 'B': ['C', 'D', 'F'], 'D': ['E']}
    function = DirManage()
    result = function.del_all_dir(dir_tree_lines)
    print(' '.join(result))
