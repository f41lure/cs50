#import <stdio.h>
#import <cs50.h>
#import <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{   
    if (argc != 2) 
    {
        printf("Usage: vigenere <key>\n");
        printf("Wrong number of parameters, string or negative number supplied. Aborting.\n");
        
        // stop executing program
        return 1;
    }
    
    string key = argv[1];
    for(int k = 0; k < strlen(key); k++)
    {
        if (!isalpha(key[k]))
        {   
            printf("Usage: vigenere <key>\n");
            printf("Non-alphabetic characters given. Aborting.\n");
            return 1;
        }
        tolower(key[k]);
    }
    
    printf("\nString: ");
    string s = get_string();
    printf("ciphertext: ");
    
    for (int i = 0, j = 0, l = strlen(s); i < l; i++)
    {
        
        j = j % strlen(key);
        if (isupper(s[i]))
        {
            int a = (int) key[j] - 65 ;
            int b = ((int) s[i]);
            int c = (a + b - 65 + 6) % 26 + 65;
            printf("%c", (char) c);
            j++;
        }
        else if (islower(s[i]))
        {
            int a = (int) key[j] - 97;
            int b = ((int) s[i]);
            int c = (a + b - 97) % 26 + 97;
            printf("%c", (char) c);
            j++;
        }
        else if (isalpha(s[i]) == false)        // Program will still increase key even if a space is present
        {
            printf("%c", s[i]);
            
        }
    } 
    printf("\n");
    return 0;
}