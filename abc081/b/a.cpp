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

int div2(int n){
  int ret=0;
  while(n > 0 and n%2==0){
    n = n/2;
    ret++;
  }
  return ret;
}
int main() {
  int N;
  cin >> N;
  vector<int> v(N);
  for(int i =0;i<N;i++){
    int e;
    cin >> e;
    v[i]=div2(e);
    //cout << v[i] << endl;
  }
  cout << *min_element(v.begin(),v.end())<<endl;
}
