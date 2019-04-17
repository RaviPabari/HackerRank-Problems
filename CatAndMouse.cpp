#include<iostream>
#include<cstdlib>
using namespace std;

void CatsAndMouse(int x, int y, int z){
	x = abs(x-z);
	y = abs(y-z);
	if(x>y){
		cout << "Cat B" << endl;
	}else if(x==y){
		cout << "Mouse C" << endl;
	}else{
		cout << "Cat A" << endl;
	}
}
int main(){		
	int q;
	int a,b,c;
	cin >>q;
	for(int i=0;i<q;i++){
		cin >> a >> b >> c;
		CatsAndMouse(a,b,c);
	}

	return 0;
}

