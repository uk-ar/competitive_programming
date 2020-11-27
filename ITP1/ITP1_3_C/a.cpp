#include <bits/stdc++.h>
using namespace std;

int main(){
    int x=1,y=1;
    while(x!=0 || y!=0){
        cin >> x >> y;
        if(x>y){
            swap(x,y);
        }
        if(x==0 && y==0){
            exit(0);
        }
        cout << x << " " << y << endl;
    }
}
