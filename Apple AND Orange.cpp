//Hackerrank Problem Solving Q: Easy : Apple And Orange Problem 10 points
//so ezzzz
//Try ur logic first dont look for answer directly :)

#include<iostream>
using namespace std;
int main(){
	int A,O,s,t,m,n,Apl=0,Orng=0,app,org;
	
	cin>>s >> t >>A >>O >> n >> m;
	
	for(int i=0;i<n;i++){
		cin >> app;
		if(A+app>=s && A+app<=t)Apl++;
	}
	for(int i=0;i<m;i++){
		cin >>org;
		if(O+org<=t && O+org>=s)Orng++;
	}
	
	cout << Apl << endl << Orng << endl;
	return 0;
}
