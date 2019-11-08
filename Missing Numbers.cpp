#include<iostream>
using namespace std;
int main(){
    int n,m,temp[100000]={0},num;
    cin >> n;
    while(n!=0){
        cin >> num;
        temp[num]--;
        n--;
    }
    cin >> m;
    while(m!=0){
        cin >> num;
        temp[num]++;
        m--;
    }
    for(int i=0;i<100000;i++){
        if(temp[i]!=0){
            cout << i << " ";
        }
    }
    return 0;
}
