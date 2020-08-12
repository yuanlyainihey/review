# 题目描述
# 请计算给出的数组（至少含有一个数字）中具有最大和的子数组（子数组要求在原数组中连续）

class Solution:
    def maxSubArray(self, A):
        # write code here
        if A is None:
            print(0)

        m_sum = A[0]
        max_sum = A[0]
        for n in A[1:]:
            if m_sum < 0:
                m_sum = n
            else:
                m_sum += n
            max_sum = max(m_sum, max_sum)

        return max_sum