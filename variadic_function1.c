/*------------------------VARIADIC FUNCTIONS-------------------------

Function with variable number of arguments.

The whole procedure is summarized in these steps-
        (i) Include the header file stdarg.h
        (ii) . The fU1!ction header should contain ellipsis to denote the variable argument list.
        (iii) Declare a variable of type va_list.
        (iv) Initialize this argument pointer using va_start, so that it points 'to the first unnamed
        (v) Use va_arg to retrieve the value of arguments.
        vi) Call the macro va_end when you have finished working with these arguments  */

#include <stdio.h>
#include <stdarg.h>         //header file for standard arguments

int sum(int , ...);        //declaration of variadic function with atleast one fixed ardument and then followed bt ellipses

int main()
{
    printf("Sum = %d\n", sum(2, 13,45));
    printf("Sum = %d\n", sum(3, 13,45, 65));
    printf("Sum = %d\n", sum(4, 13,45, 65, 87));
}

int sum(int n, ...)
{
    va_list ap;                     //va_list is a datatype for variable list which contain pointer to variable arguments (Argument Pointer)
    va_start(ap, n);                //va_start initialize 
    int sum = 0;
    for(int i =0; i<n; i++)
    {
        sum += va_arg(ap, int);     //va_arg dereference single value to type mentioned as argument and also increment ap
    }
    va_end(ap);                     //assign null to ap
    return sum;
}

