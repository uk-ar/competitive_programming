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
vector<long long>h;
vector<long long>s;
bool isOK(long long mid,int N){
  vector<long long>r(N);//rest time

  for(int i=0;i<N;i++){
    if(mid<h[i]){
      return false;
    }
    r[i]=(mid-h[i])/s[i];//残り時間
  }
  sort(r.begin(),r.end());
  for(int i=0;i<N;i++){
    if(r[i]<i){
      return false;
    }
  }
  return true;
}
int main() {
  int N;
  cin >> N;
  h.assign(N,0);
  s.assign(N,0);
  for(int i=0;i<N;i++){
    cin >> h[i] >> s[i];
  }
  long long ok = 0;//ok以下の高度で割る
  for(int i=0;i<N;i++){
    ok=max(ok,h[i]+s[i]*(N+1));
  }
  long long ng = -1;
  while(abs(ok-ng)>1){
    int mid = (ok+ng)/2;
    if(isOK(mid,N)){
      ok=mid;
    }else{
      ng=mid;
    }
  }
  cout << ok << endl;
}
