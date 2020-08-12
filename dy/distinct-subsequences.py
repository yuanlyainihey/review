# 题目描述 - distinct-subsequences
# 给定两个字符串S和T，返回S子序列等于T的不同子序列个数有多少个？
# 字符串的子序列是由原来的字符串删除一些字符（也可以不删除）在不改变相对位置的情况下的剩余字符（例如，"ACE"is a subsequence of"ABCDE"但是"AEC"不是）
class Solution:
    def numDistinct(self, S, T):
        # write code here
        m, n = len(S), len(T)
        if m == 0 or n == 0:
            return 0

        # f[i][j]表示T[0-j]在S[0-i]中出现的次数
        f = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            f[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if S[i - 1] == T[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j]
        return f[-1][-1]