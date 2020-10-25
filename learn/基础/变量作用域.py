print('嵌套列表创建问题——————————————————————————')
"""存在引用问题"""
min_sum1 = [[0, 0, 0]] * 2
min_sum1[0][0] = 1
print(min_sum1)

"""可修改为以下"""
min_sum2 = [[0] * 3 for _ in range(2)]
min_sum2[0][0] = 1
print(min_sum2)
