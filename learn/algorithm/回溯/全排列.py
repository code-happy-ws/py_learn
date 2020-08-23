"""给定一个 没有重复 数字的序列，返回其所有可能的全排列。
    输入: [1,2,3]
    输出:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
    思路：思路：深度优先搜索变形(回溯)
"""


def get_all_array(seq):
    if not seq:
        return []
    length = len(seq)
    result = []

    def dfs(first):
        if first == length:
            result.append(seq[:])
            return
        for i in range(first, length):
            print('------')
            print(first,i)
            # print(seq[first], seq[i])
            # 用first选定nums中每个位置，取值是[0, n-1]
            # 用交换来选定first位置上所有可能的元素，
            # 当first=0时有n个元素可以放到first位置
            seq[first], seq[i] = seq[i], seq[first]
            # first位置放好元素之后，用递归去放first+1位置的元素，它有n-1种取值
            print(seq)
            dfs(first + 1)
            # 当将所有位置都放好元素之后函数会return，但别忘了撤销交换操作，
            # 因为此时的first位置还要继续for循环和其它的i位置交换元素.p
            seq[first], seq[i] = seq[i], seq[first]

    dfs(0)
    return result


if __name__ == '__main__':
    seq = [0,1,2]
    print(get_all_array(seq))
