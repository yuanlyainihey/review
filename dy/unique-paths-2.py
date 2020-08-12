# 题目描述 - unique-paths-2
# 继续思考题目"Unique Paths":
# 如果在图中加入了一些障碍，有多少不同的路径？
# 分别用0和1代表空区域和障碍
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1 and n == 1:
            if obstacleGrid[0][0] == 1:
                return 0
            else:
                return 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        for j in range(m):
            if obstacleGrid[j][0] == 0:
                dp[j][0] = 1
            else:
                break

        for k in range(1, m):
            for q in range(1, n):
                if obstacleGrid[k][q] == 0:
                    dp[k][q] = dp[k - 1][q] + dp[k][q - 1]
        return dp[-1][-1]