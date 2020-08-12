# 题目描述
# 环形路上有n个加油站，第i个加油站的汽油量是gas[i].
# 你有一辆车，车的油箱可以无限装汽油。从加油站i走到下一个加油站（i+1）花费的油量是cost[i]，你从一个加油站出发，刚开始的时候油箱里面没有汽油。
# 求从哪个加油站出发可以在环形路上走一圈。返回加油站的下标，如果没有答案的话返回-1。

class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost):return -1
        cargas,ans= 0,0
        for i in range(len(gas)):
            cargas +=  gas[i]-cost[i]
            if cargas<0:
                ans = i+1
                cargas = 0
        return ans if cargas>=0 else -1