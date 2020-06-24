#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
int main(void) 
{
    printf("Key: ");
    string key = get_string();
    printf("\nString: ");
    string s = get_string();
    for (int i = 0; i < strlen(s); i++)
    {
        if (isupper(s[i]))
        {
            int a = (int) key[i % strlen(key)] - 65;
            int b = ((int) s[i]);
            int c = (a + b - 65) % 26 + 65;
            printf("%c", (char) c);
        }
        else if (islower(s[i]))
        {
            int a = (int) key[i % strlen(key)] - 97;
            int b = ((int) s[i]);
            int c = (a + b - 97) % 26 + 97;
            printf("%c", (char) c); 
        }
        else if (isalpha(s[i]) == false)        // Program will still increase key even if a space is present
        {
            printf("%c", s[i]);
        }
    }
}