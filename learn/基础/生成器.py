import re

""" 生成器表达式形式"""
def ye():
    print('start')
    yield 'a'

    yield 'b'
    print('end')
list_ye=(x*3 for x in ye())     # 生成器表达式，获得一个生成器，按需惰性生成元素，节约内存;注 ： 生成器遍历完后需重新生成；
# list_ye=[x*3 for x in ye()]   # 列表表达式，会生成所有元素
# print('~~~~~~~~~~~~~~~~~~~~~')
for i in list_ye:
    print('___________________')
    print(i)

"""re.finditer ： re.findall 函数的惰性版本，返回一个生成器，可节约内存"""
string=" ab  ac  ad  ae"
pattern=re.compile(r'(a[a-z]{1})\s')

for i in re.finditer(pattern,string):
    print(i.group())

# 生成器表达式
iter=(i.group() for i in re.finditer(pattern,string))
for j in iter:
    print(j)
