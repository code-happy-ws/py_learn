""" 横竖比自己大的数量
输入：[[10,25,20],[30,20,10]]
输出：[[3,0,1],[0,2,3]]
思路：排序累加，先处理所有行，在处理所有列，汇总两结果
教训：将可能的算法列出来，一个一个对比，看适合用哪个，正确分析时间复杂度后在下手
可能算法：排序、二分、窗口、指针、dfs、bfs、动态规划、贪心、图等
可能数据结构：栈、队列、集合等
"""
from copy import deepcopy


def get_more(grid):
    # 不建议直接切片复制，若元素可变，会同变
    result_row = deepcopy(grid)
    result_column = deepcopy(grid)
    result = deepcopy(grid)
    rows = len(grid)
    columns = len(grid[0])
    rows_info = []
    for i in range(rows):
        row_info = []
        for j in range(columns):
            row_info.append([(i, j), grid[i][j]])
        rows_info.append(row_info)

    for row in rows_info:
        sort_row = sorted(row, key=lambda x: x[1])
        row_values = [v[1] for v in row]
        more_rows = more(row_values)
        for index, info in enumerate(sort_row):
            pos = info[0]
            result_row[pos[0]][pos[1]] = more_rows[index]
    columns_info = []

    for j in range(columns):
        column_info = []
        for i in range(rows):
            column_info.append([(i, j), grid[i][j]])
        columns_info.append(column_info)

    for column in columns_info:
        sort_column = sorted(column, key=lambda x: x[1])
        values = [v[1] for v in column]
        more_nums = more(values)
        for index, info in enumerate(sort_column):
            pos = info[0]
            result_column[pos[0]][pos[1]] = more_nums[index]

    for i in range(rows):
        for j in range(columns):
            result[i][j] = result_row[i][j] + result_column[i][j]
    return result


def more(nums):
    end = len(nums) - 1
    more_nums = [None] * len(nums)
    fast = 0
    for pos, num in enumerate(nums):
        if pos == fast:
            fast = pos + 1
            now_more_num = end - pos
            while fast <= end and nums[fast] == nums[pos]:
                now_more_num -= 1
                fast += 1
            if fast - pos > 1:
                more_nums[pos:fast] = [now_more_num] * (fast - pos)
                more_nums[:pos] = [n - 1 for n in more_nums[:pos]]
            else:
                more_nums[pos] = now_more_num
    return more_nums


if __name__ == '__main__':
    # a = [1, 2, 3, 3, 4, 5, 5]
    # print(more(a))
    b = [[10, 25, 20], [30, 20, 10]]
    get_more(b)
