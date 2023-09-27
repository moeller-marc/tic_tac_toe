#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define SIZE 9

typedef struct
{
    int *board;
    int player;
    int *empty_cells;
    best_move best_move;
} minimax_node;

typedef struct
{
    int *board;
    int score;
} best_move;

void print_board(int *board);
void set_board(int *board);
int is_terminal(int *board);
void get_all_emty_cells(int *board, int *empty_cells);
void minimax_with_pruning(minimax_node *node);

int main(int argc, char const *argv[])
{
    int board[SIZE];
    print_board(board);
    board[1] = 2;
    board[4] = 2;
    board[7] = 2;

    if (is_terminal(board) == 1)
        printf("1 won\n");
    else if (is_terminal(board) == 2)
        printf("2 won\n");
    else if (is_terminal(board) == 3)
        printf("draw");
    else
        printf("still playing\n");

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

void get_all_emty_cells(int *board, int *empty_cells)
{
    int j = 0;
    for (int i = 1; i < SIZE + 1; i++)
    {
        if (board[i] == 0)
        {
            empty_cells[j] = i;
            j += 1;
        }
    }
    empty_cells[0] = j;
}

void minimax_with_pruning(minimax_node *node)
{
    if (is_terminal(->board) != 0)
    {
        if (is_terminal(node->board) == 1)
        {
            best_move best_move = {*board, 1};
            node->best_move = best_move;
        }
        else if (is_terminal(node->board) == 2)
        {
            node->best_move = -1;
        }
        else if (is_terminal(node->board) == 3)
        {
            node->best_move = 0;
        }
    }
}