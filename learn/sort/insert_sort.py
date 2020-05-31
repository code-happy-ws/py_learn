def insert_sort(a):
    """前面为已排序列表，后面元素按顺序插入到对应位置 O(n^2)"""
    for i in range(1,len(a)):
        # for j in reversed(range(1,i+1)):
        #     if a[j]<a[j-1]:
        #         a[j],a[j-1]=a[j-1],a[j]
        #     else:
        #         break
        key=a[i]
        j=i
        while a[j-1]>key and j>0 :
            a[j]=a[j-1]
            j-=1
        a[j]=key
    print(a)

if __name__ == '__main__':

    a=[5,3,6,8,1,2,5,3,22,8,88,55,33,22,11]
    insert_sort(a)

