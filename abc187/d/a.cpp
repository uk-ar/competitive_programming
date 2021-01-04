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
// * arc108_b
// * abc157_c
// * sumitrust2019_c
// * abc165_c
// * abc031_d
// * abc023_d
// * agc021_a
// * abc139_b
// * agc041_a
// * abc120_c
// * arc073_c
// * arc069_c
// * agc014_a
// * abc103_c
// check list
// * variable range
// * index range(0 origin or 1 origin)
// * input is complete?
// * unued input
// * misunderstand input(node edge and node point)
#include <bits/stdc++.h>
using namespace std;

void print(const std::vector<vector<long long> >& v)
{
  if(v.empty())return;
  cout << v[0][0] << ":" << v[0][1];
  for(int i=1;i<v.size();i++){
    cout << " " << v[i][0] << ":" << v[i][1];
  }

  std::cout << std::endl;
}

string enc(long long i,long long j){
  return to_string(i)+" "+to_string(j);
}

int main() {
  long long N;
  cin >> N;

  vector<long long> A(N);
  vector<long long> B(N);
  vector<vector<long long> > C(N);
  for(long long i=0;i<N;i++){
    cin >> A.at(i) >> B.at(i);
    C[i]={A[i]*2+B[i],i};
  }
  sort(C.begin(),C.end(),greater<vector<long long> >());
  //print(C);
  long long acc_A=accumulate(A.begin(),A.end(),0);//NG?
  long long votes=0;
  long long i;
  for(i=0;i<N;i++){
    //cout << votes << ":" << acc_A << endl;
    if(votes > acc_A){
      cout << i << endl;
      exit(0);
    }else{
      acc_A -= A[C[i][1]];
      votes += A[C[i][1]]+B[C[i][1]];
    }
  }
  cout << i << endl;
  //-A vs A+B;

  //cout << ret << endl;
}
