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
  long long N,X;
  string S;
  cin >> N >> X;
  cin >> S;
  for(char c:S){
    if(c=='o'){
      X++;
    }else{
      X = max((long long)0,X-1);
    }
  }
  cout << X << endl;
}
