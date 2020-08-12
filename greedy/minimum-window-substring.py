# 题目描述
# 给出两个字符串S和T，要求在O（n）的时间复杂度内在S中找出最短的包含T中所有字符的子串。
class Solution:
    def minWindow(self, S, T):
        # write code here
        c, l = 0, 0
        res = ""
        min_l = len(S) + 1
        d = {}
        for i in T:
            d[i] = d.get(i, 0) + 1

        for r in range(len(S)):
            if S[r] in T:
                if d[S[r]] > 0:
                    c += 1
                d[S[r]] -= 1
            while c == len(T):
                if S[l] in T:
                    if min_l > r - l + 1:
                        min_l = r - l + 1
                        res = S[l:r + 1]
                    d[S[l]] += 1
                    if d[S[l]] > 0:
                        c -= 1
                l += 1
        return res