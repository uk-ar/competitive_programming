// vector<int> v(N);
// for(int i =0;i<N;i++){
//   cin >> v.at(i);
// }
// single line with multi param
// vector of vector
//   vector<vector<int>> data(row,vector<int>(col));
//for(int row=0;row<N;row++){
//    for(int col=0;col<N;col++){
//      cin >> data[row][col];
//  }}
//  cout << std::fixed << std::setprecision(9) <<ret << endl;
// sort(A.begin(),A.end(),greater<int>());
// int s = accumulate(A.begin(),A.end(),0);
#include <bits/stdc++.h>
using namespace std;

int main() {
  int a,b;
  cin >> a >> b;
  string A;
  for(int i=0;i<b;i++){
    A+=a+'0';
  }
  string B;
  for(int i=0;i<a;i++){
    B+=b+'0';
  }
  if(A<B){
    cout << A << endl;
  }else{
    cout << B << endl;
  }
}
