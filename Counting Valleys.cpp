//Hackerrank Problem Solving Q: Easy : Counting Valleys Problem 15 points

#include<iostream>
using namespace std;
int main(){
    int n,i;
    cin >> n;
    string str;
    cin >> str;
    int count=0,valleys=0;
    for(i=0;i<n;i++){
        if(str[i]=='U'){
            count++;
        }
        if(str[i]=='D'){
            count--;
        }
        if(count==0 && str[i]=='U'){ // why we took U?
              valleys++;             // because we are only asked to find valleys not hills so  'and' condtion with 'U'
      }
    }
    cout << valleys << endl;
    return 0; 
}
