#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
int main(int argc, string argv[]) 
{
    if (argc != 2)
    {
        return 1;
    }
    string key = argv[1];

    printf("String: ");
    string s = get_string();
    printf("Ciphertext: ");
    for (int i = 0; i < strlen(s); i++)
    {
        toupper(key[i]);
        if (isupper(s[i]))
        {
            int a = (int) argv[1][(i % strlen(argv[1]))] - 65;
            int b = ((int) s[i]);
            int c = (a + b - 65) % 26 + 65;
            printf("%c", (char) c);
        }
        else if (islower(s[i]))
        {
            int a = (int) argv[1][(i % strlen(argv[1]))] - 65;
            int b = ((int) s[i]);
            int c = (a + b - 97) % 26 + 97;
            printf("%c", (char) c); 
        }
        else if (isalpha(s[i]) == false)
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
    return 0;
}