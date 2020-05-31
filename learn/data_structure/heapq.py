# 默认是小根堆
import heapq

a=[3,4,2,5,7,9,6]
# 获得前3大元素列表
m=heapq.nlargest(3,a)

# 获得前3小元素列表
n=heapq.nsmallest(3,a)
print(m,n)

heap=[]
for item in a:
    # 形成最小堆
    heapq.heappush(heap,item)

print(heap)
b=heapq.heapify(a)
print(b)