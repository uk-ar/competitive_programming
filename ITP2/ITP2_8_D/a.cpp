#include <bits/stdc++.h>
using namespace std;

int main(){
    int q;
    multimap <string,int>m;
    cin >> q;
    for(int i=0;i<q;i++){
      int c,x;
      string str,l,r;
      cin >> c;
      if(c==0){
        cin >> str >> x;
        m.emplace(str,x);
      }else if(c==1){
        cin >> str;
        auto range = m.equal_range(str);
        for(auto it = range.first;it != range.second;++it){
          cout << it->second << endl;
        }
      }else if(c==2){
        cin >> str;
        m.erase(str);
      }else if(c==3){
        cin >> l >> r;
        auto itrl = m.lower_bound(l);
        auto itrr = m.upper_bound(r);
        for(auto i=itrl;i!=itrr;i++){
          cout << (*i).first << " " << (*i).second << endl;
        }
      }
    }
}
