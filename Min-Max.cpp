
//Hackerrank problem solving question named :Easy : Min-Max 10 points 
//can also use #include <algorithm> for using sort element
#include<iostream>
using namespace std;
int main(){
int x=5;
long long arr[5];
int i,j;
for(int i=0;i<5;i++){
	cin >> arr[i];
}
for(i=0;i<x-1;i++){			//using bubblesort	
	for(j=0;j<x-i-1;j++){	
		if(arr[j]>arr[j+1]){
			swap(arr[j],arr[j+1]);
		}
	}
}
long long sum = 0;
for(i=0;i<5;i++){
	sum += arr[i];
}
cout << sum-arr[4] << " " << sum -arr[0] << endl;
return 0;
}
