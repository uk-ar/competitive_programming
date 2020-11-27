// vector<int> v(N);
// for(int i =0;i<N;i++){
//   cin >> v.at(i);
// }
// single line with multi param
// vector of vector
//   vector<vector<int>> data(row,vector<int>(col));
//for(int row=0;row<N;row++){
//    for(int col=0;col<N;col++){
//  }}
//  cout << std::fixed << std::setprecision(9) <<ret << endl;
#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  int AC,WA,TLE,RE;
  AC=WA=TLE=RE=0;
  for(int i =0;i<N;i++){
    string s;
    cin >> s;
    if(s=="AC"){
      AC++;
    }else if(s=="WA"){
      WA++;
    }else if(s=="TLE"){
      TLE++;
    }else{
      RE++;
    }
  }
  cout << "AC x " << AC << endl;
  cout << "WA x " << WA << endl;
  cout << "TLE x " << TLE << endl;
  cout << "RE x " << RE << endl;
}
