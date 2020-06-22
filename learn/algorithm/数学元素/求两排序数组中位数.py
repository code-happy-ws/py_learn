"""给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
"""

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
