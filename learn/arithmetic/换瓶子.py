"""
有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”
答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，
这时候剩2个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。
如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？
输入示例：
3
10
81
0
输出：
1
5
40

总结：
    1.作异常处理
    2.分析前几个元素规律，可取巧
"""
def max_num():
    """方法1：递归处理"""
    while True:
        """注意作异常处理"""
        try:
            data=int(input())
            if data==0:
                break
            bottle=0
            while True:
                get_bottle,last_bottle=divmod(data,3)
                bottle=bottle+get_bottle

                data=get_bottle+last_bottle
                if get_bottle==1:
                    if last_bottle==0:
                        print(bottle)
                        break
                if get_bottle==0:
                    if last_bottle==1:
                        print(bottle)
                        break
                    elif last_bottle==2:
                        bottle+=1
                        print(bottle)
                        break
        except:
            break

while True:
    """方法2：取巧；每两个瓶子可换一个"""
    try:
        a = int(input())
        if a != 0:
            print(a // 2)
    except:
        break
if __name__ == '__main__':
    max_num()




