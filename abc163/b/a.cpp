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
//  cout << std::fixed << std::setprecision(9) <<ret << endl;
#include <bits/stdc++.h>
using namespace std;

int main() {
  int N,M;
  cin >> N >> M;
  vector<long long> A(M);
  for(int i =0;i<M;i++){
    cin >> A.at(i);
  }
  int ret = N-accumulate(A.begin(),A.end(),0);
  if(ret<0){
    ret = -1;
  }
  cout << ret << endl;
}
