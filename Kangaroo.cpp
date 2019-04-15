//Hackerrank Problem Solving Q: Easy : Kangaroo Problem 10 points
//here you have to think about 2 cases one is kang1 is behind kang1
//another is kang2 is behind kang1 and their jump distance
//Try ur logic first dont look for answer directly :)

#include<iostream>
using namespace std;

int main(){
	int x1,v1,x2,v2;
	cin >> x1 >> v1 >> x2 >> v2 ;
	
	if((x1>x2) && (v1>v2)){
		cout << "NO" << endl;
	}else if((x2>x1) && (v2>v1)){
		cout << "NO" << endl;
	}
	
	else{
		if(x1<x2){
			while(x1<x2){
				x1 += v1;
				x2 += v2;
			}
		}else{
			while(x2<x1){
				x1 += v1;
				x2 += v2;
			}
		}
		
		if(x1==x2){
			cout << "YES" << endl;
		}else{
			cout << "NO" << endl;
		}
	}
	return 0;
}
