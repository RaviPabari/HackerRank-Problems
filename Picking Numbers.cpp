//Hackerrank Problem Solving :Easy : Picking Numbers Problem 20 Points

#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    int n;
    cin >> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    int max = 0;
    for(int i=0;i<n;i++){
        int sum =0;
        sum = count(arr,arr+n,arr[i])+count(arr,arr+n,arr[i]+1);
        if(sum > max){
            max = sum;
        }
    }
    cout << max << endl;
    return 0;
}
