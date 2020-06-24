#include <stdio.h>
#include <cs50.h>

int main(void)
{
    printf("Please enter your name: ");
    name = get_string();
    printf("\nWelcome, %s", name);
}