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
  int N,M;
  cin >> N >> M;
  vector<int>a({0});
  for(int i=0;i<N;i++){
    int t;
    cin >> t;
    a.push_back(t);
  }
  for(int i=0;i<N;i++){
    a[i+1] = a[i+1]+a[i];
  }
  vector<vector<int>>dp(M+1,vector<int>(N+1,0));
  for(int m=0;m<M;m++){
    for(int n=0;n<=N;n++){
      for(int k=0;k<n;k++){
        dp[m+1][n]=max(dp[m+1][n],dp[m][n]+(a[n]-a[k])/(n-k));
      }
      cout << dp[m+1][n] << " ";
    }
    cout << endl;
  }
  return 0;
  //cout << *max_element(dp[N].begin(),dp[N].end()) << endl;
}
