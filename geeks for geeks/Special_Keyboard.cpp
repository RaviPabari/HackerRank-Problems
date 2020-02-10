#include<iostream>
using namespace std;

int keyboard(int n, int a[]){
	int max = 0;
	int tempMax = 0;
	int mul = 2;
	if(n<=6){
		return n;
	}
	if(n>75){
		return -1;
	}
		for(int i=n-3;i>=0;i--){
			if(a[i]==-1){
				a[i] = keyboard(i,a);
			}
			tempMax = mul*a[i];
			
			if(tempMax > max){
				max = tempMax;
			}
			mul+=1;
		}
		return max;	    
}

int main(){
	int arr[75]={-1};
	int n;
	cin >> n;
	for(int i=0;i<75;i++){
		arr[i]=-1;
	}
	while(n--){
		int x ;
		cin >> x;
		cout << keyboard(x,arr) << endl;
	}
	return 0;
}
