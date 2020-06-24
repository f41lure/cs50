#include <stdio.h>
#include <cs50.h>

int main(void)
{
    printf("Length: ");
    while (true)
    {
        int length = get_int();
        if (length > 2010 || length < 0)
        {
            printf("Retry: ");
            continue;
        }

        int i;
        for (i = 1; i < length + 1; i++)
        {
            char space = ' ';
            int n = length - i;
            
            int b;
            for (b = 0; b < n; b++)
            {
                printf("%c", space);
            }
            
            int c;
            for (c = 0; c < i; c++)
            {
                printf("#");
            }
            
            int d;
            for (d = 0; d < 2; d++)
            {
                printf("%c", space);
            }
            
            int e;
            for (e = 0; e < i; e++)
            {
                printf("#");
            }
            printf("\n");

        }
    
        break;
    }
}