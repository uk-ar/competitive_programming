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
  long long W;
  cin >> N >> W;
  vector<int> v(N);
  vector<long long> w(N);
  for(long long i =0;i<N;i++){
    cin >> w[i] >> v[i];
  }
  long long V=100*1000;
  vector<vector<long long>>dp(N+1,vector<long long>(V+1,1e12));//min weight W9+N2+1
  dp[0][0]=0;
  for(int i=0;i<N;i++){
    for(long long j=0;j<=V;j++){
      dp[i+1][j]=dp[i][j];
      if(j-v[i]>=0 and dp[i+1][j] > dp[i][j-v[i]]+w[i]){
        dp[i+1][j]=min(dp[i+1][j],dp[i][j-v[i]]+w[i]);
        //cout << i+1 << ":" << j << ":" << dp[i+1][j] << endl;
      }
    }
  }
  int ret = 0;
  for(long long j=0;j<V+1;j++){
    if(dp[N][j]<=W){
      ret = j;
    }
  }
  cout << ret << endl;
  return 0;
  //cout << *max_element(dp[N].begin(),dp[N].end()) << endl;
}
