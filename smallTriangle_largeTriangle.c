/* Implement Quick Sort */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define SCALE_DOWN 10
struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

float areaCal(triangle *tri)
{
    float area;
    float p;
    p = (float)(tri->a + tri->b + tri->c )/2;
    float p1 = p - tri->a;
    float p2 = p - tri->b;
    float p3 = p - tri->c;
    area = (float)(p*p1*p2*p3)/SCALE_DOWN;
    return area;
}

void swap(triangle *a, triangle *b)
{
    triangle temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int partision(triangle *tr, int low, int high)
{
    int i = low - 1;
    triangle pivot = tr[high];
    for(int j = low; j <= high; j++)
    {
        if(areaCal(&tr[j]) < areaCal(&pivot))
        {
            i++;
            swap(&tr[i], &tr[j]);
        }
    }
    i++;
    swap(&tr[i], &tr[high]);
    return i;
}

void quickSort(triangle *tr, int low, int high)
{
    if(low < high)
    {
        int pivot = partision(tr, low, high);
        quickSort(tr, low, pivot - 1);
        quickSort(tr, pivot + 1, high);
        
    }
}
void sort_by_area(triangle* tr, int n) {
	
    quickSort(tr, 0, n-1);
} 
void printArea(triangle *tr, int n)
{
    for(int i = 0; i<n; i++)
    {
        printf("Triangle = %d, Area = %f \n",i, areaCal(&tr[i]));
    }
    printf("\n");
}
int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
    printf("\n");
    printArea(tr, n);
	sort_by_area(tr, n);
    //printArea(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}

    free(tr);
	return 0;
}