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
  for(int i =0;i<N;i++){
    cin >> a.at(i);
  }
  int s = accumulate(a.begin(),a.end(),0);
  vector<vector<int>> dp(N+1,vector<int>(s+1,0));
  dp[0][0]=1;
  for(int i=0;i<N;i++){
    for(int j=0;j<=s;j++){
      dp[i+1][j]=dp[i][j];
      if(0<=j-a[i]){
        dp[i+1][j]=max(dp[i+1][j],dp[i][j-a[i]]);
      }
    }
  }
  cout << accumulate(dp[N].begin(),dp[N].end(),0) << endl;
}
