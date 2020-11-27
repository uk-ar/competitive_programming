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
#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<vector<int>> data(3,vector<int>(3));
    unordered_map<int,vector<int>> m;
    for(int row=0;row<3;row++){
      for(int col=0;col<3;col++){
        cin >> data[row][col];
        m[data[row][col]]=vector<int>({row,col});
      }
    }
    int N;
    cin >> N;
    vector<int> B(N);
    vector<int> r(3,3);
    vector<int> c(3,3);
    int d1=3;
    int d2=3;
    for(int i =0;i<N;i++){
      cin >> B.at(i);
      if(m.count(B[i])>0){
        //data[m[B[i]][0]][m[B[i]][1]]=0;
        r[m[B[i]][0]]--;
        c[m[B[i]][1]]--;
        if(m[B[i]][0]==m[B[i]][1]){
          d1--;
        }
        if(m[B[i]][0]+m[B[i]][1]==2){
          d2--;
        }
        if(r[m[B[i]][0]]==0 or c[m[B[i]][1]]==0 or d1==0 or d2==0){
          cout << "Yes" << endl;
          exit(0);
        }
      }
    }
    string ANS="No";
    // for(int i=0;i<3;i++){
    //   if(r[i]==0) {ANS="Yes";}
    //   if(c[i]==0) {ANS="Yes";}
    // }
    // if(d1==0 or d2==0){
    //   ANS="Yes";
    // }
    cout << ANS << endl;
}
