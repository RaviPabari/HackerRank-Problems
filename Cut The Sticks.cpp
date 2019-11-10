#include<iostream>
using namespace std;
#define for(i,n) for(int i=0;i<n;i++)
#define for(j,n) for(int j=0;j<n;j++)

int Min(int arr[],int n){
    int min =1000;
    for(i,n){
        if(min > arr[i] && arr[i]!=0){
            min = arr[i];
        }
    }
    return min;
}

int main(){
    int n;
    cin >> n;
    int arr[n];
    
    for(i,n){
        cin >> arr[i];
    }
    for(j,n){
        int count = 0;
        int min = Min(arr,n);
        //cout << "Min = " << min << endl;
        for(i,n){    
            if(arr[i]!=0){
                arr[i] = arr[i] - min;
                count ++;
                }
            }if(count !=0){
                cout << count << endl;
        }
    }
    return 0;
}
