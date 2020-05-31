def quick_sort(arr,start,end):
    """快速排序：找一基准，将比其大的放一边，比其小的放另一边，递归下去，O（nlog2n）"""
    key=arr[end]
    left=start
    right=end
    if not start <end:
        return

    while right>left:
        while arr[left]<=key and right>left:
            left+=1
        # left位置为目前值大于key的位置，将大于key的值放在right对应位置
        arr[right]=arr[left]

        while arr[right]>key and left<right:
            right-=1
        # right位置为目前值小于key的位置，把该值放到left对应位置
        arr[left]=arr[right]

    arr[left]=key
    print('all:',arr)

    quick_sort(arr,start,left-1)
    quick_sort(arr,left+1,end)

def get_top_min(arr,start,end):
    key=arr[end]
    left=start
    right=end
    if not start <end:
        return

    while right>left:
        while arr[left]<=key and right>left:
            left+=1
        # left位置为目前值大于key的位置，将大于key的值放在right对应位置
        arr[right]=arr[left]

        while arr[right]>key and left<right:
            right-=1
        # right位置为目前值小于key的位置，把该值放到left对应位置
        arr[left]=arr[right]

    arr[left]=key
    print('all:',arr)
    get_top_min(arr,start,left-1)
    get_top_min(arr,left+1,end)

if __name__ == '__main__':
    a=[9,5,2,3,7,1,4,6]
    print(a)
    quick_sort(a,0,7)
    print(a)