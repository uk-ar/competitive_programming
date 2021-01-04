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
// check list
// * variable range
// * index range(0 origin or 1 origin)
#include <bits/stdc++.h>
using namespace std;

int main() {
  string N;
  cin >> N;
  vector<int>A(3);
  int acc=0;
  for(int i=0;i<N.size();i++){
    acc+=N[i]-'0';
    A[(N[i]-'0')%3]++;
  }
  if(acc<3){
    cout << -1 << endl;
  }else if(acc%3==0){
    cout << 0 << endl;
  }else if(acc%3==1){
    //1ooi
    if(A[1]>0 and N.size()>1){
      cout << 1 << endl;
    }else if(A[2]>0 and N.size()>2){
      cout << 2 << endl;
    }else{
      cout << -1 << endl;
    }
  }else{
    if(A[2]>0 and N.size()>1){
      cout << 1 << endl;
    }else if(A[1]>1 and N.size()>2){
      cout << 2 << endl;
    }else{
      cout << -1 << endl;
    }
  }
}
