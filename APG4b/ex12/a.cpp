//#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
  string S;
  cin >> S;
  int re = 1;
  for(char e : S){
    if(e == '+'){
      re += 1;
    }else if(e == '-'){
      re -= 1;
    }
  }
  cout << re << endl;
}
