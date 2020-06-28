import math


def is_zhishu(num):
    """为质数返回True,否则返回false"""
    flag = True
    if num <= 2:
        flag = False
    else:
        # for i in range(3,num//2+1,2):
        for i in range(3, int(math.sqrt(num) + 1), 2):
            if num % i == 0:
                flag = False
                break
    return flag


def count_of_sum(num):
    try:
        count = 0
        # num=int(input())
        if num == 0:
            print('end')
        if num == 1:
            print(0)
        else:
            for i in range(1, num // 2 + 1, 2):
                if is_zhishu(i) and is_zhishu(num - i):
                    count += 1
            print(count)
    except:
        pass



def count_primes_py(n):
    """
    求n以内的所有质数个数（纯python代码）
    """
    # 最小的质数是 2
    if n < 2:
        return 0

    isPrime = [1] * n
    isPrime[0] = isPrime[1] = 0   # 0和1不是质数，先排除掉

    # 埃式筛，把不大于根号n的所有质数的倍数剔除
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

    return sum(isPrime)

if __name__ == '__main__':
    import time

    start = time.time()
    # 10000--127--0.328s
    # 100000--810--24s  16s  11s
    # print(count_primes_py(100000))
    count_of_sum(100000)
    # print(is_zhishu(10000000000))
    end = time.time()
    print('time:', end - start)
