//Hackerrank Problem Solving Q: Easy : Birthday Chocolate 10 points
#include <iostream>
using namespace std;

int main() {    
    int n ,m ,d ,sum,i,count=0,j;
    cin >> n;
    int s[n];
    for(i=0;i<n;i++){
        cin >> s[i];
    }
    cin >> d >> m;
    for(i=0;i<n;i++){
        sum =0;
        for(j=i;j<i+m;j++){
            sum = sum + s[j];
        }
        if(sum == d){
            count ++;
        }
    }
    std::cout <<  count << std::endl;
    return 0;
}
