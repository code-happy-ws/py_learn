"""有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 
这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，
气球 left 和气球 right 就变成了相邻的气球。求所能获得硬币的最大数量。
说明:
你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100"""
class Solution:
    """动态规划：
    思路：
        关键点：
            刻画最优解结构；
            动态规划主要可以避免重复计算子问题，最优解结构要体现出这种
            避免重叠子问题重复计算功能；戳气球重叠子问题为可能会反复计算从索引m到n之间的最大值，
            故需用动态表格存储该子问题最优解，避免重复计算；
        状态：由以上分析知，重叠子问题状态表示为在俩索引位置之间戳气球最大值，故可用dp[start][end]表示
        索引start到end之间戳气球（不包含start和end）最大值;
        状态转移方程(用某问题的子问题状态表示该问题的状态)：
            举例子：
                对于[3,1,4,8],可表示为求nums=[1,2,1,4,8,1]里的dp[0][5],若先戳第i个位置气球，分成左右两部分
                dp[start][i]、dp[i][end],但是气球移动后端点会变化，因此无法继续分析，需要换个思路：为了避免端点移动导致分析困难，
                设最后戳第k个气球，这样 dp[0][5]可表示为:
                dp[0][5]=max{d[0][k]+d[i][5]+nums[start]*nums[k]*nums[end] for k in (start,end)}
           一般化：
                dp[satrt][end]=max{dp[start][k]+d[k][end]+nums[start]*nums[k]*nums[end] for k in (start+1,end)}
        步骤：
            1.构造最优解结构，如上分析；
            2.递归定义最优解值；
            3.计算最优解的值，通常采用自底向上法；
        个人卡点：第41行不认真，nums未写成all_nums!!    """
    def __init__(self):
        pass

    def maxCoins(self, nums) -> int:
        all_nums = [1]+nums+[1]
        length = len(all_nums)
        dp=[[0]*length for _ in range(length)]
        for e in range(2,len(all_nums)):
            for s in reversed(range(e-1)):
                # for k in range(s+1, e):
                    # dp[s][e]=max(dp[s][e],dp[s][k]+dp[k][e]+all_nums[s]*all_nums[k]*all_nums[e])
                # 注释等同于下面一行
                dp[s][e] = max(dp[s][k] + dp[k][e] + all_nums[s] * all_nums[k] * all_nums[e] for k in range(s+1, e))
        return dp[0][length-1]

S=Solution()
nums=[3,1,5,8]
print(S.maxCoins(nums=nums))
