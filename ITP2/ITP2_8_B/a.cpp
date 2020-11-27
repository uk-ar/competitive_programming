#include <bits/stdc++.h>
using namespace std;

int main(){
    int q;
    map <string,int>m;
    cin >> q;
    for(int i=0;i<q;i++){
      int c,x;
      string str;
      cin >> c >> str;
      if(c==0){
        cin >> x;
        m[str] = x;
      }else if(c==1){
        if(m.count(str)==1){
          cout << m[str] << endl;
        }else{
          cout << 0 << endl;
        }
      }else if(c==2){
        m.erase(str);
      }
    }
}
