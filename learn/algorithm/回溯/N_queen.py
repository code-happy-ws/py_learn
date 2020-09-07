"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
即：两皇后不能同时出现同一行、同一列、同一左斜线、同一右斜线;
输入：4
输出：[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

思路：回溯法
"""


def solve_queen(n):
    def generate_board():
        """按照queens结果生成一个解"""
        board = list()
        for i in range(n):
            row[queens[i]] = 'Q'
            board.append(''.join(row))
            row[queens[i]] = '.'
        return board

    def backtrack(row):
        # row表示本次处理的目标行数值（需保证当前要放皇后的位置所在列、左斜线、右斜线均无皇后）
        if row == n:
            # 表示一次尝试已结束，生成本次位置结果并存放至列表
            board = generate_board()
            solutions.append(board)
        else:
            for i in range(n):
                # i表示当前要放的位置column值，需先判断当前所在列、左斜线、右斜线是否已有皇后
                # （无需考虑同一行，因为每次回溯有row+1，不可能同行，queens[row]中的row表示当前行）
                if i in columns or row - i in diagonal1 or row + i in diagonal2:
                    continue
                queens[row] = i
                columns.add(i)
                diagonal1.add(row - i)
                diagonal2.add(row + i)
                backtrack(row + 1)
                columns.remove(i)
                diagonal1.remove(row - i)
                diagonal2.remove(row + i)

    solutions = list()

    # 下标表示row数，值表示皇后所在column值
    queens = [-1] * n

    # 保存已占用列值，表示该列已有皇后
    columns = set()

    # 保存已占用的左向下斜线特征值，表示该斜线已有皇后 （按照第四象限坐标轴，column-row值相等表示在同一斜线上）
    diagonal1 = set()

    # 保存已占用的右斜线特征值，表示该斜线已有皇后 （按照第四象限坐标轴，column+row值相等表示在同一斜线上）
    diagonal2 = set()

    # 一行的内容（.表示空位，Q表示皇后）
    row = ['.'] * n
    backtrack(0)
    return solutions


if __name__ == '__main__':
    print(solve_queen(4))

#
#
# class Solution:
#     def solveNQueens(self, n: int):
#         def generateBoard():
#             board = list()
#             for i in range(n):
#                 row[queens[i]] = "Q"
#                 board.append("".join(row))
#                 row[queens[i]] = "."
#             return board
#
#         def backtrack(row: int):
#             if row == n:
#                 board = generateBoard()
#                 solutions.append(board)
#             else:
#                 for i in range(n):
#                     if i in columns or row - i in diagonal1 or row + i in diagonal2:
#                         continue
#                     queens[row] = i
#                     columns.add(i)
#                     diagonal1.add(row - i)
#                     diagonal2.add(row + i)
#                     backtrack(row + 1)
#                     columns.remove(i)
#                     diagonal1.remove(row - i)
#                     diagonal2.remove(row + i)
#
#         solutions = list()
#         queens = [-1] * n
#         columns = set()
#         diagonal1 = set()
#         diagonal2 = set()
#         row = ["."] * n
#         backtrack(0)
#         return solutions
