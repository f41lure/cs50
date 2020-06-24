/**
 * fifteen.c
 *
 * Implements Game of Fifteen (generalized to d x d).
 *
 * Usage: fifteen d
 *
 * whereby the board's dimensions are to be d x d,
 * where d must be in [DIM_MIN,DIM_MAX]
 *
 * Note that usleep is obsolete, but it offers more granularity than
 * sleep and is simpler to use than nanosleep; `man usleep` for more.
 */

#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main(void)
{
    // constants
    #define DIM_MIN 3
    #define DIM_MAX 9

    // board
    int board[DIM_MAX][DIM_MAX];

    // dimensions
    int d = 3;
    int c = 0;
    for(int i = 0; i < d; i++)
    {
        for(int j = 0; j < d; j++)
        {
            board[i][j] = d * d - c;
            printf("%i, %i, %i\n", board[i][j], i, j);
            c++;
        }
    }


}