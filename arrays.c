#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>

int main(void)
{
    for (int i = 65; i < 90; i++)
    {
        printf("%c is %i\n", (char) i, i);
    }
}