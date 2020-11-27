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
  vector<long long> L(N);
  for(int i =0;i<N;i++){
    cin >> L.at(i);
  }
  int ret=0;
  sort(L.begin(),L.end());
  for(int i=0;i<N;i++){
    for(int j=0;j<i;j++){
      for(int k=0;k<j;k++){
        if(L[i]!=L[j] and L[i]!=L[k] and L[j]!=L[k]){
          if(L[k]+L[j]>L[i]){
            ret += 1;
          }
        }
      }
    }
  }
  cout << ret << endl;
}
