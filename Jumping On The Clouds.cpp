#include<iostream>
using namespace std;
int badal(int arr[],int n){
    int badalCount = 0;
    for(int i=0;i<n;i++){
        if(i>=(n-1)){
            return badalCount;
        }
        if(arr[i+2]==0){
            badalCount++;
            i++;
        }else{
            if(arr[i+1]==0){
                badalCount++;
            }
        }
    }
    return badalCount;
}

int main(){
    int n;
    cin >> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    cout << badal(arr,n) << endl;
    return 0;
}

