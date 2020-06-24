/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */

#include <cs50.h>
#include <string.h>
#include <stdio.h>

#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool binsearch(int value, int values[], int n)
{
    int lowbound = 0;
    int ubound = n - 1;
    while (lowbound <= ubound)
    {
        int midp = (lowbound + ubound) / 2;
        if (value == values[midp])
        {
            return true;
        }
        else if (value < values[midp])
        {
            ubound = midp - 1;
        }
        else
        {
            lowbound = midp + 1;
        }
    }
    return false;
}


/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int min = i;
        for (int j = i + 1; j < n; j++)
        {
            if (values[j] < values[min])
            {
                min = j;
            }
            int temp = values[min];
            values[min] = values[i];
            values[i] = temp;
        }
    }
    return;
}
bool search(int value, int values[], int n)
{
    return binsearch(value, values, n);
}


