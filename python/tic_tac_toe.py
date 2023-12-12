import pytest
def main():
    board = [0,0,0,0,0,0,0,0,0]
    # board = [0,0,0,0,0,0,1,1,1]
    # board = [0,0,1,0,0,1,0,0,1]
    # board = [1,0,0,0,1,0,0,0,1]
    # board = [0,0,1,0,1,0,1,0,0]

    # board = [1,0,2,2,1,0,2,2,1]

    print("Welcome to Tic Tac Toe!")
    print("Player 1 will be X and Player 2 will be O.")
    print("To play, enter the row and column of the space you want to play in.")
    print("For example, to play in the top left corner, enter 0, for the bottom right corner, enter 8.")
    print("Have fun!")

    def terminal_test(board) -> bool:
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] != 0:
                return True
            elif board[3*i] == board[3*i+1] == board[3*i+2] != 0:
                return True

        if board[0] == board[4] == board[8] != 0:
            return True
        elif board[2] == board[4] == board[6] != 0:
            return True

        for i in range(9):
            if board[i] == 0:
                return False
        return True 

    def who_won(board) -> int:
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] != 0 and board[i] == 1:
                return 1
            elif board[3*i] == board[3*i+1] == board[3*i+2] != 0 and board[3*i] == 1:
                return 1

        if board[0] == board[4] == board[8] != 0 and board[4] == 1:
            return 1
        elif board[2] == board[4] == board[6] != 0 and board[4] == 1:
            return 1


        for i in range(3):
            if board[i] == board[i+3] == board[i+6] != 0 and board[i] == 2:
                return 2
            elif board[3*i] == board[3*i+1] == board[3*i+2] != 0 and board[3*i] == 2:
                return 2

        if board[0] == board[4] == board[8] != 0 and board[4] == 2:
            return 2
        elif board[2] == board[4] == board[6] != 0 and board[4] == 2:
            return 2

        else:
            return 0

    def get_move(board) -> bool:
        move = input("Enter your move: ")
        move = int(move)
        if board[move] != 0 and board[move] != 2:
            board[move] = 1
            return True
        else: 
            return False
    

    def print_board(board):
        board_copy = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

        for i in range(9):
            if board[i] == 0:
                board_copy[i] = " "
            if board[i] == 1:
                board_copy[i] = "X"
            elif board[i] == 2:
                board_copy[i] = "O"

        # the drawing section

        print('+---+---+---+')
        print('| ' + board_copy[0] + ' | ' + board_copy[1] + ' | ' + board_copy[2] + ' |')
        print('+---+---+---+')
        print('| ' + board_copy[3] + ' | ' + board_copy[4] + ' | ' + board_copy[5] + ' |')
        print('+---+---+---+')
        print('| ' + board_copy[6] + ' | ' + board_copy[7] + ' | ' + board_copy[8] + ' |')
        print('+---+---+---+')
            

    print_board(board)  


if __name__ == "__main__":
    main()