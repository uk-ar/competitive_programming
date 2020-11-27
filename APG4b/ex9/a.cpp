//#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
  int x,a,b;
  cin >> x >> a >> b;
  x += 1;
  cout << x << endl;
  x *= a+b;
  cout << x << endl;
  x *= x;
  cout << x << endl;
  x -= 1;
  cout << x << endl;
}
