def quick_sort(arr,start,end):
    """快速排序：找一基准，将比其大的放一边，比其小的放另一边，递归下去，O（nlog2n）"""
    key=arr[end]
    left=start
    right=end
    if not start <end:
        return
    print('key:',key)

    while right>left:
        while arr[left]<=key and right>left:
            left+=1
        arr[right]=arr[left]
        print('left:',arr)

        while arr[right]>key and left<right:
            right-=1
        arr[left]=arr[right]
        print('right:',arr)

    arr[left]=key
    print('all:',arr)

    quick_sort(arr,start,left-1)
    quick_sort(arr,left+1,end)


if __name__ == '__main__':
    a=[9,5,2,3,7,1,4,6]
    print(a)
    quick_sort(a,0,7)
    print(a)