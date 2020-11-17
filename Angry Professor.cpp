//Hackerrank Problem Solving : Easy : Angry Professor Problem 20 Points
//Code By Ravi Pabari
#include<iostream>
using namespace std;
#define for(i,n) for(int i=0;i<n;i++)

int main(){
    int testcase;
    cin >> testcase;
    while(testcase != 0){
        int n,k;
        cin >> n >> k;
        int arr[n];
        for(i,n){
            cin >> arr[i];
        }
        
        int count=0;
        for(i,n){
            if(arr[i] <=0 ){
                count++;
            }
        }
        if(count >= k){
            cout << "NO" << endl;
        }else{
            cout << "YES" << endl;
        }
        testcase--;
    }
    return 0;
}
