# 题目描述
# 分发饼干，每个孩子最多只能给一块饼干。
# 对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。
# 如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
# 你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

def findContentChildren(g, s):
    g.sort()
    s.sort()
    child = 0
    cookies = 0
    while child < len(g) and cookies < len(s):
        if g[child] <= s[cookies]:
            child += 1
        cookies += 1
    return child