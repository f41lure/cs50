#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
int main(int argc, string argv[])
{   
    if (argc != 2) 
    {
        printf("Usage: ./caesar <key>\n");
        return 1;
    }
    
    
    int key = atoi(argv[1]);              // Converts char into int
    printf("\nString: ");
    string s = get_string();
    printf("ciphertext: ");
    for (int i = 0; i < strlen(s); i++)   // Iterates over plaintext
    {
        int a = (char) s[i];
        if (isupper(s[i]))                // isupper() check
        {
            int e = ((a - 65 + key) % 26) + 65;
            printf("%c", (char) e);
            continue;
        }
        else if (islower(s[i]))           // islower() check
        {
            int e = ((a - 97 + key) % 26) + 97;
            printf("%c", (char) e);
            continue;
        }
        else if (isalpha(s[i]) == false)  // isalpha() check
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
    return 0;
}