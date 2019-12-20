//Hackerrank Problem Solving : Easy : 15 points : Problem Hurdle Race
#include<iostream>
#include<algorithm>
#include<cstdlib>

using namespace std;

void hurdle(int a[],int n,int height){
    int count =0;
    for (int i=0;i<n;i++){
        if(a[i]>height){
            
        }
    }
    cout << count << endl;
}
bool comp(int a, int b) 
{ 
    return (a < b); 
} 

int main(){
    int n;
    cin >> n;
    int height;
    cin >> height;
    int arr[n];
    for (int i=0;i<n;i++){
        cin >> arr[i];
    }
    //hurdle(arr,n,height);
    int *li;
    li = std::max_element(arr,arr+n,comp);
    int ans = (*li - height);
    if(ans > 0){
        cout << ans << endl;
    }else{
        cout << 0 << endl;
    }
    return 0;
}
