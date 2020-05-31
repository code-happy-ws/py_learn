"""
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（字符由英文字母和数字0-9组成，不区分大小写。下同）
？：匹配1个字符

输入：
通配符表达式；
一组字符串。

输出：
返回匹配的结果，正确输出true，错误输出false

注意：
    1.若返回为None可能是有多组待测数据，通过while True循环；
    2.认真审题：匹配的不是前面字符串，为当前位置；
"""
import re
try:
    while True:
        string_with_symbol=input()
        string_need=input()
        pattern=string_with_symbol.replace('.', '\.').replace('?', '.').replace('*', '[0-9A-z]*')
        result=re.compile(pattern).findall(string_need)
        if result:
            print('true')
        else:
            print('false')
except:
    pass