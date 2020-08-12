# 题目描述
# 给出一个非负整数数组，你最初在数组第一个元素的位置
# 数组中的元素代表你在这个位置可以跳跃的最大长度
# 判断你是否能到达数组最后一个元素的位置
class Solution:
    def canJump(self, A):
        # write code here
        if len(A) < 2:
            return True

        maxr = 0
        for i in range(len(A)):
            if maxr >= i:
                maxr = max(maxr, A[i] + i)
        if maxr >= len(A) - 1:
            return True
        else:
            return False