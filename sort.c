
#include <stdio.h>
#include <string.h>
int main(void)
{
    int list1[5] = {16, 5, 8, 6, 10};
    int n = sizeof(list1) / sizeof(int);
    int swaps = n - 1;
    while (swaps != -1)
    {
        for (int i = 0; i < n - 1; i++)
        {
            int a = i + 1;
            if (list1[i] > list1[a])
            {
                int temp = list1[a];
                list1[a] = list1[i];
                list1[i] = temp;
                swaps -= 1;
            }
        }
    }
    for (int j = 0; j < n; j++)
    {
        printf("%d, ", list1[j]);
    }
}