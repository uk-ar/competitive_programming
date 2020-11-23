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

int main() {
  int N,X;
  string S;
  cin >> N >> X;
  cin >> S;
  int ret = 0;
  for(char c:S){
    if(c=='o'){
      ret++;
    }else{
      ret = max(0,ret-1);
    }
  }
  cout << ret << endl;
}
