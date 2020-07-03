"""最长连续序列
输入：[100,1,101,2,4,3,2]
输出：4  [1,2,3,4]
"""


def get_max_seq(nums):
    max_seq = 0
    for num in nums:
        if num-1 not in nums:
            length = 1
            next_num = num + 1
            while next_num\
                    in nums:
                next_num += 1
                length += 1
            max_seq = max(max_seq, length)
    return max_seq

class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == '__main__':
    seq = [5,4,3,2]
    print(get_max_seq(seq))
