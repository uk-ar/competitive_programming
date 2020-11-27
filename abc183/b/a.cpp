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
  long long x1,y1,x2,y2;
  cin >> x1 >> y1 >> x2 >> y2;
  y2 = -y2;
  if(x1==x2){
    cout << x1;
    exit(0);
  }
  // x1*=1000;
  // x2*=1000;
  // y1*=1000;
  // y2*=1000;
  double b = (y2-y1)*x1/(double)(x2-x1)-y1;
  //cout << 1*b*(x2-x1)/(double)(y2-y1);
  cout << std::fixed << std::setprecision(15) << x1-(x2-x1)*y1/(double)(y2-y1);
  //cout << (x2*y1+x1*y2-2*x1*y1)/(double)(y2-y1);
}
