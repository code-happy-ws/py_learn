"""给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

思路：
    关键点1：记录最大步长，超过数组长度结尾True
    关键点2：需考虑能否继续进行步进，例如[3,2,1,0,4]在0处无法向后步进，即当前最大步长<下一位置索引时，无法继续步进，返回False；
"""


def skip(nums):
    length = len(nums)
    max_step = 0
    for index, step in enumerate(nums):
        if max_step >= index:
            max_step = max(max_step, index + step)
            if max_step >= length - 1:
                return True
        else:
            break
    return False


if __name__ == '__main__':
    position = [3, 2, 1, 0, 4]
    print(skip(position))
