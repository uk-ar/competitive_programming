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
  vector<long long> A(N);
  vector<long long> B(N);
  for(int i =0;i<N;i++){
    cin >> A.at(i) >> B.at(i);
  }
  long long ret = 0;
  for(int i=0;i<N;i++){
    // for(int j=A[i];j<=B[i];j++){
    //   ret += j;
    // }
    ret += (A[i]+B[i])*(B[i]-A[i]+1)/2;
    // if(A[i]+B[i]%2==0){
    //   ret += (A[i]+B[i])/2*(B[i]-A[i]+1);
    // }else{
    //   ret += (B[i]-A[i]+1)/2*(A[i]+B[i]);
    // }
  }
  cout << ret << endl;
}
