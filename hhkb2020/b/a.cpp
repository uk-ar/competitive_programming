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
  int H,W;
  cin >> H >> W;
  vector<vector<int>> rc(H,vector<int>(W));
  //cout << H << ":" << W << endl;
  for(int i=0; i<H;i++){
    string S;
    cin >> S;
    for(int j=0; j<W;j++){
      rc[i][j] = S[j];
    }
  }
  //cout << H << ":" << W << endl;
  int ret = 0;
  for(int i=0; i<H; i++){
    for(int j=0; j<W; j++){
      //cout << i << ":" << j << endl;
      if(rc[i][j] == '.'){

        if(i+1<H and rc[i+1][j] == '.'){
          ret += 1;
        }
        if(j+1<W and rc[i][j+1] == '.'){
          ret += 1;
        }
      }
    }
  }
  cout << ret << endl;
}
