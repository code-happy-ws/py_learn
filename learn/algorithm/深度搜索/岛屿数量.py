"""给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
"""


class Solution:

    def numIslands(self, grid) -> int:
        def dfs(grid, r, c):
            nonlocal row_nums
            nonlocal column_nums
            grid[r][c] = 0
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < row_nums and 0 <= y < column_nums and grid[x][y] == '1':
                    dfs(grid, x, y)

        row_nums = len(grid)
        if row_nums == 0:
            return 0
        column_nums = len(grid[0])
        count = 0
        for row in range(row_nums):
            for column in range(column_nums):
                if grid[row][column] == '1':
                    count += 1
                    dfs(grid, row, column)
        return count

    def numIslands2(self, grid) -> int:

        def dfs(grid, state):
            nonlocal row_nums
            nonlocal column_nums
            grid[state[0]][state[1]] = 0
            for x, y in [(state[0] - 1, state[1]), (state[0] + 1, state[1]),
                         (state[0], state[1] - 1), (state[0], state[1] + 1)]:
                if 0 <= x < row_nums and 0 <= y < column_nums and grid[x][y] == '1':
                    dfs(grid, (x, y))

        row_nums = len(grid)
        if row_nums == 0:
            return 0
        column_nums = len(grid[0])
        count = 0
        for row in range(row_nums):
            for column in range(column_nums):
                if grid[row][column] == '1':
                    count += 1
                    state = (row, column)
                    dfs(grid, state)
        return count
