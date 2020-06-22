"""从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值"""


def get_advance_num():
    while True:
        length_less = 0
        length_more = 0
        sum_more = 0
        try:
            nums = list(map(int, input().split()))
            for num in nums:
                if num >= 0:
                    sum_more += num
                    length_more += 1
                else:
                    length_less += 1
            advance = sum_more / length_more
            print(length_less)
            print(round(advance, 1))
        except:
            break


if __name__ == '__main__':
    get_advance_num()
