"""给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度"""
m = """
{} None -1
{'t': 0} None -1
{'t': 0, 'm': 1} 1 -1
{'t': 0, 'm': 2} None 1
{'t': 0, 'm': 2, 'z': 3} None 1
{'t': 0, 'm': 2, 'z': 3, 'u': 4} None 1
{'t': 0, 'm': 2, 'z': 3, 'u': 4, 'x': 5} 0 1
"""
n = """
{} None -1
{'t': 0} None -1
{'t': 0, 'm': 1} 1 -1
{'t': 0, 'm': 2} None 1
{'t': 0, 'm': 2, 'z': 3} None 1
{'t': 0, 'm': 2, 'z': 3, 'u': 4} None 1
{'t': 0, 'm': 2, 'z': 3, 'u': 4, 'x': 5} 0 1
"""


def lengthOfLongestSubstring(s: str) -> int:
    start, res, letter_dict = -1, 0, {}
    for i, letter in enumerate(s):
        # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
        print(letter_dict, letter, start)
        if letter in letter_dict and letter_dict.get(letter) > start:
            start = letter_dict[letter]
            letter_dict[letter] = i
        else:
            print('---------')
            print(res, i, start)
            letter_dict[letter] = i
            res = max(res, i - start)
    return res


if __name__ == '__main__':
    print(lengthOfLongestSubstring("tmmzuxt"))
