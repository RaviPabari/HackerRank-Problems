#include<iostream>
#include<stdlib.h>
using namespace std;
void swap(int *x, int *y){
	int temp=*x;
	*x=*y;
	*y=temp;
}

	void BubbleSort(int A[], int n){
		int i,j,flag=0;
		
		for(i=0;i<n;i++){
			flag=0;
			for(j=0;j<n-i-1;j++){
				if(A[j]>A[j+1]){
					swap(&A[j] , &A[j+1]);
					flag=1;
				}
			}
			if(flag==0){
				break;
			}
		}
	}

int main(){
	int A[] = {11,13,6,23,443,44,54,656,65,98}, n=10,i;
	BubbleSort(A,n);
	
	for(i=0;i<n;i++){
		cout << A[i] << " " ;
	}
	return 0;
}
