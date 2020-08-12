class Solution:
    def grayCode(self, n):
        res = [0]
        m = 1
        for i in range(n):
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] + m)
            m *= 2
        return res