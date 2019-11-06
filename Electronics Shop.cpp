//Hackerrank Problem Solving : Easy : Electronics Shop Problem 15 points
#include<iostream>
using namespace std;
int main(){
    int n,m,b;
    cin >> b >> n >> m;
    int A[n], B[m];

    for(int i=0;i<n;i++){
        cin >> A[i];
    }
    for(int i=0;i<m;i++){
        cin >> B[i];
    }
//so I was stuck at some cases because I was initializing the max = A[0]+B[0] or max = 0 or max =1...
//but we needed to initialize the max with -1
//so if the input were like this
//5 1 1
//4
//5
//so our program should return -1 becasue the condition for b is already violated...if we initialize max with A0B0 or 1 or anything then it will fail here
    int max=-1,temp; 
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            temp = A[i]+B[j];
            if(temp > max && temp <=b){
                max = temp;
            }
        }
    }
   //cout <<"max "<< max << " b "<< b<< endl;
    if(max > b){
        cout << -1 << endl;
    }else{
        cout << max << endl;
    }
    return 0;
}
