#include<iostream>
#include<stdlib.h>
using namespace std;
void swap(int *x, int *y){
    int temp=*x;
    *x=*y;
    *y=temp;
}

    int BubbleSort(int A[], int n){
        int i,j,flag=0,shift=0;
        
        for(i=0;i<n;i++){
            flag=0;
            for(j=0;j<n-i-1;j++){
                if(A[j]>A[j+1]){
                    swap(&A[j] , &A[j+1]);
                    flag=1;
                    shift++;
                }
            }
            if(flag==0){
                break;
            }
        }
        return shift;
    }

int main(){
    int n;
    cin >> n;
    int A[n];
    for(int i=0;i<n;i++){
        cin >> A[i];
    }
    cout << BubbleSort(A,n);
    return 0;
}
