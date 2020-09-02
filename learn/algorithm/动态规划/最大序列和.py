"""最大连续序列和"""
test = [2, -1, 4, -2, 1]
result = 5


class Solution:
    def maxSubArray(self, nums: list) -> int:
        """动态规划"""
        result = 0
        max_num = 0
        for i, v in enumerate(nums):
            max_num = max(max_num + v, v)
            result = max(max_num, result)
        return result


if __name__ == '__main__':
    a = Solution().maxSubArray(test)
    print(a)
