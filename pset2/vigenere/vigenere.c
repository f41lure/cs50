#import <stdio.h>
#import <cs50.h>
#import <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{   
    if (argc != 2) 
    {
        printf("Usage: vigenere <key>\n");
        return 1;
    }
    
    string key = argv[1];
    for (int k = 0; k < strlen(key); k++)
    {
        tolower(key[k]);
        if (!isalpha(key[k]))
        {   
            printf("Usage: vigenere <key>\n");
            return 1;
        }
    }
    
    printf("\nString: ");
    string s = get_string();
    printf("ciphertext: ");
    
    for (int i = 0, j = 0, l = strlen(s); i < l; i++)
    {
        tolower(s[i]);
        j = j % strlen(key);
        if (isupper(s[i]))                      // If current letter in the plaintext is uppercase...
        {
            if (isupper(key[j]))
            {
                int a = (int) key[j] - 65;           // Handles ciphertext
                int b = ((int) s[i]) - 65;           // Handles plaintext
                int c = (a + b) % 26 + 65;  
                printf("%c", (char) c);
                j++;
            }
            
            else if (islower(s[i]))
            {
                int a = (int) key[j] - 97;
                int b = ((int) s[i]) - 65;
                int c = (a + b) % 26 + 65;
                printf("%c", (char) c);
                j++;
            }
        }
        
        else if (islower(s[i]))                 // If current letter in the plaintext is lowercase...
        {
            if (isupper(key[j]))
                {
                    int a = (int) key[j] - 97;       // Handles ciphertext
                    int b = ((int) s[i]) - 65;       // Handles plaintext
                    int c = (a + b) % 26 + 97;
                    printf("%c", (char) c);
                    j++;
                }
            
            else if (islower(s[i]))
                {
                    int a = (int) key[j] - 97;
                    int b = ((int) s[i]) - 97;
                    int c = (a + b) % 26 + 97;
                    printf("%c", (char) c);
                    j++;
                }
        }
            
        else if (isalpha(s[i]) == false)        // Print numbers and symbols as they are
        {
            printf("%c", s[i]);
        }

        
    }
    printf("\n");
    return 0;
}