# import re
# from copy import copy, deepcopy
# # s='everyone'
# # pattern = re.compile('every|eve')
# # result = re.search(pattern,s)
# class A:
#     def __init__(self):
#         self.b='a'
#
#     def a(self):
#         return [1,2]
# p=A()
# m=copy(p)
# n = deepcopy(p)
# q = A()
# print(id(p),id(m),id(n),id(q))
# A=p.a()
# B=m.a()
# C=n.a()
# print(id(p.a()),id(m.a()),id(n.a()),type(q.a()),id([1,2]))
# print(id(A),id(B),id(C),type(A))
# print(A,B,C)
# # pattern = re.compile('(?:[^"]|.)+')
# # result = re.search(pattern, p)
# # print(result.group())
a=[1,2]
b=a
b.append(3)
a.append(4)
print(a,b)

