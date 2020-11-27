// int N,M;cin >> N >> M;
// vector<int> v(N);
// for(int i =0;i<N;i++){
//   cin >> v.at(i);
// }
// single line with multi param
// a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
// a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG

using namespace std;

int main() {
  int N, S;
  cin >> N >> S;
  vector<int> A(N), P(N);
  for (int i = 0; i < N; i++) {
    cin >> A.at(i);
  }
  for (int i = 0; i < N; i++) {
    cin >> P.at(i);
  }

  // リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
  // ここにプログラムを追記
  int ret=0;
  for(int a: A){
    for(int p: P){
      if(a+p==S){
        ret += 1;
      }
    }
  }
  cout << ret << endl;
}
