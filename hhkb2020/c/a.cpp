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
  long long N = 0;
  cin >> N;
  vector<bool> v(200002,false);
  long long cur=0;
  for(long long i =0;i<N;i++){
    long long t;
    cin >> t;
    v.at(t) = true;
    while(cur < 200002 && v.at(cur)){
      cur += 1;
    }
    cout << cur << endl;
  }
}
