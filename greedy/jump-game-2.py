# 题目描述
# 给出一个非负整数数组，你最初在数组第一个元素的位置
# 数组中的元素代表你在这个位置可以跳跃的最大长度
# 你的目标是用最少的跳跃次数来到达数组的最后一个元素的位置
class Solution:
    def jump(self, A):
        # write code here
        if len(A) <= 1:
            return 0
        max_da = min(A[0], len(A) - 1)
        index = 0
        count = 1
        while max_da < len(A) - 1:
            for i in range(index + 1, max_da + 1):
                if [i] + i > max_da:
                    index = i
                    max_da = A[i] + i
            count += 1
        return count
