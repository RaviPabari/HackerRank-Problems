#include<iostream>
using namespace std;

void location(int arr[],int n,int key){
    int i;
    for(i=0;i<n;i++){
        if(arr[i]==key){
            cout << i << endl;
            break;
        }
    }
}

int main(){
    int key,n;
    cin >> key >> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i] ;
    }
    location(arr,n,key);
    return 0;
}
