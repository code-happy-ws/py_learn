def isPopOrder(pushes, pops):
    """两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序"""
    if not pushes or not pops or len(pushes) != len(pops):
        return False
    while pops:
        # print( pushes.pop(0), pops.pop(-1))
        if pushes.pop(0)!=pops.pop(-1):
            return False
    if not pushes:
        return True

if __name__ == '__main__':

    # test
    pops = [4, 3, 2, 1]
    pushes = [1, 2, 3, 4, 5]
    print(isPopOrder(pushes, pops))
    # print(isPopOrder2(pushes, pops))
    # print(pop_order(pushes, pops))