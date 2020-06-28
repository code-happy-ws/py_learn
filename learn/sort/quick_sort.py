def quick_sort(arr, start, end):
    """快速排序：分治法,找一基准，将比其大的放一边，比其小的放另一边，递归下去，O（nlogn）"""
    key = arr[end]
    left = start
    right = end
    if not start < end:
        return

    while right > left:
        while arr[left] <= key and left < right:
            left += 1
        # left位置为目前值大于key的位置，将大于key的值放在right对应位置
        arr[right] = arr[left]

        while arr[right] > key and left < right:
            right -= 1
        # right位置为目前值小于key的位置，把该值放到left对应位置
        arr[left] = arr[right]


    arr[left] = key
    quick_sort(arr, start, left - 1)
    quick_sort(arr, left + 1, end)


class Sort():
    def __init__(self):
        self.top = None

    def get_top_min(self, arr, start, end, top_k):
        """求第k小数 ,分治法(减治法,典型二分查找),时间复杂度O(n) << n+n/2+n/4+n/8+...+n/n==2n
        最坏情况下O(n^2)"""
        key = arr[end]
        left = start
        right = end
        if not start < end:
            return

        while right > left:
            while arr[left] <= key and right > left:
                left += 1
            # left位置为目前值大于key的位置，将大于key的值放在right对应位置
            arr[right] = arr[left]

            while arr[right] > key and left < right:
                right -= 1
            # right位置为目前值小于key的位置，把该值放到left对应位置
            arr[left] = arr[right]

        arr[left] = key

        if top_k < left:
            self.get_top_min(arr, start, left - 1, top_k)
        elif top_k > left:
            self.get_top_min(arr, left + 1, end, top_k)
        else:
            self.top = arr[:top_k]
            return


if __name__ == '__main__':
    a = [9, 5, 3, 8, 5,4, 7,9,6]
    # print(a)
    quick_sort(a, 0, 8)
    print(a)
    # SORT = Sort()
    # SORT.get_top_min(a,0,6,1)
    # print(SORT.top)
