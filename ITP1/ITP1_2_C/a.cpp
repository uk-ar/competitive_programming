// int N,M;cin >> N >> M;
// vector<int> v(N);
// for(int i =0;i<N;i++){
//   cin >> v.at(i);
// }
// single line with multi param
// a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
// a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
// vector of vector
//   vector<vector<int>> data(row,vector<int>(col));
//for(int row=0;row<N;row++){
//    for(int col=0;col<N;col++){
//  }}
#include <bits/stdc++.h>
using namespace std;

int main(){
  vector <int>v(3);
  for(int i=0;i<3;i++){
    cin >> v[i];
  }
  sort(v.begin(),v.end());
  for(int i=0;i<3;i++){
    if(i==0){
      cout << v[i];
    }else{
      cout <<" "<< v[i];
    }
  }
  cout << endl;
}
