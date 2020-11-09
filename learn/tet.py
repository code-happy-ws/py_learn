"""
A
|-B
|-|-C
|-|-D
|-|-|-E
|-|-F
|-G
|-|-H


{A:[B,G],B:[C,D,F],D:[E],g:[H]}

[(0,'A'),(1,'B'),(2,'C'),(2,'D'),(3,'E'),(2,'F'),(1,'G'),(2,'H')]
[C,E,D,F,B,H,G,A]
"""
from collections import OrderedDict

level_flag = '|-'


def get(tree):
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
    a = [(0, 'A'), (1, 'B'), (2, 'C'), (2, 'D'), (3, 'E'), (2, 'F'), (1, 'G'), (2, 'H')]
    b = get(a)
    print(b)
