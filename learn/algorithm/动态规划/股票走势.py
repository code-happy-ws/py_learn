"""根据股票走势寻找最大利润"""

def max_profit(datas):
    """动态规划
    关键:
        max_profit保存此刻为止的最大利润
    """
    if not datas:
        return None
    min_data=datas[0]
    max_profit=datas[0]
    for i in range(1,len(datas)):
        max_profit=max(max_profit,datas[i]-min_data)
        min_data=min(min_data,datas[i])
    print(max_profit)


if __name__ == '__main__':
    data = [1, 6, 3, 7, 5, 1, 4, 9]
    max_profit(data)


