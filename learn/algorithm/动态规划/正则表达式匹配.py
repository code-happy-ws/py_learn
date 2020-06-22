import functools


def match_easy(text, pattern):
    """  . 匹配单个字符"""
    if not pattern:
        return not text
    now_match = bool(text) and pattern[0] in {text[0], '.'}
    return now_match and match_easy(text[1:], pattern[1:])


@functools.lru_cache()
def match_hard(text, pattern):
    """ . 匹配单个字符，*匹配零或多个字符
    思路： 回溯法
    要点：
        返回：模式匹配完后，若有剩余字符串则匹配失败，若字符串为空，则匹配成功‘
        """
    if not pattern:
        return not text
    now_match = bool(text) and pattern[0] in {text[0], '.'}

    # pattern第二个为*，分为0个和多个两种情况讨论，满足其一即可
    if len(pattern) >= 2 and pattern[1] == '*':
        return match_hard(text, pattern[2:]) or \
               (now_match and match_hard(text[1:], pattern))

    # pattern第二个不为*
    else:
        return now_match and match_hard(text[1:], pattern[1:])


def match_dp(text, pattern):
    """ . 匹配单个字符，*匹配零或多个字符
    思路： 动态规划
    状态转移方程：
    f[i][j]表示text的前i个字符和pattern的前j个字符匹配；
    if pattern[j]!='*':
        f[i][j]=f[i-1][j-1] if match(text[i],pattern[j]) else False
    else:
    # 字母带*号时，本质上有两种情况（将字母带*号视为一个组合处理）：
        1.能匹配字符串末尾一个字符，则将该字符扔掉，模式组合能继续匹配；
        2.不能匹配字符串末尾一个字符，则将该模式组合扔掉，剩余模式组合能继续匹配
        f[i][j]=(f[i-1][j] or f[i][j-2]) if match(text[i],pattern[j-1]) else f[i][j-2]
    """
    m, n = len(text), len(pattern)

    def match(i, j):
        """ 判断字符串的第i个字符是否能同pattern第j个字符匹配；
        注：参数上的i或j表示第i或j个字符，该字符对应text[i-1]或pattern[j - 1];
        同f[i][j]中i j 的含义一致"""
        if i == 0:
            return False
        if pattern[j - 1] == '.':
            return True
        return text[i - 1] == pattern[j - 1]

    f = [[0] * (n + 1) for _ in range(m + 1)]

    f[0][0] = 1
    for i in range(m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == '*':
                if match(i, j - 1):
                    f[i][j] = f[i - 1][j] or f[i][j - 2]
                else:
                    f[i][j] = f[i][j - 2]
            else:
                if match(i, j):
                    f[i][j] = f[i - 1][j - 1]
    return bool(f[m][n])


if __name__ == '__main__':
    print(match_easy('heffo', 'he..o'))
    print(match_hard('h', 'ho*'))
    print(match_dp('bccd', 'b.*d'))
