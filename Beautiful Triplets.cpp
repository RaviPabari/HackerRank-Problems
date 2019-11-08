//Hackerrank Problem Solving : Easy : Beautiful Triplets Problem 20 Points
#include<iostream>
using namespace std;
int main(){
    int n,d;
    int i,j,k,p,q;
    cin >> n >> d;
    int arr[n];
    for(p=0;p<n;p++){
        cin >> arr[p];
    }
    int MainCount=0;
    for(p=0;p<n;p++){
        i=arr[p];
        j=i+d;
        k=j+d;
        int count = 0;
        for(q=0;q<n;q++){
            if(arr[q]==i){
                count++;
            }
            if(arr[q]==j){
                count ++;
            }
            if(arr[q]==k){
                count++;
            }
        }
        if(count==3){
            MainCount++;
        }
    }
    cout << MainCount << endl;
    return 0; 
}

