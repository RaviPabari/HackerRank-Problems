#include <stdio.h>
#include <math.h>
int main()
{
    int a ;
    scanf("%d", &a);
    float f = sqrt(a);
    printf("Square root = %f\n", f);
    f = pow(a, 0.5);
    printf("Square root = %f\n", f);

}