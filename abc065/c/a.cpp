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
// to be review
// * abc139_b
// * abc099_b
// check list
// * variable range
// * index range(0 origin or 1 origin)
#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007

int main() {
  int N,M;
  cin >> N >> M;

  if(abs(N-M)>1){
    cout << 0 << endl;
    exit(0);
  }

  long long PN=1;
  for(int i=1;i<=N;i++){
    PN = (PN*i)%MOD;
    //cin >> A.at(i) >> B.at(i);
  }
  long long PM=1;
  for(int i=1;i<=M;i++){
    PM = (PM*i)%MOD;
    //cin >> A.at(i) >> B.at(i);
  }
  if(N==M){
    cout << ((PN*PM)%MOD*2)%MOD << endl;
  }else{
    cout << (PN*PM)%MOD << endl;
  }

}
