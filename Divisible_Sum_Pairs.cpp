#include<iostream>
using namespace std;
int main(){
    int n,k,sum=0,count=0,a,b;
    cin >> n;
    int arr[n],i,j;
    cin >>k;
    for(i=0;i<n;i++){
        cin >> arr[i] ;
    }
    for(i=0;i<n;i++){
        a = arr[i];
        for(j=0;j<n && j!=i;j++){
           b= arr[j];
           sum = a + b;
            if(sum%k==0){
                count ++;
            }
        }
    }
    cout << count << endl;

}
