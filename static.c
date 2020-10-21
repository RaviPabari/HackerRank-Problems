/*  Prog to understand use of Static varible    */
#include<stdio.h>
void fun(void)
{
    int a = 5;
    static int b = 6;
    printf("Value of a = %d\tvalue to b = %d\n", a,b);
    a++;
    b++;
    return ;
}
int main()
{
    fun();
    fun();
    fun();
    return 0;
}