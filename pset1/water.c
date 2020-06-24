#include <stdio.h>
#include <cs50.h>

int main(void)
{ 
    printf("How many minutes were you in the shower: ");
    int min = get_int();
    int ounces = min * 192;
    printf("%i\n", ounces / 16);   
}