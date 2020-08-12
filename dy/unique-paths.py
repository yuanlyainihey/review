# 题目描述
# 一个机器人在m×n大小的地图的左上角（起点，下图中的标记“start"的位置）。
# 机器人每次向下或向右移动。机器人要到达地图的右下角。（终点，下图中的标记“Finish"的位置）。
# 可以有多少种不同的路径从起点走到终点？
class Solution:
    def uniquePaths(self, m, n):
        res = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                res[j] = res[j-1] + res[j]
        return res[-1]