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
#define LEFT 0
#define TOP 1
#define DIA 2

int main() {
  string S,T;
  cin >> S >> T;
  //cout << s << endl;
  //cout << t << endl;
  vector<vector<int>>dp(S.size()+1,vector<int>(T.size()+1,0));
  vector<vector<int>>dr(S.size()+1,vector<int>(T.size()+1,0));//dir
  for(int s=0;s<S.size();s++){
    for(int t=0;t<T.size();t++){
      dp[s+1][t+1]=dp[s][t+1];
      dr[s+1][t+1]=TOP;
      if(dp[s+1][t+1]<dp[s+1][t]){
        dp[s+1][t+1]=dp[s+1][t];
        dr[s+1][t+1]=LEFT;
      }
      if(S[s]==T[t]){
        dp[s+1][t+1]=dp[s][t]+1;
        dr[s+1][t+1]=DIA;
      }
      // if(dp[s+1][t+1]<=dp[s][t]){
      //   }else{
      //     dp[s+1][t+1]=dp[s][t];
      //   }
      // }
      //cout << dp[s][t] << " ";
    }
    //cout << endl;
  }
  int s = S.size();
  int t = T.size();
  string ret="";
  while(dp[s][t]!=0){
    if(dr[s][t]==TOP){
      s--;
    }else if(dr[s][t]==LEFT){
      t--;
    }else{
      s--;
      t--;
      ret+=S[s];
    }
  }
  reverse(ret.begin(),ret.end());
  cout << ret << endl;
  return 0;
  //cout << *max_element(dp[N].begin(),dp[N].end()) << endl;
}
