"""给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

说明:
假设你总是可以到达数组的最后一个位置。

示例:
输入: [2,3,3,1,2]
输出: 3
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
思路：
    关键点1：确定times加1d的时机，从end_pos走时加1；
    关键点2：！理解前提，题目中有确保一定会达到终点，必须忽略最后一个位置元素，否则很难处理（
    ，若不忽略尾元素，最后一次的max_pos大于尾元素的位置或刚好等于尾元素的位置这两种情况的区分很难处理）；
"""


def skip(nums):
    max_pos = 0
    times = 0
    end_pos = 0
    # 要点：必须忽略最后一个位置元素（原因：题目中有确保一定会达到终点,
    # 最后一次跳跃边界一定大于等于末尾，故忽略）
    for index, step in enumerate(nums[:-1]):
        max_pos = max(max_pos, index + step)
        if index == end_pos:
            times += 1
            end_pos = max_pos
    return times

if __name__ == '__main__':
    position = [2,3,4,1,4,2,1,1]
    # position = [0]
    # position = [1,1,1]
    # position = [2,3,1,1,4]
    print(skip(position))
