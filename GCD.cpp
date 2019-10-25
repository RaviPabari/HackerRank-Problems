#include <iostream>
using namespace std;
int main(){
    int a,b,c,num1,num2;
    cout<<"enter two numbers"<<endl;
    cin>>num1>>num2;
    if(num1>num2){
        a=num1;
        b=num2;
    }
    else{
        a=num2;
        b=num1;

    }
    while(b!=0){
        c=a%b;
        a=b;
        b=c;
    }
    cout<<a<<endl;
    return 0;

}
