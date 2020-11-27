// int N,M;cin >> N >> M;
// vector<int> v(N);
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
  vector<int> v(N);
  for(int i =0;i<N;i++){
    cin >> v.at(i);
  }
  vector<int> dp(N,INT_MAX);
  dp[0]=0;
  for(int i=0;i<N;i++){
    if(i+1 < N){
      dp[i+1]=min(dp[i+1],dp[i]+abs(v[i]-v[i+1]));
    }
    if(i+2 < N){
      dp[i+2]=min(dp[i+2],dp[i]+abs(v[i]-v[i+2]));
    }
  }
  cout << dp[N-1] <<endl;
}
