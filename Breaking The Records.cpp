//Hackerrank Problem Solving Q: Easy : Breaking The Records Problem 10 points
//Name of this problem reminds me of song "Breaking The Habits" by LinkinPark ♥
//Try ur logic first dont look for answer directly :)
#include<iostream>
using namespace std;
int main(){
	int n;
	cin >> n;
	int a[n],i;
	int max, min,MAX=0,MIN=0;
	for(i=0;i<n;i++){
		cin >> a[i];
	}
	min = a[0];
	max = a[0];
	for(i=1;i<n;i++){		
		if(a[i]<min){
	        	min=a[i];
			MIN++;		
		}else if(a[i]>max){
			max=a[i];
			MAX++;
		}
	}
	cout << MAX << " "<< MIN;
	return 0;		
}
