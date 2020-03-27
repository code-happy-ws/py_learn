from sort.insert_sort import insert_sort

def bucket_sort(a):
    """桶排序，将数据分至若干个桶，适用于数据均匀分布于0-1之间"""
    s=[[] for i in range(len(a))]
    b=[]
    for i in a:
        s[int(i*len(a))].append(i)
    for i in s:
        b.extend(i)
    return b
if __name__ == '__main__':
    a=[0.8,0.3,0.1,0.9,0.5]
    print(insert_sort(a))
    b=bucket_sort(a)
    print(b)