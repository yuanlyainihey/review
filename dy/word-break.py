# 题目描述 - word-break
# 给定一个字符串s和一组单词dict，判断s是否可以用空格分割成一个单词序列，使得单词序列中所有的单词都是dict中的单词（序列可以包含一个或多个单词）。

# C++
#  class Solution {
# public:
#     bool wordBreak(string s, unordered_set<string> &dict) {
#         int len = s.length();
#         if (len == 0)
#             return false;
#         int dp[len]; memset(dp, 0, sizeof(dp));
#         if (dict.find(s.substr(0,1)) != dict.end())
#             dp[0] = 1;
#         for(int i=1; i<len; i++) {
#             for(int j=0; j<=i; j++) {
#                 string y = s.substr(j, i-j+1);
#                 if ( (j==0 && dict.find(y) != dict.end())
#                      ) {
#                     dp[i] = 1;
#                     break;
#                 } else if (dp[j-1] && dict.find(y) != dict.end()) {
#                     dp[i] = 1;
#                     break;
#                 }
#             }
#         }
#         return dp[len-1]==1;
#     }
# };