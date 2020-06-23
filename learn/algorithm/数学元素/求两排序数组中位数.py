"""给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
"""
def get_mid_num_by_bisect(m,n):
    """二分法：转化问题为求第k大数，k为中位数位置"""
    def get_k(k):
        index1,index2=0,0
        while True:
            # 特殊情况
            if index1 == len_m:
                return n[index2+k-1]
            if index2==n:
                return m[index1+k-1]
            if k==1:
                return min(m[index1],n[index2])

            # 正常情况
            new_index1 = min(index1+k//2-1,len_m-1)
            new_index2 = min(index2+k//2-1,len_n-1)
            elem1,elem2 = m[new_index1],n[new_index2]
            if elem1<=elem2:
                k-=new_index1-index1+1
                index1 = new_index1+1
            else:
                k-=new_index2-index2+1
                index2=new_index2+1

    len_m,len_n=len(m),len(n)
    len_m_n=len_m+len_n
    if len_m_n%2:
        return get_k((len_m_n+1)//2)
    else:
        return (get_k(len_m_n//2)+get_k(len_m_n//2+1))/2



def get_mid_num(m,n):
    # 普通方法 O(m+n) 遍历len(m+n)/2+1次
    l_m = len(m)
    l_n = len(n)
    length = l_m+l_n
    left = right = next = 0
    index_m = index_n = 0
    for _ in range(int(length/2)+1):
        left = right
        if index_m< l_m and index_n<l_n and m[index_m]<n[index_n]:
            right = m[index_m]
            index_m+=1
        elif index_m<l_m and index_n<l_n and m[index_m]>=n[index_n]:
            right = n[index_n]
            index_n+=1
        elif index_m==l_m:
            right = n[index_n]
            index_n+=1
        elif index_n==l_n:
            right = m[index_m]
            index_m += 1
    if length%2==0:
        return (right+left)/2.0
    else:
        return float(right)

if __name__ == '__main__':
    m = [1,5]
    n = [4]
    print(get_mid_num(m,n))
    print(get_mid_num_by_bisect(m,n))
