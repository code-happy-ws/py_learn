from random import randint
from collections import namedtuple
""" filter() 解析式按条件筛选"""
a='''from random import randint
data=[randint(-10,10) for x in range(100000)]
print(data)
data_after=filter(lambda x:x>2,data)
print(list(data_after))'''

# 列表解析更快
b="""
data=[randint(-10,10) for x in range(100000)]   
print(data)
data_after=[x for x in data if x>2]
print(list(data_after))"""

# from timeit import timeit
# # 程序执行计时
# print(timeit(a,number=1))
# print(timeit(b,number=1))

a={'b':56,'c':68,'d':75}
m={k:v for k,v in a.items() if v>60}
print(m)
print('-'*30)


"""为元组每个元素命名，提高程序可读性"""
s=('Tom','16','male')
# 方法1
NAME,AGE,SEX=range(3)
print(s[AGE])

#方法2

Student=namedtuple('stu',['name','age','sex'])
s1=Student('Tom','16','male')
print(s1)
print(s1.name)
print('-'*30)

"""sorted()统计元素出现次数"""
aa=[randint(0,10) for x in range(10)]
bb=dict.fromkeys(aa,0)
print(aa)
for a in aa:
    bb[a]+=1
print(bb)
# 按键排序
bbb=sorted(bb.items(),key=lambda bb:bb[0],reverse=False)
print(bbb)
# 按值排序
bbbb=sorted(bb.items(),key=lambda bb:bb[1],reverse=False)
print(bbbb)
# bbb={k:v for k,v in bb.items()  }


# 切片复制并不真正等同于深拷贝，如果列表里有可变对象，会同变
a = [[1,2],[3,4]]
b= a[:]
b[1].append(9)
print(a) # [[1, 2], [3, 4, 9]]


