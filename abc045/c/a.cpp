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

long long rec(string &s,int ind,long long cur,long long acc){
  //cout << ind << ":" << cur <<endl;
  long long ret = 0;
  if(ind == s.size()){
    return cur+acc;
  }
  ret += rec(s,ind+1,cur*10+s[ind]-'0',acc);//1
  ret += rec(s,ind+1,s[ind]-'0',acc+cur);//1
  return ret;
}
int main() {
  string S;
  cin >> S;
  cout << (long long)rec(S,1,S[0]-'0',0) <<endl;
}
