#include<iostream>
using namespace std;
int main(){
	char s;
	int h,m,ss;
	scanf("%d:%d:%d%c",&h,&m,&ss,&s);
	if(s == 'P'){
		if(h!=12) h+=12;
	}else if(h==12){
		h=0;
	}
	printf("%02d:%02d:%02d",h,m,ss);
	return 0;
}
