"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""


def get_rain(height):
    """ 双指针
        时间复杂度：O(n)。单次遍历的时间O(n)。
        空间复杂度：O(1)的额外空间。left,right,left_max 和 right_max 只需要常数的空间。
    """
    left = 0
    right = len(height) - 1
    left_max = right_max = 0
    result = 0
    while left <= right:
        # 在某个位置i处，它能存的水，取决于它左右两边的最大值中较小的一个
        # 对于左边元素，left_maxs是可信的，right_max是不可信的
        # 如果left_max<right_max成立，那么它就知道自己能存多少水了。
        # 无论右边将来会不会出现更大的right_max，都不影响这个结果，右侧相似
        if left_max < right_max:
            result += max(0, left_max - height[left])
            left_max = max(left_max, height[left])
            left += 1
        else:
            result += max(0, right_max - height[right])
            right_max = max(left_max, height[right])
            right -= 1
    return result


def get_rain1(height):
    """ 单调栈
    """
    pass


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(get_rain(height))
