"""
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。"""
class Solution:
    def firstMissingPositive(self, nums):
        """ 就地算法a[n]为负值表示n存在
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # 基本情况
        if 1 not in nums:
            return 1

        # nums = [1]
        if n == 1:
            return 2

        # 用 1 替换负数，0，
        # 和大于 n 的数
        # 在转换以后，nums 只会包含
        # 正数
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # 使用索引和数字符号作为检查器
        # 例如，如果 nums[1] 是负数表示在数组中出现了数字 `1`
        # 如果 nums[2] 是正数 表示数字 2 没有出现
        for i in range(n):
            a = abs(nums[i])
            # 如果发现了一个数字 a - 改变第 a 个元素的符号
            # 注意重复元素只需操作一次
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])

        # 现在第一个正数的下标
        # 就是第一个缺失的数
        for i in range(1, n):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return n

        return n + 1

    def firstMissingPositive_2(self, nums) -> int:
        """非就地算法"""
        if not nums:
            return 1
        length = len(nums)
        inters = list(range(1, length + 1))
        counts = [1]*length
        dict_info = dict(zip(inters,counts))
        for num in nums:
            count = dict_info.get(num)
            if count is not None:
                dict_info[num]-=1
        print(dict_info.items())
        for k,v in dict_info.items():
            if v==1:
                return k
        else:
            return k+1