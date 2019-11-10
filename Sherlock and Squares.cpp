#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int testcase;
    cin >> testcase;
    while(testcase != 0){
        unsigned int a,b;
        cin >> a >> b;
        cout << floor(sqrt(b))-ceil(sqrt(a)) + 1 << endl;
        testcase--;
    }
    return 0;
}
