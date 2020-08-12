# 题目描述 - subsets-2
# 给出一个可能包含重复元素的整数集合S，返回该整数集合的所有子集。
# C++
# class Solution {
#     public:
#         vector<vector<int>> res;
#         vector<int> tmp;
#         vector<vector<int> > subsetsWithDup(vector<int> &S) {
#             res.push_back(tmp);
#             sort(S.begin(),S.end());
#             dp(0,1,S);
#             return res;
#         }
#     void dp(int start,int n,vector<int> &S){
#         if(tmp.size()==n){
#             res.push_back(tmp);
#             if(n<S.size()) dp(start,n+1,S);
#             else
#                 return ;
#         }
#         for(int i=start;i<S.size();){
#             tmp.push_back(S[i]);
#             dp(i+1,n,S);
#             int j(i);
#             while(j<S.size()&&S[j]==S[i]) ++j;
#             i=j;
#             tmp.pop_back();
#         }
#     }
# };