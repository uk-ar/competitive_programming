// for(int i =0;i<N;i++){
//   cin >> v.at(i);
// }
// single line with multi param
// vector of vector
//   vector<vector<int>> data(row,vector<int>(col));
//for(int row=0;row<N;row++){
//    for(int col=0;col<N;col++){
//  }}
#include <bits/stdc++.h>
using namespace std;

int rec(long long r1,long long c1,long long r2,long long c2){
  if(r1==r2 and c1==c2){
    return 0;
  }else if(r1+c1==r2+c2){
    return 1;
  }else if(r1-c1==r2-c2){
    return 1;
  }else if(abs(r1-r2)+abs(c1-c2)<=3){
    return 1;
  }else if(abs(r1-r2)+abs(c1-c2)<=6){
    return 2;
  }else if((r1+c1)%2 == (r2+c2)%2){
    return 2;
  }else if(abs(c2-r2-c1+r1)/1.41<=3 or abs(c2+r2-c1-r1)/1.41<=3){
    return 2;
  }else{
    return 3;
  }
}
int main() {
  long long r1,c1,r2,c2;
  cin >> r1 >> c1;
  cin >> r2 >> c2;
  // if(r1>r2)swap(r1,r2);
  // if(c1>c2)swap(c1,c2);
  //vector<vector<int>>dp(r1,r2)
  cout << rec(r1,c1,r2,c2) << endl;
}
