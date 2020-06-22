"""
输入：
3
1T
20M
3G
输出：
从小到大排序
"""
from functools import cmp_to_key
def compare_disk(a,b):
    a_num=get_num(a)
    b_num = get_num(b)
    if a_num>b_num:
        return 1
    elif a_num<b_num:
        return -1
    else:
        return 0

def sort_disk():
    while True:
        try:
            num=int(input())
            disk_list=[]
            for _ in range(num):
                disk_list.append(input())
            # disk_sorted=sorted(disk_list,key=lambda x:get_num(x))
            disk_sorted=sorted(disk_list,key=cmp_to_key(compare_disk))
            for disk in disk_sorted:
                print(disk)
        except:
            break

def get_num(a):
    a_num=None
    if a[-1]=='M':
        a_num=int(a[:-1])
    elif a[-1]=='G':
        a_num=int(a[:-1])*1000
    elif a[-1]=='T':
        a_num = int(a[:-1]) * 1000000
    return a_num


if __name__ == '__main__':
    sort_disk()