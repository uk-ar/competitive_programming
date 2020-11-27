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
// sort(A.begin(),A.end(),greater<int>());
// int s = accumulate(A.begin(),A.end(),0);
#include <bits/stdc++.h>
using namespace std;

int main() {
  int N,M;
  cin >> N >> M;
  vector<long long> A(N);
  for(int i =0;i<N;i++){
    cin >> A.at(i);
  }
  // sort(A.begin(),A.end(),greater<int>());
  int s = accumulate(A.begin(),A.end(),0);
  int ret=0;
  for(int i=0;i<N;i++){
    if(A[i]>=s/(double)(4*M)){
      // cout << "No" << endl;
      // exit(0);
      ret += 1;
    }
  }
  if(ret>=M){
    cout << "Yes" << endl;
  }else{
    cout << "No" << endl;
  }
}
