#include<iostream>
using namespace std;

void CanWe(string s1, string s2, int n){
    int l1,l2;
    l1 = s1.length();
    l2 = s2.length();
    int count=0;
    for(int i=0;i<l2;i++){
        if(s1[i]==s2[i]){
            count++;
        }else{
            break;
        }
    }
    int same=0;
    for(int i=0;i<l2;i++){
        if(s2[0]==s2[i]){
            same++;
        }
    }
    //cout <<"same=" <<same<<" l2="<<l2 << endl;
    int L1,L2;
    L1=l1-count;
    L2=l2-count;
    int ans = L1+L2;
    //cout << L1+L2 << endl;
    
    if(ans <=n){
        cout << "Yes" << endl; 
    }
    else if(same==l2){
        cout << "Yes" << endl;
    }
    else if(ans == 0){
        cout << "Yes" << endl;
    }
    else if(ans > n){
        cout << "No" << endl;
    }
}

int main(){
    int n;
    string s1,s2;
    cin >> s1 >> s2 >> n;
    CanWe(s1,s2,n);
    return 0;
}

