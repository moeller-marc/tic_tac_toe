def main():
    # board = [0,0,0,0,0,0,0,0,0]
    # board = [0,0,0,0,0,0,1,1,1]
    # board = [0,0,1,0,0,1,0,0,1]
    # board = [1,0,0,0,1,0,0,0,1]
    # board = [0,0,1,0,1,0,1,0,0]

    # board = [1,0,2,0,0,0,2,2,1]
    board = [1,2,1,2,2,1,0,0,0]

    print("""Welcome to Tic Tac Toe!
Player 1 will be X and Player 2 will be O.)
To play, enter the row and column of the space you want to play in.)
For example, to play in the top left corner, enter 0, for the bottom right corner, enter 8.)
Have fun!""")

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
                return -1
            elif board[3*i] == board[3*i+1] == board[3*i+2] != 0 and board[3*i] == 2:
                return -1

        if board[0] == board[4] == board[8] != 0 and board[4] == 2:
            return -1
        elif board[2] == board[4] == board[6] != 0 and board[4] == 2:
            return -1

        else:
            return 0

    def get_move(board) -> bool:
        move = input("Enter your move: ")
        move = int(move)
        if board[move] == 0:
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
    
    def minimax(board, alpha, beta, maximizingPlayer) -> (int, int):
        if terminal_test(board):
            return who_won(board), None 
            
        if maximizingPlayer:
            board_copy = board.copy()
            maxEval = -100
            for i in range(9):
                if board_copy[i] == 0:
                    board_copy[i] = 1
                    eval = minimax(board_copy, alpha, beta, False)[0]
                    if eval > maxEval:
                        maxEval = eval
                        bestMove = i
                    board_copy[i] = 0
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return maxEval, bestMove
        else:
            board_copy = board.copy()
            minEval = 100
            for i in range(9):
                if board_copy[i] == 0:
                    board_copy[i] = 2
                    eval = minimax(board_copy, alpha, beta, True)[0]
                    if eval < minEval:
                        minEval = eval
                        bestMove = i
                    board_copy[i] = 0
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return minEval, bestMove
        


    def game():
        board = [0,0,0,0,0,0,0,0,0]
        first_move = True 
        while not terminal_test(board):
            if first_move:
                print_board(board)
                get_move(board)
                board[minimax(board, -100, 100, False)[1]] = 2
                print_board(board)
                get_move(board)
                first_move = False

            else:
                board[minimax(board, -100, 100, False)[1]] = 2
                print_board(board)
                get_move(board)

    game()
if __name__ == "__main__":
    main()
