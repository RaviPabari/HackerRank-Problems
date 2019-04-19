//Hackerrank Problem Solving Q: Easy : Viral Advertising Problem 15 points
//so ezzzz
//Try ur logic first dont look for answer directly :)
#include<iostream>
using namespace std;
int main(){
	int n;
	cin >>n;
	int x=5,y,z,result=0;
	for(int i=0;i<n;i++){
		y=x/2;
		z=y*3;
		result += y;
		x=z;
	}
	cout << result;
	return 0;
}
