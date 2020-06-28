"""
输入: [3,30,34,5,9]
输出: str(9534330 )
"""
from copy import copy
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums) -> str:
        _seq=nums[:]
        if not _seq:
            return 0
        _seq.sort(key=cmp_to_key(self.compare))
        return str(int(''.join(map(str,_seq))))

    @staticmethod
    def compare(x,y):
        x_y = int(str(x)+str(y))
        y_x = int(str(y)+str(x))
        if x_y>y_x:
            return -1
        elif x_y<y_x:
            return 1
        else:
            return 0

if __name__ == '__main__':
    seq=[3,30,34,5,9]
    print(Solution().largestNumber(seq))