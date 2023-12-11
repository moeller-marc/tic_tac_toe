
def main():
    board = [0,0,0,0,0,0,0,0,0]
    # board = [0,0,0,0,0,0,1,1,1]
    # board = [0,0,1,0,0,1,0,0,1]
    # board = [1,0,0,0,1,0,0,0,1]
    # board = [0,0,1,0,1,0,1,0,0]

    print("Welcome to Tic Tac Toe!")
    print("Player 1 will be X and Player 2 will be O.")
    print("To play, enter the row and column of the space you want to play in.")
    print("The top left space is row 1, column 1.")
    print("The bottom right space is row 3, column 3.")
    print("Have fun!")

    def terminal_test(board):
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] != 0:
                return True
            elif board[3*i] == board[3*i+1] == board[3*i+2] != 0:
                return True

        if board[0] == board[4] == board[8] != 0:
            return True
        elif board[2] == board[4] == board[6] != 0:
            return True

        return False
    


if __name__ == "__main__":
    main()