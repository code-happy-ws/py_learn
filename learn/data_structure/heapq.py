# 默认是小根堆
import heapq

a = [3, 4, 2, 5, 7, 9, 6]
# 获得前3大元素列表
m = heapq.nlargest(3, a)

# 获得前3小元素列表
n = heapq.nsmallest(3, a)
print('前3大/小:', m, n)

# 形成最小堆--方式一
heap = []
for item in a:
    heapq.heappush(heap, item)
print('heap:', heap)

# 弹出堆顶，其余仍然是最小堆
min_elem = heapq.heappop(heap)
print('after_pop:', heap, min_elem)

# 删除最小元素，替换新的值, 其余仍然是最小堆
heapq.heapreplace(heap, 8)
print('after_replace:', heap)

# 形成最小堆--方式二
b = [3, 4, 2, 5, 7, 9, 6]
heapq.heapify(b)
print(b)

# 最大堆
c = [3, 4, 2, 5, 7, 9, 6]
heapq._heapify_max(c)
print('max_heap:',c)


