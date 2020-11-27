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
int digit(int N){
  int ret = 0;
  while(N>0){
    N = N/10;
    ret++;
  }
  return ret;
}
int rec(int N,int d,int flags,int acc){
  int ret=0;
  if(acc <= N and flags==7){
    ret++;
  }
  if(d==0){
    return ret;
  }
  for(int i=3;i<=7;i+=2){
    ret += rec(N,d-1,(flags | 1<<((i/2)-1)),acc*10+i);
  }
  return ret;
}
int main() {
  int N;
  cin >> N;
  cout << rec(N,digit(N),0,0) <<endl;
}
