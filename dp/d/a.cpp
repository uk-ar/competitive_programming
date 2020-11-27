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
  long long N,W;
  cin >> N >> W;
  vector<int> w(N);
  vector<int> v(N);
  for(int i =0;i<N;i++){
    cin >> w.at(i);
    cin >> v.at(i);
  }
  vector<vector<long long>>dp(N+1,vector<long long>(W+1,INT_MIN));
  dp[0][0]=0;
  for(int i=0;i<N;i++){
    for(int j=0;j<=W;j++){
      if(j-w[i]>=0){
        dp[i+1][j]=max(dp[i][j],dp[i][j-w[i]]+v[i]);
        //cout << i << ":" << j << ":" << dp[i+1][j] << endl;
      }else{
        //dp[i+1][j]=max(dp[i][j],dp[i+1][j]);
        dp[i+1][j]=dp[i][j];
      }
    }
  }
  cout << *max_element(dp[N].begin(),dp[N].end()) << endl;
}
