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
  int N=5;
  vector<int> v(N);
  for(int i =0;i<N;i++){
    cin >> v.at(i);
    if(v[i]==0){
      cout << i+1 << endl;
      exit(0);
    }
  }
}
