// for(int i =0;i<N;i++){
//   cin >> v.at(i);
// }
// single line with multi param
// vector of vector
//   vector<vector<int>> data(row,vector<int>(col));
//for(int row=0;row<N;row++){
//    for(int col=0;col<N;col++){
//  }}
#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> a(N);
  vector<int> b(N);
  vector<int> c(N);
  for(int i =0;i<N;i++){
    cin >> a.at(i);
    cin >> b.at(i);
    cin >> c.at(i);
  }
  vector<vector<int>> dp(3,vector<int>(N+1,INT_MIN));
  dp[0][0]=0;
  dp[1][0]=0;
  dp[2][0]=0;
  for(int i=0;i<N;i++){
    dp[0][i+1]=max(dp[1][i]+b[i],dp[2][i]+c[i]);
    dp[1][i+1]=max(dp[0][i]+a[i],dp[2][i]+c[i]);
    dp[2][i+1]=max(dp[0][i]+a[i],dp[1][i]+b[i]);
  }
  cout << max(dp[0][N],max(dp[1][N],dp[2][N])) <<endl;
}
