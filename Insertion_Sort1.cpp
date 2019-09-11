#include<bits/stdc++.h>
using namespace std;

void insertionSort(vector <int>  ar) {
    int small = 0;
    for(int i = 0; i < ar.size()-1;i++){
        if(ar[i] > ar[i+1]){
            small = ar[i+1];
            int j = i;
            while(ar[j] > small){
                ar[j+1] = ar[j];
                j--;
                for(int k = 0; k < ar.size(); k++)cout << ar[k] << " ";
                cout << endl;
            }
            ar[j+1] = small;
        }
    }
    for(int i = 0; i < ar.size(); i++)cout << ar[i] << " ";
    cout << endl;
}
int main(void) {

   vector <int>  _ar;
   int _ar_size;
   cin >> _ar_size;
   for(int _ar_i=0; _ar_i<_ar_size; _ar_i++) {
      int _ar_tmp;
      cin >> _ar_tmp;
      _ar.push_back(_ar_tmp);
   }
   insertionSort(_ar);
   return 0;
}
