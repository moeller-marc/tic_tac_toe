
def main():
    board = [0,0,0,0,0,0,0,0,0]
    # board = [0,0,0,0,0,0,1,1,1]
    # board = [0,0,1,0,0,1,0,0,1]
    # board = [1,0,0,0,1,0,0,0,1]
    # board = [0,0,1,0,1,0,1,0,0]

    print("Welcome to Tic Tac Toe!")
    print("Player 1 will be X and Player 2 will be O.")
    print("To play, enter the row and column of the space you want to play in.")
    print("For example, to play in the top left corner, enter 0")
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

        return False

    def who_won(board) -> int:
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] != 0 and board[i]!= 1:
                return 2
            elif board[3*i] == board[3*i+1] == board[3*i+2] != 0 and board[3*i] != 1:
                return 2

        if board[0] == board[4] == board[8] != 0 and board[4] != 1:
                return 2

        elif board[2] == board[4] == board[6] != 0 and board[4] != 1:
                return 2

        return 1
    
    def get_move(board) -> bool:
        move = input("Enter your move: ")
        move = int(move)
        if board[move] != 0 and board[move] != 2:
            board[move] = 1
            return True
        else: 
            return False
    




if __name__ == "__main__":
    main()