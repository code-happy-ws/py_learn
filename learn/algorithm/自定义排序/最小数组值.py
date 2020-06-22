"""根据数组值组合出最小的数
思路：需进行自定义排序(冒泡思路)
    比较两元素不同方式的组合和大小"""
from functools import cmp_to_key

def mycmp(a,b):
    if int(str(a)+str(b))-int(str(b)+str(a))>0:
        return 1
    elif int(str(a)+str(b))-int(str(b)+str(a))<0:
        return -1
    else:
        return 0
def min_num(nums):
    n=sorted(nums,key=cmp_to_key(mycmp))
    print(n)


if __name__ == '__main__':
    a=[34,65,123,87]
    min_num(a)
