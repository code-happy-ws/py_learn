"""请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。"""

def dailyTemperatures(T):
    """单调栈"""
    length = len(T)
    stack = []
    for i in range(length):
        temperature = T[i]
        while stack and temperature > T[stack[-1]]:
            prev_index = stack.pop()
            T[prev_index] = i - prev_index
        stack.append(i)
    for pos in stack:
        T[pos]=0
    return T

def dailyTemperatures1(T):
    """优化空间"""
    length = len(T)
    stack = []
    for i in range(length):
        temperature = T[i]
        while stack and temperature > T[stack[-1]]:
            prev_index = stack.pop()
            T[prev_index] = i - prev_index
        stack.append(i)
    for pos in stack:
        T[pos]=0
    return T

def dailyTemperatures2(T):
    """KMP:该思路由KMP中失配数组的构造演变而来。
    假设ans[i]记录了i位置上的答案（向右找多少个比自己大），
    则求ans[i]时，我先看一眼i+1位置，如果T[i+1]比我大，那得了，答案就是它了。"""
    n = len(T)
    ans = [0] * n
    for i in range(n - 2, -1, -1):
        now = i + 1
        while T[now] <= T[i]:
            if ans[now]:
                now += ans[now]
            else:
                break
        else:
            ans[i] = now - i
    return ans
if __name__ == '__main__':
    T=[73, 77, 75, 79, 69, 72, 76, 73]
    # [1,1,4,2,1,1,0,0]
    print(dailyTemperatures(T))