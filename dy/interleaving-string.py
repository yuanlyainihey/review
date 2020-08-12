# 题目描述 - interleaving-string
# 给出三个字符串s1, s2, s3,判断s3是否可以由s1和s2交织而成。
class Solution:
    def isInterleave(self, s1, s2, s3):
        m, n, s = len(s1), len(s2), len(s3)
        if m+n != s:
            return False
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(m+1):
            for j in range(n+1):
                point = i+j-1
                if i == 0 and j > 0:
                    dp[j] = dp[j-1] and s3[point] == s2[j-1]
                if j == 0 and i > 0:
                    dp[j] = dp[j] and s3[point] == s1[i-1]
                if j > 0 and i > 0:
                    dp[j] = (dp[j] and s3[point] == s1[i-1]) or (dp[j-1] and s3[point] == s2[j-1])
        return dp[-1]