def merge(times):
    """输入：[1,2,3,5,6,8]
    输出：[[1,4],[5,7],[8,9]]"""
    result = []
    fast = 0
    for pos, time in enumerate(times):
        if pos == fast:
            during = []
            during.append(times[pos])
            fast = pos + 1
            while fast < len(times) and times[fast] == times[fast - 1] + 1:
                fast += 1
            during.append(times[fast - 1] + 1)
            result.append(during)
    print(result)


if __name__ == '__main__':
    merge([1, 3])
