#include<iostream>
using namespace std;
void insort(int A[],int n){
    int x,i,j;
    for(i=1;i<n;i++){
        j=i-1;
        x=A[i];
        while(j>-1 && A[j]>x){
            A[j+1]=A[j];
            j=j-1;
        }
        A[j+1]=x;
        for(int k=0;k<n;k++){
            cout << A[k] << " " ;
        }
        cout << endl;
    }
}

int main(){
    int n;
    cin >> n;
    int A[n];
    for(int i=0;i<n;i++){
        cin >> A[i] ;
    }
    insort(A,n);
    return 0;
}
