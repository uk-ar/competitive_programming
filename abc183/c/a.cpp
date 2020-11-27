// int N,M;cin >> N >> M;
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
#include <bits/stdc++.h>
using namespace std;
int N,K;

int dfs(vector<vector<int>> &data,unordered_set<int> &v,vector<int> path,int acc){
  if(path.size()==data.size()){
    //cout << acc << ":" << path.size() << endl;
    if((acc + data[path.back()][0])==K){
      return 1;
    }
    return 0;
  }
  int ret = 0;
  for(int i=0;i<N;i++){
    if(v.count(i)==0){
      int n = acc + data[path.back()][i];//0,1=>1
      v.emplace(i);
      path.push_back(i);//[0,1]//2
      ret += dfs(data,v,path,n);
      path.pop_back();
      v.erase(i);
    }
  }
  return ret;
}

int main() {
  cin >> N >> K;
  vector<vector<int>> data(N,vector<int>(N));
  for(int row=0;row<N;row++){
    for(int col=0;col<N;col++){
      cin >> data[row][col];
      //cout << data[row][col] << " ";
    }
    //cout << endl;
  }
  unordered_set<int> v;
  v.emplace(0);
  vector<int> path({0});
  cout << dfs(data,v,path,0) << endl;
}
