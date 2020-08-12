# 题目描述 - climbStairs
# 你在爬楼梯，需要n步才能爬到楼梯顶部
# 每次你只能向上爬1步或者2步。有多少种方法可以爬到楼梯顶部？
class Solution:
    def climbStairs(self, n):
        DP = [0 for _ in range(0, n)]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            DP[0] = 1
            DP[1] = 2
            for i in range(2, n):
                DP[i] = DP[i-1] + DP[i-2]
            return DP[-1]