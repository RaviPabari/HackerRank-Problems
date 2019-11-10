//Hackerrank Problem Solving : Easy : The Hurdle Race Problem 15 Points
#include<iostream>
#include<algorithm>
using namespace std;
#define for(i,n) for(i=0;i<n;i++)

int maxx(int A[],int n){
    int i,max=0;
    for(i,n){
        if(max < A[i]){
            max = A[i];
        }
    }
    return max;
}
int main(){
    int n,m,i;
    cin >> n >> m;
    int arr[n];
    for(i,n){
        cin >> arr[i];
    }
    int max;
    max = maxx(arr,n);
    //cout << max << endl;
    if(max <= m){
        cout << 0 << endl;
    }
    if(max > m){
        cout << max - m << endl;
    }
    return 0;
}
