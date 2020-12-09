"""给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
"""


def subarraySum(nums, k: int) -> int:
    """思路：前缀和+Hash"""
    sum = 0
    count = 0
    # 保存前缀和及出现次数
    mp = {0: 1}
    for num in nums:
        sum += num
        sum_need = sum - k
        if sum_need in mp:
            count += mp[sum_need]
        if sum in mp:
            mp[sum] += 1
        else:
            mp[sum] = 1
    return count


if __name__ == '__main__':
    a = subarraySum([0, 0, 0], 0)
    print(a)
