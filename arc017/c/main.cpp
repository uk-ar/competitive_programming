// set<int, greater<int> > s;
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
// long long s = accumulate(A.begin(),A.end(),(long long)0);
// unordered_map<string,int>m({{"SUN",1},{"MON",2},{"TUE",3},{"WED",4},{"THU",5},{"FRI",6},{"SAT",7}});
// max({A,B,C});
// S.substr(i,2)=="RS"
// SS.erase (std::remove(SS.begin(), SS.end(), 'A'), SS.end()); //delete string
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
// * agc017_a
// * agc040_a
// * agc028_a
// * agc008_a
// * agc007_a
// * abc116_c
// * abc064_c
// * agc016_a
// * agc034_a
// * cf16_b
// * abc188_e
// * abc052_c
// * abc110_d
// * abc142_d
// * arc067_c
// * abc146_c
// * abc061_c
// * abc114_d
// * abc114_c
// * arc032_a
// * arc034_c
// * aoj_2706
// * aoj_DSL_3_D
// * abc172_c
// * arc084_c
// * arc110_a
// * apc001_a
// * abc124_d
// * arc106_b
// * abc157_d
// * agc046_a
// * abc185_d
// * arc044_a
// * abc046_a
// * abc039_c
// * arc107_b
// * arc054_a
// * abc136_d
// * arc051_a
// * abc180_d
// * abc190_d
// * abc121_d
// * abc038_c
// * abc130_d
// * abc127_d
// * arc018_b
// * arc001_c
// * digitalarts2012_a
// * code-festival-2015-quala_c
// * abc192_d
// * srm_StockHistory
// * dp_i
// * srm_BinaryFlips
// * abc088_c
// * past202004-open_d
// * past201912-open_e
// * past201912-open_h
// * past202005-open_g
// * abc161_d
// * dp_a
// * dp_e
// * past202005-open_h
// * tdpc_a
// * past202004-open_h
// * past201912-open_g
// check list
// * variable range
// * immeditate value is int range(accumulate)
// * index range(0 origin or 1 origin)
// * input is complete?
// * unued input
// * loop initial value
// * check variable range maximum and minimum
// * misunderstand input(node Edge and node Vertex)
// * check que front and back
// * check using INT_MAX
// * modify element in graph retrieval
// * dp initial value, max index+1
// * return value could be negative?(initial value 0 to INT_MIN)
#include <bits/stdc++.h>
using namespace std;

//https://www2.slideshare.net/Roadagain/ss-71620380
//https://github.com/kurokoji/.cpp-Template/blob/master/template/template.cpp
#define int long long
//check over flow
//assert(a<LONG_LONG_MAX-b)
//a+b
//assert(a<LONG_LONG_MAX/b)
//a*b
struct Fast {Fast(){std::cin.tie(0);ios::sync_with_stdio(false);}} fast;

/* cpp template {{{ */

/* short */
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define Fi first
#define Se second
#define ALL(v) begin(v), end(v)
#define RALL(v) rbegin(v), rend(v)
// #define X real()
// #define Y imag()

/* REPmacro */
#define REPS(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define REP(i, n) REPS(i, 0, n)
#define RREP(i, n) REPS(i, 1, n + 1)
#define DEPS(i, a, n) for (ll i = (a); i >= (ll)(n); --i)
#define DEP(i, n) DEPS(i, n, 0)
#define EACH(i, n) for (auto&& i : n)

/* debug */
#define debug(x) cerr << #x << ":" << x << " " << "(L:" << __LINE__ << ")" << '\n';

/* alias */
using ll = long long;
using ull = unsigned long long;
using vi = vector<int>;
using vvi = vector<vi>;
using vvvi = vector<vvi>;
using pii = pair<int, int>;
using D = double;
using P = complex<D>;
using vs = vector<string>;
template <typename T> using PQ = priority_queue<T>;
template <typename T> using minPQ = priority_queue<T, vector<T>, greater<T> >;

/* const */
const int INF = 1001001001;
const ll LINF = 1001001001001001001ll;
const int MOD = 1e9 + 7;
const D EPS = 1e-9;
const int dx[] = {0, 1, 0, -1, 1, -1, 1, -1}, dy[] = {1, 0, -1, 0, 1, -1, -1, 1};

/* func */
inline bool inside(int y, int x, int H, int W) {return y >= 0 && x >= 0 && y < H && x < W;}
template <class T = int> inline T in() {T x; cin >> x; return (x);}
inline vs split(const string& t, char c) {vs v; stringstream s(t); string b; while(getline(s, b, c)) if(b!="")v.eb(b); return v;}
inline string join(const vs &ss,char c){string s;REP(i,ss.size()){s+=(i!=(ll)ss.size()-1?ss[i]+c:ss[i]);}return s;}
template <typename T> inline bool chmin(T& a, const T& b) {if (a > b) a = b; return a > b;}
template <typename T> inline bool chmax(T& a, const T& b) {if (a < b) a = b; return a < b;}

template <typename T> using min_priority_queue = priority_queue<T, vector<T>, greater<T>>;

template <typename T, typename S> inline void print(const pair<T, S>& p) {cout << p.first << " " << p.second << endl;}
template <typename T> inline void print(const T& x) {cout << x << '\n';}
template <typename T, typename S> inline void print(const vector<pair<T, S> >& v) {for (auto&& p : v) print(p);}
template <typename T> inline void print(const vector<T>& v, string s = " ") {for(int i=0;i<v.size();i++) cout << v[i] << (i !=(long long)v.size() - 1 ? s : "\n");}
template <typename T> inline void print(const T& b, const T&e, string s = " ") {for(auto i=b;i!=e;i++) print(*i);}
template < typename T > void pprint(T const& a){  std::cout << " " << a ; }
template < typename... Args > void pp(Args... args){using swallow = std::initializer_list<int>; (void)swallow{ (void( pprint(args) ), 0)... }; cout << endl; }

template <typename T> inline vector<pair<T,int> > counter(const vector<T>& v) {unordered_map<T,int> m;for(int i=0;i<v.size();i++) m[v[i]]++;return {m.begin(),m.end()};}
inline vector<pair<char,int> > counter(const string& v) {unordered_map<char,int> m;for(int i=0;i<(long long)v.size();i++) m[v[i]]++;return{m.begin(),m.end()};}
// clang-format on
/* }}} */

string enc(long long i,long long j){
  return to_string(i)+" "+to_string(j);
}
uint64_t combinations2(uint64_t n, uint64_t k) {
  uint64_t r = 1;
  for (uint64_t d = 1; d <= k; ++d) {
    r *= n--;
    r /= d;
  }
  return r;
}

signed main() {
  int N = in();
  int X = in();
  int NE = (N+1)/2;
  int NO = N/2;
  vi WE(NE);
  vi WO(NO);
  REP(i,N){
    if((i&1)==1)//odd
      cin >> WO.at((i-1)/2);
    else
      cin >> WE.at(i/2);
  }

  unordered_map <int,int> m;
  REP(state,1<<NE){
    int acc = 0;
    REP(i,NE)
      if(((state>>i)&1)==1) acc += WE[i];
    m[acc]++;
  }

  int ret = 0;
  REP(state,1<<NO){
    int acc = 0;
    REP(i,NO)
      if(((state>>i)&1)==1) acc += WO[i];
    if(m.count(X-acc) > 0)
      ret += m[X-acc];
  }
  cout << ret << endl;
}
