
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
  vector<int> A(N);
  for(int i =0;i<N;i++){
    cin >> A.at(i);
  }
  int M = *max_element(A.begin(),A.end());
  int ind = 0;
  int ma = 0;
  for(int i=2;i<=M;i++){
    int temp = 0;
    for(int j=0;j<N;j++){
      if(A[j]%i==0){
        temp ++;
      }
    }
    if(temp>=ma){
      ma=temp;
      ind=i;
    }
  }
  cout << ind << endl;
}
