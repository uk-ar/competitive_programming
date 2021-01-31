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
// sort(A.begin(),A.end(),greater<int>());
// int s = accumulate(A.begin(),A.end(),0);
#include <bits/stdc++.h>
using namespace std;

struct UnionFind{
  vector<int> parents,siz;
  UnionFind(int N): parents(N,-1), siz(N,1){}
  //x 根を求める
  int root(int x){
    if(parents[x]==-1)return x;
    return parents[x] = root(parents[x]);
  }
  //x とyが同じグループに属するかどうか
  bool issame(int x,int y){
    return root(x)==root(y);
  }
  //x を含むグループと yを含むグループを併合
  bool unite(int x,int y){
    x = root(x);
    y = root(y);
    if(x==y)return false;
    if(x>y)swap(x,y);
    // サイズが大きい方のグループに併合
    parents[x]=y;
    siz[y]+=siz[x];
    return true;
  }

  //x を含むグループのサイズ
  int size(int x){
    return siz[root(x)];
  }
};

template <typename T, typename S> inline void print(const pair<T, S>& p) {cout << p.first << " " << p.second << endl;}
template <typename T> inline void print(const T& x) {cout << x << '\n';}
template <typename T, typename S> inline void print(const vector<pair<T, S> >& v) {for (auto&& p : v) print(p);}
template <typename T> inline void print(const vector<T>& v, string s = " ") {for(int i=0;i<v.size();i++) cout << v[i] << (i !=(long long)v.size() - 1 ? s : "\n");}
template < typename T > void pprint(T const& a){  std::cout << " " << a ; }
template < typename... Args > void pp(Args... args){using swallow = std::initializer_list<int>; (void)swallow{ (void( pprint(args) ), 0)... }; cout << endl; }

signed main() {
  int V = in();//頂点
  int M = in();//辺 friend
  int K = in();//辺 block

  vector<int> A(M);
  vector<int> B(M);
  UnionFind ufm(V);
  for(int i=0;i<M;i++){
    cin >> A.at(i) >> B.at(i);
    A[i]--;B[i]--;
    ufm.unite(A[i],B[i]);
  }

  vector<int>ret(V);
  for(int i=0;i<V;i++){
    ret[i]=ufm.size(i);
  }
  for(int i=0;i<M;i++){
    ret[A[i]]--;
    ret[B[i]]--;
  }

  vector<int> C(K);
  vector<int> D(K);
  UnionFind ufk(V);
  for(int i=0;i<K;i++){
    cin >> C.at(i) >> D.at(i);
    C[i]--;D[i]--;
    ret[C[i]]--;
    ret[D[i]]--;
  }
  print(ret);
}
