def max_heapify(heap,heapSize,root):
    """最大堆调整"""
    left=2*root+1
    right=left+1
    larger=root
    if left<heapSize and heap[larger]<heap[left]:
        larger=left
    if right < heapSize and heap[larger]<heap[right]:
        larger=right
    if larger!=root:
        # 表明需要交换子节点和父节点
        heap[root],heap[larger]=heap[larger],heap[root]
        max_heapify(heap,heapSize,larger)

def build_max_heap(heap):
    """建立最大堆"""
    heap_size=len(heap)
    for i in reversed(range((heap_size+1)//2+1)):
        max_heapify(heap,heap_size,i)

def heap_sort(heap):
    """ 堆排序，将根节点取出与最后一位对调，对前面len-1个节点继续进行堆调整过程，
        最坏O(nlog2n)
    """
    build_max_heap(heap)
    for i in reversed(range(len(heap))):
        heap[0],heap[i]=heap[i],heap[0]
        max_heapify(heap,i,0)
    return heap

if __name__ == '__main__':
    a=[30,50,57,77,62,78,94,80,84]
    heap_sort(a)
    print(a)
