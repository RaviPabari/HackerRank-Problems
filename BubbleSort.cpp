#include<iostream>
using namespace std;

void Swap(int *x,int *y){
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void BubbleSort(int arr[],int n){
    int i,j,sc=0;
    for(i=0;i<n;i++){
        for(j=0;j<n-i-1;j++){
            if(arr[j]>arr[j+1]){
                Swap(&arr[j],&arr[j+1]);
                sc++;
            }
        }
    }
    cout <<"Array is sorted in " << sc << " swaps." << endl;
    cout <<"First Element: " << arr[0] << endl;
    cout <<"Last Element: " << arr[n-1] << endl;
}
int main(){
    int n,i;
    cin >>n;
    int arr[n];
    for(i=0;i<n;i++){
        cin >> arr[i];
    }
    BubbleSort(arr,n);
    return 0;
}
