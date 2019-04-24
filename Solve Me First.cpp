#include<iostream>
using namespace std;
int function(int a, int b){
    return(a+b);
}
int main(){
  int x,y;
  cin >> x >> y;
  cout << function(x,y);
  return 0;
}

