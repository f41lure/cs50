#include <stdio.h>
#include <cs50.h>

int main(void)
{
    while (true)
    {
        char choice = get_char();
        if (choice == '+')
        {
            int nums = get_int();
            int sum = 0;
            for (int i = 0; i < nums; i++)
            {
                int n = get_int();
                sum = sum + n;
            }
            printf("%d", sum);
            break;
        }
        else if (choice == '-')
        {
            printf("First Number: ");
            int n1 = get_int();
            printf("Second Number: ");
            int n2 = get_int();
            printf("%d\n", n1 - n2);
            break;
        }
        else if (choice == 'x')
        {
            
        }
    }
}