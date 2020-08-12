# 题目描述 - decode-ways
# 字母加密有多少种解法
class Solution:
    def numDecodings(self, s):
        n = int(len(s))
        if n == 0 or s == '0':
            return 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if s[i] != '0':
                dp[i] = dp[i-1]
            if i == 1 and s[0] + s[1] <= '26':
                dp[i] += dp[i-1]
            if i >= 2 and '26' >= s[i - 1] + s[i] >= '10':
                dp[i] += dp[i - 2]
        return dp[-1]