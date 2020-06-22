def max_heapify(heap, heapSize, root_index):
    """最大堆调整：子堆为最大堆情况下，堆顶更换后进行调整
    heapSize:堆大小,从root_index开始从0计数
    root:子堆顶索引编号
    O(logn)"""
    left = 2 * root_index + 1
    right = left + 1
    larger = root_index

    if left < heapSize and heap[larger] < heap[left]:
        larger = left
    if right < heapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root_index:
        heap[root_index], heap[larger] = heap[larger], heap[root_index]
        max_heapify(heap, heapSize, larger)


def build_max_heap(heap):
    """建立最大堆"""
    heap_size = len(heap)
    for i in reversed(range((heap_size + 1) // 2 + 1)):
        max_heapify(heap, heap_size, i)


def heap_sort(heap):
    """ 堆排序，将根节点取出与最后一位对调，
        对前面len-1个节点继续进行堆调整过程，
        最坏O(nlogn)
    """
    build_max_heap(heap)
    for i in reversed(range(len(heap))):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)
    return heap


def get_min_k(heap, k):
    """获取最小的k个数，维护k个元素的最大堆，那其他元素与堆顶比较，若小于堆顶
    ，就替换，重新维护最大堆，最后不在堆里的n-k个元素都比堆里元素大，及堆为最小k
    时间复杂度：k+(n-k)logk >> O(nlogk)"""
    heap_k = heap[:k]
    heap_other = heap[k:]
    build_max_heap(heap_k)
    for i in range(len(heap_other)):
        if heap_other[i] < heap_k[0]:
            heap_k[0] = heap_other[i]
            max_heapify(heap_k, k, 0)
    print(heap_k)


if __name__ == '__main__':
    a = [5, 4, 7, 8, 1, 3, 9, 6]
    # heap_sort(a)
    # get_min_k(a, 5)
    # 堆模块使用
    import heapq
    heapq._heapify_max(a)
    print(a)
    heap = []
    for i in a:
        heapq.heappush(heap, i)

    print(heap)
