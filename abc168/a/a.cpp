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
  int N;
  cin >> N;
  if(N%10==3){
    cout << "bon" << endl;
  }else if(N%10==0 or N%10==1 or N%10==6 or N%10==8){
    cout << "pon" << endl;
  }else{
    cout << "hon" << endl;
  }
}
