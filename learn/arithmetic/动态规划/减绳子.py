"""把一根长为n的绳子剪成m段，并且使得每段的长度乘积最大."""

def cut(n):
    """动态规划
    思路：第一次剪断位置左右绳子均最大时乘积最大，左右绳子为子问题，即成功构造包含子问题的最优解；
    """
    max_cut=[0,1,1,2]
    if n>3:
        for i in range(4,n+1):
            max_temp=max_cut[i-1]
            for j in range(1,i//2+2):
                max_temp=max(max_cut[i-j]*max_cut[j],max_temp,(i-j)*j,max_cut[i-j]*j)
            max_cut.append(max_temp)
    print(max_cut)

if __name__ == '__main__':
    cut(10)



