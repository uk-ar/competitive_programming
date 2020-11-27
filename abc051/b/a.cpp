// int N,M;cin >> N >> M;
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
#include <bits/stdc++.h>
using namespace std;

int main() {
  int K,S;
  cin >> K >> S;
  int ret=0;
  for(int x=0;x<=K;x++){
    for(int y=0;y<=K;y++){
      int z = S-x-y;
      if(0<= z and z<=K){
        ret++;
      }
    }
  }
  cout << ret <<endl;
}
