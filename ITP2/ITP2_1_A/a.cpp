#include <bits/stdc++.h>
using namespace std;

void permutationWithoutDups(set<char>&se,vector<string>&ret,string &str){
  if(se.empty()){
    ret.push_back(string(str));
    return;
  }
  ret.push_back("aaa");
  for(char c:se){
    cout << str << " " << c << endl;
    str += c;
    se.erase(c);
    permutationWithoutDups(se,ret,str);
    se.emplace(c);
    str.pop_back();
  }
  return;
}
vector <string> permutationWithoutDups(string s){
  if(s.empty()){
    return vector<string>(0);
  }
  set<char> se(s.begin(),s.end());
  vector<string>ret(0);
  string t = "";
  permutationWithoutDups(se,ret,t);
  return ret;
}
// int main(){
//   for(string s: permutationWithoutDups("abc")){
//     cout << s << endl;
//   }
// }
struct TreeNode
{
    int data;
    TreeNode *left;
	  TreeNode *right;
    TreeNode() { data =0; left = NULL; right = NULL; }
    TreeNode(int x) { data = x; left = NULL; right = NULL; }
    TreeNode(int x, TreeNode *l, TreeNode *r) { data = x; left = l; right = r; }
};
void printvec(string str, vector<int>&ret){
  cout << str << endl;
  //for(vector<int>v:ret){
    for(int a:ret){
      cout << a << " ";
    }
    cout << endl;
    //}
}

void merge(vector<int>&rl,vector<int>&rr,vector<int>&temp,vector<vector<int>>&ret){
  //printvec("rl",rl);
  //printvec("rr",rr);
  //printvec("temp",temp);
  //printvec("ret",ret);
  if(rl.empty() and rr.empty()){
    ret.push_back(vector<int>(temp));//copy
    return;
  }
  if(!rl.empty()){//[1][2][3]
    temp.push_back(rl.back());//[1,2][2][3]
    rl.pop_back();//[1,2][][3]
    merge(rl,rr,temp,ret);
    rl.push_back(temp.back());//[1,2][2][3]
    temp.pop_back();//[1][2][3]
  }
  if(!rr.empty()){//[1,2][][3]//[1][2][3]
    temp.push_back(rr.back());//[1,2,3][][3]//[1,3][2][3]
    rr.pop_back();//[1,2,3][][]//[1,3][2][]
    merge(rl,rr,temp,ret);
    rr.push_back(temp.back());//[1,2,3][][3]
    temp.pop_back();//[1,2][][3]
  }
  return;
}
void printvv(string str, vector<vector<int>>&ret){
  cout << str << endl;
  for(vector<int>v:ret){
    for(int a:v){
      cout << a << " ";
    }
    cout << endl;
  }
}
vector<vector<int>> sequencesOfBST(TreeNode *root){
  //vector<vector<int>>ret(1,vector<int>(0));
  vector<vector<int>>ret(0);
  if(!root){
    return ret;
  }
  if(!root->left and !root->right){
    ret.push_back({root->data});
    return ret;
  }
  vector<vector<int>>left = sequencesOfBST(root->left);//[2][123,132]
  vector<vector<int>>right= sequencesOfBST(root->right);//[3][456,465]
  if(!root->left){
    for(vector<int> &v:right){
      reverse(v.begin(),v.end());
      v.push_back(root->data);
      reverse(v.begin(),v.end());
      //printvec("left",v);
    }
    return right;
  }
  if(!root->right){
    for(vector<int> &v:left){
      reverse(v.begin(),v.end());
      v.push_back(root->data);
      reverse(v.begin(),v.end());
      //printvec("right",v);
    }
    return left;
  }
  // cout << root->data << endl;
  // printvv("left",left);
  // printvv("right",right);
  for(vector<int>&rl:left){
    reverse(rl.begin(),rl.end());
  }
  for(vector<int>&rr:right){
    reverse(rr.begin(),rr.end());
  }
  for(vector<int>&rl:left){
    for(vector<int>&rr:right){
      vector<int> temp({root->data});
      merge(rl,rr,temp,ret);//[123][456][0][]
    }
  }
  return ret;
}
class BinaryTree {
public:
      struct TN
    {
        int cnt;
        int data;
        TN *left;
    	  TN *right;
        TN() { data =0; left = NULL; right = NULL; }
        TN(int x) { cnt=1; data = x; left = NULL; right = NULL; }
        TN(int x, TN *l, TN *r) { data = x; left = l; right = r; }
    };
  private:
    TN*root;
	public:
		/** Initialize Your Data Structure Here */
		BinaryTree():root(nullptr) {

		}
		TN* insert(int x,TN*node) {
			if(!node){
			  return new TN(x);
			}
			node->cnt++;
			if(node->data < x){
			  node->right = insert(x,node->right);
			}else{
			  node->left = insert(x,node->left);
			}
			return node;
		}
		void insert(int x) {
			root = insert(x,root);
		}

		bool find(int x,TN*node) {
			if(!node){
			  return false;
			}
			//cout << x << ":" << node->data << endl;
			if(node->data < x){
			  return find(x,node->right);
			}else if(node->data == x){
			  return true;
			}else{
			  return find(x,node->left);
			}
		}
		bool find(int x) {
			return find(x,root);
		}
		TN* leftMost(TN*node){
		  while(node and node->left){
		    node = node->left;
		  }
		  return node;
		}
  TN* delete_(int x,TN*node) {
    if(!node){
      return node;
    }
    node->cnt--;
    if(node->data < x){
      node->right = delete_(x,node->right);
      return node;
    }else if(node->data > x){
      node->left = delete_(x,node->left);
      return node;
    }
    if(!node->left and !node->right){
      delete node;
      return nullptr;
    }
    if(!node->left){
      TN* ret = node->right;
      delete node;
      return ret;
    }
    if(!node->right){
      TN* ret = node->left;
      delete node;
      return ret;
    }
    TN* t = leftMost(node->right);
    swap(t->data,node->data);
    node->right = delete_(x, node->right);
    return node;
  }
		void delete_(int x) {
		  if(!find(x)){
		    return;
		  }
			root = delete_(x,root);
		}
		TN* findKth(int Kth,TN* node){
		  if(!node){
		    return node;
		  }
		  int left=0;
		  if(node->left){
		    left=node->left->cnt;
		  }
		  if(Kth < left){
		    return findKth(Kth,node->left);
		  }else if(Kth==left){
		    return node;
		  }else{
		    return findKth(Kth-1-left,node->right);
		  }
		}
		TN* getRandomNode() {
		  return root;
			//return findKth(rand()%(root->cnt),root);
		}
};
/**
* Definition for a Box
* struct Box {
*    int width;
*    int height;
*	   int depth;
*    Box(int w, int h,int d) {width = w;height = h;depth =d;}
*};
*/
struct Box {
   int width;
   int height;
   int depth;
   Box(int w, int h,int d) {width = w;height = h;depth =d;}
};
bool isValid(Box &prev,Box &next){
  return (prev.width > next.width) and
         (prev.height > next.height) and
         (prev.depth  > next.depth);
}
int backtrack(vector<Box> &boxes,vector<int> &temp,unordered_set<int> &used){
  int ret=0;
  for(int e:temp){
    cout << e << " ";
    ret += boxes[e].height;
  }
  cout << endl;
  for(int i=0;i<boxes.size();i++){
    if(used.count(i)==0 and (temp.empty() or
    isValid(boxes[temp.back()],boxes[i]))){
      temp.push_back(i);
      used.emplace(i);
      ret = max(ret,backtrack(boxes,temp,used));
      used.erase(i);
      temp.pop_back();
    }
  }
  return ret;
}
int stackHeight(vector<Box> boxes){
  if(boxes.empty()){
    return 0;
  }
  vector<int>temp(0);
  unordered_set<int> used;
  return backtrack(boxes,temp,used);//[],{}
}
int smallestDifference(vector<int> a, vector<int> b){
  sort(a.begin(),a.end());
  sort(b.begin(),b.end());
  int ai = 0;
  int bi = 0;
  int m = INT_MAX;
  while(ai < a.size() and bi < b.size()){
    m = min(m,abs(a[ai]-b[bi]));
    if(ai==a.size()-1){
      bi++;
    }else if(bi==b.size()-1){
      ai++;
    }else if(abs(a[ai+1]-b[bi])<abs(a[ai]-b[bi+1])){
      ai++;
    }else{
      bi++;
    }
  }
  return m;
}
void print_match(vector<string> lines, string pattern, int context) {//
	if(lines.empty()){
    	return;
    }
    /*if(lines.size() < context){

    }*/
    //Time comp O(n):init
    //          O(1):searh
    //Space comp O(n)
    //unorderd_map<string,vector<int>> {"it":[1,4],"acessible":[5]}
/* context
0 organize =>
1 it       =>
2 and      =>
3 make     =>
4 it       =>
5 accessible =>
6 and */
// lines.size == 7
/* context
0 organize =>
1 it       =>
2 and       =>
3 make      =>
4 it        =>
5 accessible =>
6 and        =>
*/
    for(int i=0;i<lines.size();i++){//1 i==6//i==0 //i==4
    	int flag=false;
    	for(int j=i-context;j<i+context+1;j++){//i==1 j==1 0,1,2//j=0;j<3//i==1 j=0 j<3 0,1,2 //i==6 j=5,6,7 j==-2 j<3 -2,-1,0,1,2
        // j==4-2=2;j<4+2+1=7 //2,3,4,5,6//i==6 j=4,5,6
        	if(0<=j and j < lines.size()){//i = 0;context=1;j=-1;j<2 -1,0,1 flag=false//5,6//j=0,1,2
                  //line -> lines
            	if(lines[j] == pattern){/* O(pattern.size()) *//**/
                	flag=true;//i==0;j==1//i==1;j==1
                }
                //equals -> compare
            }
        }
        if(flag){
	        cout << lines[i] << endl;//orgaize//it//
        }
    }
}
vector<int>co({25,10,5,1});
unordered_map<string,int>rir;
int coins(int rest,int ind){
  //cout << rest << " " << ind << endl;
  string p = to_string(rest)+":"+to_string(ind);
  if(rir.count(p)==1){
    return rir[p];
  }
  if(rest==0){
    return 1;
  }
  if(ind>=co.size()){
    return 0;
  }
  int ret = 0;
  for(int i=0;i*co[ind]<=rest;i++){
    ret += coins(rest-i*co[ind],ind+1);
  }
  rir[p]=ret;
  return ret;
}
int coins(int n){
  return coins(n,0);
}
#include <string>

int booleanEvaluation(string ex,bool result){
  //1^0|0|1  //7
  //   ^     //7-3-1
  if(ex.empty()){
    return 0;
  }
  if(ex.size()==1){
    if(ex=="1" and result){
      return 1;
    }else if(ex=="0" and ~result){
      return 1;
    }else{
      return 0;
    }
  }
  int ret=0;//1^0|0
  for(int i=1;i<ex.size();i+=2){//1 0|0//1^0 0
    int l_t = booleanEvaluation(ex.substr(0,i),true);//1 //1
    int l_f = booleanEvaluation(ex.substr(0,i),false);//0//0
    int r_t = booleanEvaluation(ex.substr(i+1,ex.size()-1-i),true);//0//1
    int r_f = booleanEvaluation(ex.substr(i+1,ex.size()-1-i),false);//1//0
    int t_t; //total true
    int total = l_t * r_t + l_t * r_f + l_f * r_t + l_f * r_f;
    if(ex[i]=='&'){
      t_t = l_t * r_t;
    }if(ex[i]=='|'){
      t_t = total - l_f * r_f;
    }if(ex[i]=='^'){//1+0
      t_t = l_t * r_f + l_f * r_t;
    }else{
      //return -1;
    }
    if(result){
      ret += t_t;
    }else{
      ret += total-t_t;
    }
    //cout << ex.substr(0,i) << ":" << ex[i] << ":" << ex.substr(i+1,ex.size()-1-i) << ":" << ret << endl;
  }
  cout << ex << ":" << result << ":" << ret << endl;
  return ret;
}
vector<unordered_set<char>>pad({{},{},{'a','b','c'},{'d','e','f'},{'g','h','i'},{'m','n','o'},{'p','q','r','s'},{'t','u','v'},{'w','x','y'}});
vector<string> tNine(vector<string> words,string input){
  vector<string> ret(0);
  for(string word:words){
    if(word.size()!=input.size()){
      continue;
    }
    int i=0;
    while(i<word.size() and pad[input[i]-'0'].count(word[i])>0){
      cout << word[i] << i <<endl;
      i++;
    }
    if(i==word.size()){
      ret.push_back(word);
    }
  }
  return ret;
}
int main(){

  // booleanEvaluation("1&1",true);//ok
  // cout << booleanEvaluation("0",true) << endl;// 0
  // cout << booleanEvaluation("0",false) << endl;// 1
  // cout << booleanEvaluation("1",true) << endl;// 1
  // cout << booleanEvaluation("1",false) << endl;// 0
  // booleanEvaluation("0|1",true);
  //cout << coins(10);
  /*  0 organize =>
1 it       =>
2 and       =>
3 make      =>
4 it        =>
5 accessible =>
6 and        */
  //print_match(vector<string> ({"it","and","make","it","accesible","and"}), "it", 0);
  //cout << smallestDifference(vector<int>({11,77,33,44}),vector<int>({77,2,34,50}))<< endl;
  // vector<Box> boxes;
  // boxes.push_back(Box(100,100,100));
  // boxes.push_back(Box(25,25,25));
  // boxes.push_back(Box(20,5,30));
  // boxes.push_back(Box(17,4,28));
  // boxes.push_back(Box(10,10,10));
  // boxes.push_back(Box(12,12,12));
  // boxes.push_back(Box(9,9,9));
  // cout << stackHeight(boxes);
  // BinaryTree binaryTree = BinaryTree();
  // binaryTree.insert(1);
  // binaryTree.delete_(1);
  // cout << binaryTree.find(1) << endl;
  // binaryTree.insert(1);
  // BinaryTree::TN *randomNode = binaryTree.getRandomNode();
  // cout << randomNode->data << endl;

  // binaryTree.insert(1);
  // binaryTree.insert(2);
  // cout << binaryTree.find(1) << endl;
  // binaryTree.insert(3);
  // BinaryTree::TN *randomNode = binaryTree.getRandomNode();
  // cout << randomNode->data << endl;
  // cout << binaryTree.find(4) << endl;
  // binaryTree.delete_();
  // bool found = binaryTree.find(x)

  // TreeNode *root = new TreeNode(4,new TreeNode(2,NULL,new TreeNode(3)),new TreeNode(5));
  // //TreeNode *root = new TreeNode(4,new TreeNode(2),new TreeNode(5));
  // //TreeNode *root = new TreeNode(2,NULL,new TreeNode(3));
  // vector<vector<int>> ret = sequencesOfBST(root);
  // cout << "hello" << endl;
  // for(vector<int>v:ret){
  //   for(int a:v){
  //     cout << a << " ";
  //   }
  //   cout << endl;
  // }}
}
