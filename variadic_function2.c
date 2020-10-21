/*      Find minimum using variadic */
#include <stdio.h>
#include <stdarg.h>         //header file for standard arguments

int min(int , ...);        //declaration of variadic function with atleast one fixed ardument and then followed bt ellipses
int max(int , ...);   
int main()
{
    printf("Min = %d\n", min(2, 13,45));
    printf("Min = %d\n", min(3, 3,45, 65));
    printf("Min = %d\n", min(4, 13,45, 6, 87));

    printf("Max = %d\n", max(2, 13,45));
    printf("Max = %d\n", max(3, 3,45, 65));
    printf("Max = %d\n", max(4, 13,45, 6, 87));
}

int min(int count, ...)
{
    va_list ap;
    va_start(ap, count);
    int min = va_arg(ap, int);
    for(int i =1; i<count; i++)
    {
        int temp = va_arg(ap, int);
        if(min > temp)
        {
            min = temp;
        }
    }
    va_end(ap);
    return min;
}
int max(int count, ...)
{
    va_list ap;
    va_start(ap, count);
    int max = va_arg(ap, int);
    for(int i =1; i<count; i++)
    {
        int temp = va_arg(ap, int);
        if(max < temp)
        {
            max = temp;
        }
    }
    va_end(ap);
    return max;
}
