#include<iostream>
using namespace std;
int F[30];

int mfib(int n){
                    //memoization technique takes O(n)  | the simple recursive technique takes O(2^n)
    if(n<=1){
        F[n]=n;
        return n;
    }else{
        if(F[n-2]==-1){
            F[n-2]=mfib(n-2);
        }
        if(F[n-1]==-1){
            F[n-1]=mfib(n-1);
        }
        F[n]=F[n-2]+F[n-1];
        return F[n-2]+F[n-1];
    }
}

int main(){
    int n;
    cin >> n;
    for(int i=0;i<30;i++){
        F[i]=-1;
    }
    cout << mfib(n) << endl;
    return 0;
}
