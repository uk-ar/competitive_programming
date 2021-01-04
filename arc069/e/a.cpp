// vector<int> v(N);
// for(int i =0;i<N;i++){
//   cin >> v.at(i);
// }
// single line with multi param
// vector of vector
//   vector<vector<int>> data(row,vector<int>(col));
//for(int row=0;row<N;row++){
//    for(int col=0;col<N;col++){
//      cin >> data[row][col];
//  }}
//  cout << std::fixed << std::setprecision(9) <<ret << endl;
// sort(A.begin(),A.end(),greater<int>());
// int s = accumulate(A.begin(),A.end(),0);
// unordered_map<string,int>m({{"SUN",1},{"MON",2},{"TUE",3},{"WED",4},{"THU",5},{"FRI",6},{"SAT",7}});
// max({A,B,C});
// S.substr(i,2)=="RS"
// char c = 'a';string({c});
// transform(ret.begin(),ret.end(),ret.begin(),::toupper);
// to be review
// * abc139_b
// * abc099_b
// * abc090_a
// * abc062_a
// * abc032_a
// * abc030_b
// * abc027_b
// * abc021_a
// * abc018_a
// * abc182_c
// * abc181_c
// * abc175_c
// * abc170_c
// * abc161_c
// * abc154_c space O(1)
// * abc151_c
// * abc147_c
// * abc113_c
// * abc123_c
// * abc115_c
// * abc153_d
// * abc120_c
// * abc081_b
// * sumitrust2019_c
// check list
// * variable range
// * index range(0 origin or 1 origin)
#include <bits/stdc++.h>
using namespace std;

void print(const std::vector<int>& v)
{
  std::for_each(v.begin(), v.end(), [](int x) {
    std::cout << x << " ";
  });
  std::cout << std::endl;
}

string enc(long long i,long long j){
  return to_string(i)+" "+to_string(j);
}

int main() {
  int N,M;
  cin >> N >> M;
  int A,B;
  cin >> A >> B;
  int C,D;
  cin >> C >> D;
  int H,W;
  cin >> H >> W;
  string S;
  cin >> S;
  int N = S.size();
  vector<long long> A(N);
  vector<long long> B(N);
  for(int i=0;i<N;i++){
    cin >> A.at(i) >> B.at(i);
  }
  if(true){
    cout << "Yes" << endl;
    cout << "YES" << endl;
  }else{
    cout << "No" << endl;
    cout << "NO" << endl;
  }
  cout << std::fixed << std::setprecision(9) <<ret << endl;
  cout << ret << endl;
}
