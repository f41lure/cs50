#include <stdio.h>

int main(void)
{
    int n = 100;         // Makes a pointer that will store location of int
    int *m = &n;
    int z = 20;
    int *k = &z;
    int *t = NULL;
    printf("N: %i, Z: %i\n", n, z);
    t = k;
    k = m;
    printf("N: %i, Z: %i\n", n, z);
}