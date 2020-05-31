"""求字符串中第一个只出现一次的字符
思路：保存每个元素的出现次数"""
from collections import OrderedDict
def get_first_once(s):
    if not s:
        return ' '
    times=OrderedDict()
    for k,v in enumerate(s):
        if not times.get(s[k]):
            times[v]=1
        else:
            times[v] += 1
    for k,v in times.items():
        if v==1:
            return k
    else:
        return ' '

if __name__ == '__main__':
    a=""
    print(bool(a))
    # get_first_once(a)