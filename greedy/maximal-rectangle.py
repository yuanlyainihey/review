# C++
# 题目描述
# 给出一个只包含0和1的二维矩阵，找出最大的全部元素都是1的长方形区域，返回该区域的面积。
# class Solution {
# public:
#     int maximalRectangle(vector<vector<char> > &matrix) {
#         int row=matrix.size();
#         if(row==0) return 0;
#         int column=matrix[0].size();
#         if(column==0) return 0;
#         vector<int> height(column,0);
#         int result=0;
#         for(int i=0;i<row;++i){
#             for(int j=0;j<column;++j){
#                 if(matrix[i][j]=='1'){
#                     height[j]++;
#                 }else{
#                     height[j]=0;
#                 }
#             }
#             int area=largestRectangleArea(height);
#             result=area>=result?area:result;
#         }
#         return result;
#     }
#     int largestRectangleArea(vector<int> &height) {
#         int max=0;
#         stack<int> sta;
#         for(int i=0;i<height.size();++i){
#             if(sta.empty()){
#                 sta.push(i);
#                 continue;
#             }
#             while(!sta.empty()&&height[i]<=height[sta.top()]){
#                 int j=sta.top();
#                 sta.pop();
#                 int k=sta.empty()==true?-1:sta.top();
#                 int area=(i-k-1)*height[j];
#                 max=area>=max?area:max;
#             }
#             sta.push(i);
#         }
#         int i=height.size();
#         while(!sta.empty()){
#             int j=sta.top();
#             sta.pop();
#             int k=sta.empty()==true?-1:sta.top();
#             int area=(i-k-1)*height[j];
#             max=area>=max?area:max;
#         }
#         return max;
#     }
# };