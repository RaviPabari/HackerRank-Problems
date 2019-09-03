//Hackerrank Problem Solving Q: Easy : Sock Merchant Problem 10 points
#include<iostream>
#include<algorithm>
using namespace std;
int array(int arr[],int n){
    int i,pair=0;
    sort(arr,arr+n);
    for(i=0;i<n;i++){
        if(arr[i]==arr[i+1]){
            pair++;
            i++;
        }
    }
    return pair;
}

int main(){
    int i,n;
    cin >> n;
    int arr[n];
    for(i-0;i<n;i++){
        cin >> arr[i];
    }
    cout << array(arr,n) << endl;
    return 0;
}
