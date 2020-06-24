#include <string.h>

void foo (char *bar)
{
   char  c[12];

   strcpy(c, bar);  // no bounds checking
}

int main (int  **argv)
{
   foo(argv[1]);

   return 0;
}