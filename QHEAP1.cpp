#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int arr[1000000];
int curr=-1;

int mindex(int left,int right){
    return arr[left]<arr[right]?left:right;
}

int find_index(int y){
    for(int i=0;i<=curr;i++)
        if(arr[i]==y)
        return i;
        
        return -1;
}

void heapifyUp(int index){
    int parent=index/2;
    if(arr[parent]<arr[index] || (parent==index))
        return;
    else{
        int temp=arr[parent];
        arr[parent]=arr[index];
        arr[index]=temp;
        heapifyUp(parent);
    }
return;
}

void heapifyDown(int index){
    int left=2*index;
    int right=2*index+1;
    if(left<=curr && right<=curr){
        if(arr[index]<arr[left] && arr[index]<arr[right])
            return;
        else{
            int min_index=mindex(left,right);
            int temp=arr[min_index];
            arr[min_index]=arr[index];
            arr[index]=temp;
            heapifyDown(min_index);
        }
    }
}

void insert(int y){
    arr[++curr]=y;
    heapifyUp(curr);
    /*for(int i=0;i<=curr;i++)
        printf("%d\t",arr[i]);
    printf("\n");*/
}

void delet(int y){
int index=find_index(y);
    //printf("found index:%d\t",index);
    if(index!=-1){
    arr[index]=arr[curr--];
        heapifyDown(index);
    }
    /*for(int i=0;i<=curr;i++)
        printf("%d\t",arr[i]);
    printf("\n");
*/
}


int main() {

    int n,x,y;
    scanf("%d",&n);
    
    while(n--){
        scanf("%d",&x);
        if(x==1){
            scanf("%d",&y);
            insert(y);
        }
        if(x==2){
            scanf("%d",&y);
            delet(y);
        }
        if(x==3){
            if(curr>=0)
                printf("%d\n",arr[0]);
        }
    }
    
    return 0;
}

