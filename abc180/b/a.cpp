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
  vector<long long> v(N);
  for(int i =0;i<N;i++){
    cin >> v.at(i);
  }
  long long m,y,c;
  m=y=c=0;
  for(int i =0;i<N;i++){
    m+=abs(v[i]);
    y+=pow(v[i],2);
    c=max(abs(v[i]),abs(c));
  }
  cout << m << endl;
  cout << std::fixed << std::setprecision(15) << pow((double)y,0.5) << endl;
  cout << c << endl;
}
