//Hackerrank Problem Solving Q: Easy : Apple And Orange Problem 10 points
#include<iostream>
using namespace std;

void countingValleys(int n,string str){
	int i,count=0,valleys=0;
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
}

int main(){
    int n;
    cin >> n;
    string str;
    cin >> str;
    countingValleys(n,str);
    return 0; 
}
