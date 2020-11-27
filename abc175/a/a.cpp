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
  string S;
  cin >> S;
  int ret = 0;
  int i=0;
  while(i<S.size()){
    int j=i;
    while(j<S.size() and S[j]=='R'){
      ret = max(ret,j+1-i);
      j++;
    }
    i = j+1;
  }
  cout << ret << endl;
}
