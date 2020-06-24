#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <math.h>
int main(void)
{
    int item = get_int();
    int list1[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(list1) / sizeof(int);
    int lowbound = 0;
    int ubound = n - 1;
    bool found = false;
    while (found == false && lowbound <= ubound)
    {
        int midp = (lowbound + ubound) / 2;
        if (list1[midp] > item)
        {
            ubound = midp - 1;
        }
        else if (item == midp)
        {
            found = true;
        }
        else
        {
            lowbound = midp + 1;
        }
    }
    if (found == true)
    {
        printf("TRUE");
    }
    else if (found == false)
    {
        printf("FALSE");
    }
}