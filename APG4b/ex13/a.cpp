// int N,M;cin >> N >> M;
// vector<int> v(N);
// for(int i =0;i<N;i++){
//   cin >> v.at(i);
// }
// single line with multi param
// a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
// a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
//#include <bits/stdc++.h>
#define _GLIBCXX_DEBUG
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> v(N);
  int sum = 0;
  for(int i =0;i<N;i++){
    cin >> v.at(i);
    sum += v.at(i);
  }
  int avg = sum/N;
  for(int e:v){
    cout << abs(e-avg) << endl;
  }
}
