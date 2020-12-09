import bisect

a = [2, 5, 7]

# bisect.insort(a,8)
# print(a)

l = len(a)
if l % 2 == 0:
    index = l // 2
    r = (a[index] + a[index - 1]) / 2
else:
    index = (l - 1) // 2
    r = a[index]
print(r)

import bisect


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.list, num)

    def findMedian(self) -> float:
        l = len(self.list)
        if l % 2 == 0:
            index = l // 2
            r = (self.list[index] + self.list[index - 1]) / 2
        else:
            index = (l - 1) // 2
            r = self.list[index]
        return r

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
