#include <iostream>
using namespace std;
int main(){
    int d,c,a,e,f=0;
    cout<<"enter the two numbers"<<endl;
    cin>>d>>c;
    a=d;
    e=c;
    while(d!=c){
        if(d>c){
            d=d-c;
        }
        else{
            c=c-d;
        }
    }
        f=(a*e)/d;
        cout<<f<<endl;
        return 0;
}
