#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>

int main(void)
{
    string s = get_string();
    printf("%c", toupper(s[0]));            // Prints the first initial
    for (int i = 0; i < strlen(s); i++)     // Iterate over the string
    {
        if (s[i] == ' ')                    // If the character stored in index position i a space,
        {                                   // Print the next character in uppercase.
            char c = s[i + 1];
            printf("%c", toupper(c));
        }
    }
    printf("\n");
    
}
