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
  int X,Y;
  cin >> X >> Y;
  if(Y%2==1){
    cout << "No" << endl;
  }else if(4*X<Y or Y<2*X){
    cout << "No" << endl;
  }else{
    cout << "Yes" << endl;
  }
}
