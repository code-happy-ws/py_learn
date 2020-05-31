#coding=utf-8

# 二分法


# 遍历法 O(n)
def get_mid_num(arr):
    length=len(arr)
    for i in range(1,length):
        if arr[i] >= arr[i-1]:
            pass
        else:
            change_index=i
            remain=length-change_index
            if remain>=change_index:
                index=(remain-change_index)//2+change_index*2
                return arr[index]
            else:
                index=(change_index-remain)//2
                return arr[index]
    else:
        index=length//2
        return arr[index]

print(get_mid_num([1,2,3,4,5,6,7]))