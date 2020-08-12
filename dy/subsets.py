# 题目描述 - subsets
# 现在有一个没有重复元素的整数集合S，求S的所有子集
class Solution:
    def subsets(self, A):
        # write code here
        n = len(A)
        test_marks = [1 << i for i in range(len(A))]
        res = []
        for k in range(2**n):
            l = []
            for idx, mark in enumerate(test_marks):
                if mark & k:
                    l.append(A[idx])
            res.append(l)
        return res