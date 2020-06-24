#include <stdio.h>
#include <cs50.h>

int main(void){
    int a = 1;
    printf("%p", &a);
    char* s = "abc";
    printf("%s", s);
}