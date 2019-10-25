//Hackerrank Problem Solving Q: Easy : #Staircase Problem 10 points
//Try ur logic first dont look for answer directly :)

#include<iostream>
using namespace std;
int main(){
	int n,i,j;
	cin >> n;
	for(i=0;i<n;i++){
		for(j=1;j<n-i;j++){
			cout << " " ;
		}
		for(int k =0; k<=i; k++){
			cout << "#";
		}
		cout << endl;
	}
	return 0;
}

