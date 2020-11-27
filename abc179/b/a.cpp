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
  vector<int> D1(N);
  vector<int> D2(N);
  for(int i =0;i<N;i++){
    cin >> D1.at(i) >> D2.at(i);
  }
  for(int i=2;i<N;i++){
    if(D1[i]==D2[i] and D1[i-1]==D2[i-1] and D1[i-2]==D2[i-2]){
      cout << "Yes" << endl;
      exit(0);
    }
  }
  cout << "No" << endl;
}
