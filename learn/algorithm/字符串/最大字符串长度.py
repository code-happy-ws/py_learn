"""
输出字符串中最长的数字字符串和它的长度。如果有相同长度的串，则要一块儿输出，但是长度还是一串的长度
输入：abcd12345ed125ss123058789
输出：123058789,9
关键：
    1.考虑时间超时，较少手动遍历与列表对象频繁创建
    2.break 关键
"""
import re

while True:
    try:
        datas = input()
        datas_new = [i for i in re.compile(r'[^0-9]+').split(datas)]
        max_length = max([len(i) for i in datas_new])
        max_list = []
        for data in datas_new:
            length = len(data)
            if length == max_length:
                max_list.append(data)
        print(''.join(max_list) + ',' + str(max_length))
    except Exception as e:
        break

# 自定义分隔符
# a='1as2da234sds4'
# print([i for i in re.compile(r'[^0-9]+').split(a)])
