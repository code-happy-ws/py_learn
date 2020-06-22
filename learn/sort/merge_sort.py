def merge(left,right):
    result=[]
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]
    return result

def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = int(len(seq)/2)
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)

if __name__ == '__main__':
    seq = [6, 4, 5, 2, 3, 1]
    print(merge_sort(seq))

