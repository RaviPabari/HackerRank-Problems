//Hackerrank Problem Solving Q: Easy : Lonley Integer Problem 20 points
//so ezzzz

#include<iostream>
#include<algorithm>
using namespace std;

int lonley(int A[],int n){
    int count=0,i;
    sort(A,A+n);
    if(n==1){
        return A[0];
    }
    for(i=0;i<n;i+=2){
        if(A[i]==A[i+1]){
            count ++;
            if(count == n/2){
                return A[n-1];
                break;
            }
        }else{
            return A[i];
            break;
        }
    }
    return -1;
}

int main(){
    int n,i;
    cin >> n;
    int A[n];
    for(i=0;i<n;i++){
        cin >> A[i];
    }
    cout <<lonley(A,n) << endl;
    return 0;
}
