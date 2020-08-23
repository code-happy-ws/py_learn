"""给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串"""
from collections import defaultdict


class Solution:
    """双指针"""

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        need = defaultdict(int)
        need_num = len(t)
        for v in t:
            need[v] += 1
        position = (0, float('inf'))
        i = 0
        for j, v in enumerate(s):
            if need[v] > 0:
                need_num -= 1
            need[v] -= 1
            if need_num == 0:
                while True:
                    if need[s[i]] == 0:
                        break
                    need[s[i]] += 1
                    i += 1
                if j - i < position[1] - position[0]:
                    position = (i, j)
                need[s[i]] += 1
                i += 1
                need_num += 1
        return '' if i == 0 else s[position[0]:position[1] + 1]



if __name__ == '__main__':
    s = "bbabcbaaac"
    t = "bac"
    print(get_min_window(s, t))
    # solution = Solution()
    # print(solution.minWindow(s,t))
