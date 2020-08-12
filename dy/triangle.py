# C++
# class Solution {
# public:
#     int minimumTotal(vector<vector<int> > &triangle) {
#         int sum;
#         sum = getres(triangle,0,0);
#         return sum;
#     }
#     int getres(vector<vector<int> > &triangle,int l,int k)
#         {
#         int sum = triangle[l][k];
#         if(l<triangle.size() -1 )
#             sum = sum + min(getres(triangle,l+1,k),getres(triangle,l+1,k+1));
#         return sum;
#     }
# };