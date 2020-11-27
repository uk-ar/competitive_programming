#include <bits/stdc++.h>
using namespace std;

class SetOfStacks {
private:
  vector <vector<int>>s;
  int lim;
public:
  /** Initialize Your Data Structure Here */
  SetOfStacks(int threshold) : s({}),lim(threshold){
    if(threshold<1){
      throw "ex";
    }
  }

  void push(int x) {

    //for(auto i=s.begin();i<s.end();i++){
    for(vector <int> &v:s){
      //for(int i=0;i<s.size();i++){
      //vector <int>v = s.at(i);
      if(v.size()<lim){
        //s.at(i).push_back(x);
        v.push_back(x);
        // cout << "push ";
        // for (auto i:v){
        //   cout << i << " ";
        // }
        // cout << endl;
        return;
      }
    }
    s.push_back({x});
  }

  int pop() {
    return popAt(s.size()-1);
  }

  int popAt(int index) {//0 oriented
    if(s.size()<=index or s.at(index).empty()){
      throw "ex";
    }
    // cout << "pop " << index << " ";
    // for (auto i:s.at(index)){
    //   cout << i << " ";
    // }
    // cout << endl;
    int ret = s.at(index).back();
    s.at(index).pop_back();
    if(s.at(index).empty()){
      s.erase(s.begin()+index);
    }
    return ret;
  }
};

int main(){
  SetOfStacks setOfStacks = SetOfStacks(2);
  setOfStacks.push(4);
  setOfStacks.push(5);
  cout << setOfStacks.pop() << endl;
  setOfStacks.push(3);
  setOfStacks.push(8);
  setOfStacks.push(2);
  cout << setOfStacks.popAt(0) << endl;
  setOfStacks.push(10);
  cout << setOfStacks.popAt(0) << endl;
  cout << setOfStacks.pop() << endl;
}
