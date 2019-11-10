//Hackerrank Problem Solving : Easy : Sequence Equation Problem 20 points
#include<iostream>
#define for(i,n)  for(int i=1;i<=n;i++)
using namespace std;
int main(){
    int n;
    cin >> n;
    int p[n+1];
   for(i,n){
        int temp;
        cin >> temp;
        p[temp] = i;        
    }
    for(i,n){
        cout << p[p[i]] << endl;
    }
    return 0;
}
