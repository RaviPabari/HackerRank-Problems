//Hackerrank Problem Solving Q: Easy : Apple And Orange Problem 10 points
#include<iostream>
#include<string.h>
using namespace std;
int main(){
    string str;
    long long n,count =0,rem, rept,remCount=0;
    int i;
    cin >> str >> n;
    long long length = str.length();
    rem = n%length;
    rept = n/length;
    for(i=0;i<length;i++){
        if(str[i]=='a'){
            count++;
        }
        if(str[i]=='a' && i <rem){
            remCount++;
        }
    }
    cout << (count*rept)+remCount << endl;
    return 0;
}
