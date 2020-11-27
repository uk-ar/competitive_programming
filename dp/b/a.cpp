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
  int N,K;
  cin >> N >> K;
  vector<int> a(N);
  for(int i =0;i<N;i++){
    cin >> a.at(i);
  }
  vector<int>dp(N+1,INT_MAX);
  dp[0]=0;
  for(int i=0;i<N;i++){
    for(int j=i+1;j<=min(N,i+K);j++){
      //cout << dp[j]<< ":" << dp[i] << ":" << a[i] << a[j] << endl;
      dp[j]=min(dp[j],dp[i]+abs(a[i]-a[j]));
    }
    //cout << dp[i] << endl;
  }
  cout << dp[N-1] << endl;
}
