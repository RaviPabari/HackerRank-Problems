#include <stdio.h>
int isLeap(int y)
{
    if((y/100==0) && (y/400==0))
    {
        return 1;
    }
    else if(y/100!=0 && (y/4==0))
    {
        return 1;
    }
    else
    {
        return 0;
    }
    

}
int check_date( int d, int m, int y)
{
    int valid = 1;
    if( y>2050 || y< 1850)
    {
        valid = 0;
    }
    else if (m<1 || m>12)
    {
        valid = 0;
    }
    else 
    {
        if(d<1)
        {
            valid = 0;
        }
        else if (m == 2)
        {
            if(d>28)
            {
                valid = 0;
            }
            else if (isLeap(y))
            {
                if(d>29)
                    valid = 0;
            }
        }
        else if ( m ==4 || m ==6 || m ==9 || m ==11)
        {
            if(d>30)
                valid = 0;
            
        }
        else 
        {
            if(d > 31)
                valid = 0;
        }
    }
    return valid;
}
int main()
{
    int d,m,y;
    printf("Enter a valid date : ");
    scanf ("%d/%d/%d", &d, &m, &y);
    if(check_date(d,m,y) == 1)
    {
        printf("Valid\n");
    }
    else{
        printf("Invalid \n");
    }
}