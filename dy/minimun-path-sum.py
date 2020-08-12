# 题目描述 - minPathSum
# 给定一个由非负整数填充的m x n的二维数组，现在要从二维数组的左上角走到右下角，请找出路径上的所有数字之和最小的路径。
# 注意：你每次只能向下或向右移动。
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        flag = [[0 for _ in range(n)] for _ in range(m)]
        flag[0][0] = grid[0][0]
        for i in range(1, n):
            flag[0][i] = flag[0][i-1] + grid[0][i]
        for i in range(1, m):
            flag[i][0] = flag[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                flag[i][j] = min(flag[i-1][j], flag[i][j-1]) + grid[i][j]
        return flag[m-1][n-1]