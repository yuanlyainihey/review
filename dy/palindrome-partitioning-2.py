# 题目描述 - palindrome-partitioning-2
# 给出一个字符串s，分割s使得分割出的每一个子串都是回文串
# 计算将字符串s分割成回文分割结果的最小切割数
# 例如:给定字符串s="aab",
# 返回1，因为回文分割结果["aa","b"]是切割一次生成的。
class Solution:
    def minCut(self, s):
        if not s:
            return 0
        l = len(s)
        dp = [i for i in range(l)]
        check = [[False]*l for _ in range(l)]
        for i in range(l):
            for j in range(i, -1, -1):
                if s[j] == s[i] and (i-j <= 1 or check[j+1][i-1]):
                    check[j][i] = True
                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j-1]+1)
        return dp[-1]