"""盒子中装有3个红球，3个蓝球，4个黄球，从中抽取三次，每次抽一个球，取完不放回，则每种颜色球各得一个的概率是多少"""
import random

def get_propority(balls):
    count = 0
    for _ in range(100000):
        balls_copy = balls[:]
        balls_get = []
        for _ in range(3):
            index = random.randint(0, len(balls_copy)-1)
            balls_get.append(balls_copy[index])
            balls_copy.remove(balls_copy[index])
        if len(set(balls_get)) == 3:
            count += 1
    print(count)

balls = ['r', 'r', 'r', 'b', 'b', 'b', 'y', 'y', 'y', 'y']

get_propority(balls)
# count=0
# import random
# for i in range(100000):
#     index = random.randint(0,9)
#     if index==1:
#         count+=1
# print(count)