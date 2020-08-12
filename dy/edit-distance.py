# 题目描述 - minDistance
# 给定两个单词word1和word2，请计算将word1转换为word2至少需要多少步操作。
# 你可以对一个单词执行以下3种操作：
# a）在单词中插入一个字符
# b）删除单词中的一个字符
# c）替换单词中的一个字符
class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = i
        for i in range(m+1):
            dp[i][0] = i
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1] ,dp[i-1][j])+1
        return dp[-1][-1]