#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 9

void print_board(int *board);
void set_board(int *board);

int main(int argc, char const *argv[])
{
    int board[SIZE];
    set_board(board);
    print_board(board);
    return 0;
}

void print_board(int *board)
{
    int o = 1;
    for (int i = 0; i < SIZE; i++)
    {
        printf("%d|", board[i]);
        if (o % 3 == 0){
            printf("\n");
        }
        o += 1;
    }
    printf("\n");


}

void set_board(int *board){
    for (int i = 0; i < SIZE; i++)
    {
        board[i] = 0;
    }
    
}