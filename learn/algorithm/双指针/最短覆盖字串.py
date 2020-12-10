"""给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串"""
from collections import defaultdict


class Solution:
    """双指针"""

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        need = defaultdict(int)
        # 总需要包含的字母数量
        need_num = len(t)
        for v in t:
            # t中每个字母需要的个数，其他字母为0
            need[v] += 1
        position = (0, float('inf'))
        i = 0
        for j, v in enumerate(s):
            # v在t中，需要总个数减1
            if need[v] > 0:
                need_num -= 1
            # 字母需要数量减1，若v不在t中，值变成负值
            need[v] -= 1
            # 说明当前窗口已包含全部t,且快指针刚好为边界，
            # 但是慢指针可能不是边界（为负值），需要向右移动，直至该位置的need值为0，
            if need_num == 0:
                while True:
                    # 慢指针已经到边界
                    if need[s[i]] == 0:
                        break
                    # 慢指针不是边界（为负值），需要向右移动，直至该位置的need值为0
                    need[s[i]] += 1
                    i += 1
                # 当前域的快慢指针均为边界，与历史做对比
                if j - i < position[1] - position[0]:
                    position = (i, j)

                # 慢指针向前移动一位，寻找下个可能结果域
                i += 1
                need[s[i]] += 1
                need_num += 1

        return '' if i == 0 else s[position[0]:position[1] + 1]



if __name__ == '__main__':
    s = "bbabcbaaac"
    t = "bac"

    solution = Solution()
    print(solution.minWindow(s,t))
