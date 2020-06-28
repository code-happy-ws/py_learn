# # 获得单行输入列表
# nums = list(map(int, input().split()))
#
# # 先制定输入行数，再得到输入列表
# num = int(input())
# disk_list = []
# for _ in range(num):
#     disk_list.append(input())
#
# # 牛客网代码样式
#     while True:
#         try:
#             pass
#         except:
#             break

# 运算
print(9/2) # 4.5 默认float
print(9//2) # 4 取整
print(9%2) # 1 取余
round(2.51,1) # 2.5保留小数 类型为float
a = '%.2f'%6.358 # 6.36 保留小数，类型为str
print(9**0.5) #幂运算

# 位运算
# & 与：全1则1
# | 或：有1则1
# ^ 异或：不同时为1
# 同或：相同为1
# ~：取反
b=[1,8,9,1,3,2]
bb=b[0]
for i in b[1:]:
    bb=(bb^i)
print(bb)
print('result:', ~(4^2))

#倒序遍历
for i in range(3,0,-1):
    print(i)
