//Hackerrank Problem Solving Q: Easy : Bon Apetit problem 10 points
//Try ur logic first dont look for answer directly :)


#include<iostream>
using namespace std;
void splitter(int bil[], int n1, int k1,int x){
	int total = 0;
	for(int i=0;i<n1;i++){
		total += bil[i];
	}
	int allergic_split;
	allergic_split = (total - bil[k1])/2;
	total = total/2;
	if(allergic_split == x) cout<<"Bon Appetit" << endl;
	else cout << (x - allergic_split) << endl;
}
int main(){
	
	int n,k,charged;
	cin >> n >> k ;
	int bill[n];

	for(int i=0;i<n;i++){
		cin >> bill[i];
	}
	cin >> charged;
	
	splitter(bill,n,k,charged);
	return 0;
}
