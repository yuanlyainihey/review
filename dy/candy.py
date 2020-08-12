# 题目描述 - candy
# 有N个小朋友站在一排，每个小朋友都有一个评分
# 你现在要按以下的规则给孩子们分糖果：每个小朋友至少要分得一颗糖果,分数高的小朋友要他比旁边得分低的小朋友分得的糖果多
# 你最少要分发多少颗糖果？
class Solution:
    def candy(self, ratings):
        # write code here
        if not ratings:
            return 0
        dp = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                dp[i] = dp[i-1] + 1
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j+1] and dp[j] <= dp[j+1]:
                dp[j] = dp[j+1] + 1
        return sum(dp)