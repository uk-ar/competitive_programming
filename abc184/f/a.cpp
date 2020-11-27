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

bool isOK(vector<int> &A,long long mid){
  //mid分以下
}
int main() {
  int N,T;
  cin >> N >> T;
  vector<int> A;
  for(int i =0;i<N;i++){
    cin >> A.at(i);
  }
  long long ng = -1;
  long long ok = INT_MAX * 40;
  while(abs(ok-ng)>1){
    long long mid= (ok+ng)/2;
    if(isOK(A,mid)){
      ok=mid;
    }else{
      ng=mid;
    }
  }
  cout << ok << endl;
}
