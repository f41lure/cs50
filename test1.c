#include <stdio.h>
#include <cs50.h>

int main(void)
{
    while (true)
    {
        char c = get_char();
        if (c == 'y')
        {
            printf("Yes\n");
            break;
        }
        else if (c == 'n' || c == 'N')
        {
            printf("No\n");
            break;
        }
        else 
        {
            printf("Error\n");
            continue;
        }
    }    
}