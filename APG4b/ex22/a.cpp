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

int main() {
  int N;
  cin >> N;
  vector<vector<int>> ab(N,vector<int>(2));
  for(int i=0;i<N;i++){
    cin >> ab[i][0] >> ab[i][1];
  }
  sort(ab.begin(),ab.end(),[](const vector<int>&x,const vector<int>&y){return x[1] < y[1];});
  for(int i=0;i<N;i++){
    cout << ab[i][0] << " " << ab[i][1] << endl;
  }
}
