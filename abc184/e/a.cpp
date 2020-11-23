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
int H,W;
unordered_map<char,vector<vector<int> >>m;
int bfs(vector<string>&A,vector<vector<int>>&dp,int r,int c,int d){
  deque<vector<int>> nodes({{r,c,d}});
  while(!nodes.empty()){
    r = nodes.front()[0];
    c = nodes.front()[1];
    d = nodes.front()[2];
    nodes.pop_front();
    //cout << r << ":" << c << endl;
    if(r<0 or H<=r or c<0 or W<=c or A[r][c]=='#'){
       continue;
    }
    if(A[r][c]=='G'){
      return d;
    }
    if(dp[r][c] <= d){
       continue;
    }
    //cout << r << ":" << c << endl;
    dp[r][c] = d;
    //for(vector<int> dr:vector<vector<int>>({{0,1},{1,0},{-1,0},{0,-1}})){
    for(vector<int> dr:vector<vector<int>>({{r,c+1},{r+1,c},{r-1,c},{r,c-1}})){
      if(dr[0]<0 or H<=dr[0] or dr[1]<0 or W<=dr[1] or A[dr[0]][dr[1]]=='#' or dp[dr[0]][dr[1]]<=d){
        continue;
      }
      //cout << dr[0] << ":" << dr[1] << endl;
      nodes.push_back(vector<int>({dr[0],dr[1],d+1}));
      //nodes.push_back(vector<int>({r+dr[0],c+dr[1],d+1}));
    }
    for(vector<int> dr:m[A[r][c]]){
      // if(dr[0]<0 or H<=dr[0] or dr[1]<0 or W<=dr[1] or A[dr[0]][dr[1]]=='#'){
      //   continue;
      // }
      if(dr[0]<0 or H<=dr[0] or dr[1]<0 or W<=dr[1] or A[dr[0]][dr[1]]=='#' or dp[dr[0]][dr[1]]<=d){
        continue;
      }
      nodes.push_back(vector<int>({dr[0],dr[1],d+1}));
    }
    m.erase(A[r][c]);
  }
  return -1;
}

int main() {
  cin >> H >> W;
  vector<string>A(H);
  int rs,cs;
  for(int r=0;r<H;r++){
    cin >> A[r];
    for(int c=0;c<W;c++){
      if(A[r][c]!='S' and A[r][c]!='G' and A[r][c]!='.' and A[r][c]!='#'){
        m[A[r][c]].push_back(vector<int>({r,c,0}));
      }else if(A[r][c]=='S'){
        rs = r;
        cs = c;
      }
    }
  }
  vector<vector<int>>dp(H,vector<int>(W,INT_MAX));
  cout << bfs(A,dp,rs,cs,0) << endl;
  //cout << std::fixed << std::setprecision(9) <<ret << endl;
}
