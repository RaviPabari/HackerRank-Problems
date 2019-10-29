//Hackerrank Problem Solving Q: Easy : Flipping Bits Problem 40 points
//IDK why this was for 40 points !

#include<iostream>
using namespace std;

void FlippingBit(unsigned int arr[],int n){
    for(int i=0;i<n;i++){
        cout << 4294967295 - arr[i] << endl;
    }
}

int main(){
    int n;
    cin >> n;
    unsigned int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    FlippingBit(arr, n);
    return 0;
}
