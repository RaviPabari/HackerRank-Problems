//Hackerrank Problem Solving : Easy : Alternating Characters problem 20 points

#include<iostream>
using namespace std;

void Delete(string s){
    int i,count=0;
    int n = s.length();
    for(i=0;i<n-1;i++){
        if(s[i]==s[i+1]){
            count++;
        }
    }
    cout << count << endl;
}
int main(){
    int n;
    cin  >> n;
    string s;
    while(n!=0){
        cin >> s;
        Delete(s);
        n--;
    }
    return 0;
}
