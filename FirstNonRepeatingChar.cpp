#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void nonRepeating(string s){
	bool flag = true;
    int arr[26]={0};
    for (int i=0;i<s.length();i++){
        arr[s[i]-'a']++; 
    }
    for (int i=0;i<s.length() ;i++){
        if (arr[s[i]-'a']==1){
            cout << s[i] << endl;
            flag = false;
            break;
        }
    }
    if(flag==true){
    	cout << -1 << endl;	
	}
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    string s;
    int n;
    cin >> n;
    while(n--){
        scanf(" %[^\n]s",s); 
        nonRepeating(s);
    }
    return 0;
}

