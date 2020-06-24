#include<stdio.h>

int main(void){
    int x = 8;
    int *ptr;
    ptr = &x;
    ptr = ptr + 4;
    printf("%p\n", ptr);
    printf("%d\n", *ptr);
}