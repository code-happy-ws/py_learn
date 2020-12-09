"""只含2 3 5因子的数称为丑数 求第1500个丑数
前十个丑数：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
思路：第n个丑数为前n个中某三个数与2 3 5 积的最小值，通过三个变量暂存者3个数的位置"""


def get_num(n):
    nums = [1]
    t2 = t3 = t5 = 0
    num2 = nums[t2] * 2
    num3 = nums[t3] * 3
    num5 = nums[t5] * 5
    while len(nums) < n:
        while num2 <= nums[-1]:
            t2 += 1
            num2 = nums[t2] * 2
        while num3 <= nums[-1]:
            t3 += 1
            num3 = nums[t3] * 3
        while num5 <= nums[-1]:
            t5 += 1
            num5 = nums[t5] * 5
        nums.append(min(num2, num3, num5))
    return nums[-1]


if __name__ == '__main__':
    get_num(10)
