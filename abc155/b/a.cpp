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
  int N;
  cin >> N;
  vector<long long> A(N);
  bool d=true;
  for(int i =0;i<N;i++){
    cin >> A.at(i);
    if(A[i]%2==0){
      d=d&(A[i]%3==0 or A[i]%5==0);
      //cout << i << ":" << d << endl;
    }
  }
  if(d){
    cout << "APPROVED" << endl;
  }else{
    cout << "DENIED" << endl;
  }
}
