from random import randint
from collections import namedtuple
""" filter() è§£æå¼æŒ‰æ¡ä»¶ç­›é€‰"""
a='''from random import randint
data=[randint(-10,10) for x in range(100000)]
print(data)
data_after=filter(lambda x:x>2,data)
print(list(data_after))'''

# åˆ—è¡¨è§£ææ›´å¿«
b="""
data=[randint(-10,10) for x in range(100000)]   
print(data)
data_after=[x for x in data if x>2]
print(list(data_after))"""

# from timeit import timeit
# # ç¨‹åºæ‰§è¡Œè®¡æ—¶
# print(timeit(a,number=1))
# print(timeit(b,number=1))

a={'b':56,'c':68,'d':75}
m={k:v for k,v in a.items() if v>60}
print(m)
print('-'*30)


"""ä¸ºå…ƒç»„æ¯ä¸ªå…ƒç´ å‘½åï¼Œæé«˜ç¨‹åºå¯è¯»æ€§"""
s=('Tom','16','male')
# æ–¹æ³•1
NAME,AGE,SEX=range(3)
print(s[AGE])

#æ–¹æ³•2

Student=namedtuple('stu',['name','age','sex'])
s1=Student('Tom','16','male')
print(s1)
print(s1.name)
print('-'*30)

"""sorted()ç»Ÿè®¡å…ƒç´ å‡ºç°æ¬¡æ•°"""
aa=[randint(0,10) for x in range(10)]
bb=dict.fromkeys(aa,0)
print(aa)
for a in aa:
    bb[a]+=1
print(bb)
# æŒ‰é”®æ’åº
bbb=sorted(bb.items(),key=lambda bb:bb[0],reverse=False)
print(bbb)
# æŒ‰å€¼æ’åº
bbbb=sorted(bb.items(),key=lambda bb:bb[1],reverse=False)
print(bbbb)
# bbb={k:v for k,v in bb.items()  }

