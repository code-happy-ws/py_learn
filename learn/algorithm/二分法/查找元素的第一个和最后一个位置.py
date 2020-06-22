class Solution:
    def search_range(self, nums, target):
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if target > mid:
                pass
            if target < mid:
                pass


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    Solution().search_range()
