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
// check list
// * variable range
// * index range(0 origin or 1 origin)
#include <bits/stdc++.h>
using namespace std;

vector<bool>primes;
void initPrimes(long long N){
  primes.assign(N+1,true);
  for(long long i=2;i*i<=N;i++){
    if(primes[i]==true){
      for(long long j=2;i*j<=N;j++){
        primes[i*j]=false;
      }
    }
  }
}

void print(const std::vector<int>& v)
{
  std::for_each(v.begin(), v.end(), [](int x) {
    std::cout << x << " ";
  });
  std::cout << std::endl;
}

int main() {
  long long N;
  cin >> N;
  vector<long long>first(0);//prime factors
  vector<long long>second(0);//prime factors
  for(long long j=1;j*j<=N;j++){
    if(N%j==0){
      first.push_back(j);
      if(j!=N/j) second.push_back(N/j);
    }
  }
  reverse(second.begin(),second.end());
  first.insert(first.end(),second.begin(),second.end());
  for(long long e:first)
    cout << e << endl;

}
