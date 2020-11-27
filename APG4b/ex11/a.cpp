//#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
  long long N,A;
  cin >> N >> A;
  for(int i=0; i<N; i++){
    string op;
    int B;
    cin >> op >> B;
    if(op=="+"){
      A = A + B;
    }else if(op=="-"){
      A = A - B;
    }else if(op=="*"){
      A = A * B;
    }else if(op=="/" && B!=0){
      A = A / B;
    }else{
      cout << "error" << endl;
      break;
    }
    cout << i+1 << ":" << A << endl;
  }
}
