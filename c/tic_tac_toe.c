#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define SIZE 9

void print_board(int *board);
void set_board(int *board);
int is_terminal(int *board);
void get_all_emty_cells(int *board, int *emty_cells);
void get_all_moves
int main(int argc, char const *argv[])
{
    int board[SIZE];
    set_board(board);
    print_board(board);
    board[1] = 2;
    board[4] = 2;
    board[7] = 2;

    // if (is_terminal(board) == 1)
    //     printf("1 won\n");
    // else if (is_terminal(board) == 2)
    //     printf("2 won\n");
    // else if (is_terminal(board) == 3)
    //     printf("draw");
    // else
    //     printf("still playing\n");

    int emty_cells[SIZE + 1];
    get_all_emty_cells(board, emty_cells);
    for (int i = 0; i < SIZE + 1; i++)
    {
        printf("%d ", emty_cells[i]);
    }   

    return 0;
}

void print_board(int *board)
{
    int o = 1;
    for (int i = 0; i < SIZE; i++)
    {
        printf("%d|", board[i]);
        if (o % 3 == 0)
        {
            printf("\n");
        }
        o += 1;
    }
    printf("\n");
}

void set_board(int *board)
{
    for (int i = 0; i < SIZE; i++)
    {
        board[i] = 0;
    }
}

int is_terminal(int *board)
{
    int win_states[] = {5, 3, 4};
    int fields[] = {1, 3, 4, 5, 7};
    for (int i = 0; i < 5; i++)
    {
        if (board[fields[i]] == 0)
        {
            return 0;
        }
        else
        {

            if (i == 4)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (board[i] == board[i - win_states[j]] && board[i] == board[i + win_states[j]])
                    {
                        if (board[i] == 1)
                            return 1;
                        else
                            return 2;
                    }
                }
            }
            else
            {
                if (board[fields[i]] == board[fields[i] - 3] && board[fields[i]] == board[fields[i] + 3])
                {
                    if (board[fields[i]] == 1)
                        return 1;
                    else
                        return 2;
                }
            }
        }
    }
    return 0;
}

void get_all_emty_cells(int *board, int *emty_cells){
    int counter = 0;
    for (int i = 1; i < SIZE; i++)
    {
        if (board[i] == 0)
        {
            emty_cells[i] = 1;
            counter += 1;
        }
        else
        {
            emty_cells[i] = 0;
            counter += 1;
        }
    }
    emty_cells[0] = counter;
}