"""获得从左上角到右下角最小路径和
输入：(非负整数)
    [[1,2,3],
     [4,5,6],
     [7,8,9]]

输出：7"""
def get_min_path(grid):
    """思路：动态规划(时间复杂度O（row*column）)
    min_sum[i][j] = min(min_sum[i-1][j]+grid[i][g],min_sum[i][j-1]+grid[i][g])
    要点：细心，处理特殊情况
    空间优化：使用原空间grid
    """

    if not grid:
        return 0
    all_row = len(grid)
    all_column = len(grid[0])
    for row in range(1, all_row):
        grid[row][0] = grid[row-1][0] + grid[row][0]
    for column in range(1, all_column):
        grid[0][column] = grid[0][column-1] + grid[0][column]

    for row in range(1, all_row):
        for column in range(1, all_column):
            grid[row][column] = min(grid[row-1][column]+grid[row][column],
                                    grid[row][column-1]+grid[row][column])
    return grid[all_row-1][all_column-1]

def get_min_path0(grid):
    """思路：动态规划(时间复杂度O（row*column）)
    min_sum[i][j] = min(min_sum[i-1][j]+grid[i][g],min_sum[i][j-1]+grid[i][g])
    要点：细心，处理特殊情况
    空间优化：使用原空间grid
    """

    if not grid:
        return 0
    all_row = len(grid)
    all_column = len(grid[0])
    min_sum = [[0]*all_column for _ in range(all_row)]
    min_sum[0][0] = grid[0][0]
    for row in range(1, all_row):
        min_sum[row][0] = min_sum[row-1][0] + grid[row][0]
    for column in range(1, all_column):
        min_sum[0][column] = min_sum[0][column-1] + grid[0][column]

    for row in range(1, all_row):
        for column in range(1, all_column):
            min_sum[row][column] = min(min_sum[row-1][column]+grid[row][column],
                                       min_sum[row][column-1]+grid[row][column])
    return min_sum[all_row-1][all_column-1]



def get_min_path1(grid):
    """思路1：DFS 遍历所有路径，时间复杂度过大,估计O(2^n)
    """
    all_row = len(grid)
    all_column = len(grid[0])
    result = []
    all_path = []

    def dfs(row, column, sum, path):
        sum += grid[row][column]
        path.append(grid[row][column])
        if row < all_row - 1:
            dfs(row + 1, column, sum, path)
            path.pop()
        if column < all_column - 1:
            dfs(row, column + 1, sum, path)
            path.pop()
        if row == all_row - 1 and column == all_column - 1:
            result.append(sum)
            # 注意：一定要保持path副本，否则path.pop()会影响all_path
            all_path.append(path[:])
            return

    dfs(0, 0, 0, [])
    return min(result)


if __name__ == '__main__':
    grid = [[1, 2, 3]]
    # result = get_min_path1(grid)
    # print(result)

    result0 = get_min_path(grid)
    print(result0)
