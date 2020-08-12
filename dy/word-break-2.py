# 题目描述 - word-break-2
# 给定一个字符串s和一组单词dict，在s中添加空格将s变成一个句子，使得句子中的每一个单词都是dict中的单词
# 返回所有可能的结果
# C++
# class Solution {
# public:
#     vector<string> wordBreak(string s, unordered_set<string> &dict) {
#         int len=s.length();
#         dp =new vector<bool>[len];
#         for(int pos=0;pos<len;pos++){
#             for(int i=1;i<len-pos+1;i++){
#                 if(dict.find(s.substr(pos,i))!=dict.end())
#                     dp[pos].push_back(true);
#                 else
#                     dp[pos].push_back(false);
#             }
#         }
#         dfs(s,len-1);
#         return res;
#     }
#     void dfs(string s, int n){
#         if(n>=0){
#             for(int i=n;i>=0;i--){
#                 if(dp[i][n-i]){
#                     mid.push_back(s.substr(i,n-i+1));
#                     dfs(s,i-1);
#                     mid.pop_back();
#                 }
#             }
#         }
#         else{
#             string r;
#             for(int j=mid.size()-1;j>=0;j--){
#                 r+=mid[j];
#                 if(j>0)
#                     r+=" ";
#             }
#             res.push_back(r);
#         }
#     }
#     vector<bool> *dp;
#     vector<string> res;
#     vector<string> mid;
# };