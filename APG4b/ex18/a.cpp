// int N,M;cin >> N >> M;
// vector<int> v(N);
// for(int i =0;i<N;i++){
//   cin >> v.at(i);
// }
// single line with multi param
// a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
// a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
//   vector<vector<int>> data(row,vector<int>(col));
//for(int row=0;row<N;row++){
//    for(int col=0;col<N;col++){
//  }
//}
#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG

using namespace std;

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A(M), B(M);
  for (int i = 0; i < M; i++) {
    cin >> A.at(i) >> B.at(i);
  }

  // ここにプログラムを追記
  // (ここで"試合結果の表"の2次元配列を宣言)
  //cout << N << ":" << M << endl;
  vector<vector<char>> data(N,vector<char>(N,'-'));
  for(int i=0;i<M;i++){
    data[A[i]-1][B[i]-1] = 'o';
    data[B[i]-1][A[i]-1] = 'x';
  }

  for(int row=0;row<N;row++){
    for(int col=0;col<N;col++){
      if(col==0){
        cout << data[row][col];
      }else{
        cout << " " << data[row][col];
      }
    }
    cout << endl;
  }
}
