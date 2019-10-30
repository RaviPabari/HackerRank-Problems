//Hackerrank Problem Solving Q : easy : Ice Cream Parlor Problem 30 Points

#include<iostream>
using namespace std;

void Parlor(){
    int n1,m,i;
        cin >> m;
        cin >> n1;
        int arr[n1];
        for(i=0;i<n1;i++){
            cin >> arr[i];
        }
        int j;
        for(i=0;i<n1;i++){
            for(j=1 && j!=i ;j<n1 ;j++){ 
                if((arr[i]+arr[j])==m &&(i!=j)){
                    cout << i+1 << " " << j+1 << endl;
                    return;                 //I have used return here because break; was not breaking me out of loop 
                }  
            }
        }
}

int main(){
    int n;
    cin >>n;
    while(n!=0){
        Parlor();
        n--;
    }
    return 0;
}
