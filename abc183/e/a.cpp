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
  int H,W;
  cin >> N >> W;
  unordered_map<int,long long> imos;
  //vector<vector<int>> data(N,vector<int>(3));
  for(int row=0;row<N;row++){
      int S,T,P;
      cin >> S >> T >> P;
      imos[S]=imos[S]+P;
      imos[T]-=P;
  }
  // for(auto p:imos){
  //   cout << p.first << ": " << p.second << endl;
  // }

  map<int, long long> ordered(imos.begin(), imos.end());
  vector<long long>imos2({0});
  for(auto it = ordered.begin(); it != ordered.end(); ++it)
    imos2.push_back(it->second);
  for(int i=0;i<imos2.size();i++){
    imos2[i+1]=imos2[i]+imos2[i+1];
    //cout << i+1 << ":" << imos2[i+1] << endl;
    if(imos2[i+1]>W){
      cout << "No" << endl;
      exit(0);
      }
  }
  cout << "Yes" << endl;
}
