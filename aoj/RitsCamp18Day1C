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
  vector<long long>a({0});
  for(int i=0;i<N;i++){
    int t;
    cin >> t;
    a.push_back(t);
  }
  for(int i=0;i<N;i++){//1-n
    a[i+1] = a[i+1]+a[i];
  }
  //cout << endl;
  vector<vector<double>>dp(M+1,vector<double>(N+1,0));
  for(int n=1;n<=N;n++){
    dp[1][n]=a[n]/(double)n;
    //0 9 10 12 15 24
    //0 9 5  4  3.75 4.8
  }
  for(int m=1;m<M;m++){
    for(int n=0;n<=N;n++){
      for(int k=0;k<n;k++){
        //k=0 max(0,dp[m][0]+(a[5]-a[0])/5)0+(24-0)/5
        //k=1 max(0,dp[m][1]+(a[5]-a[1])/4)0+(24-0)/5
        //...
        //k=4 max(0,dp[m][4]+(a[5]-a[4])/1)0+(24-0)/5
        dp[m+1][n]=max(dp[m+1][n],dp[m][k]+(a[n]-a[k])/(double)(n-k));
      }
      //cout << dp[m+1][n] << " ";
    }
    //cout << endl;
  }
  cout << std::fixed << std::setprecision(6) << dp[M][N] << endl;
  //return 0;
  //cout << *max_element(dp[N].begin(),dp[N].end()) << endl;
}
