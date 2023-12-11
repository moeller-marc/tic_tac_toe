typedef struct{
    int board[9];
    int score;
} move;

// an implementation of the min max algoritm with alpha beta pruning
minmax_alpha_beta_pruning(board, player, alpha, beta){

    if is_terminal() != 0{
        return move = {board, is_terminal()}
    }

    else{
       int moves[] 
    }
}


// minmax_alpha_beta_pruning(board, player, alpha, beta){
//     if is_terminal() != 0{
//         return move = {board, is_terminal()}
//     }

//     else{
//         int moves[SIZE * SIZE];
//         get_all_moves(moves)

//     }
// }


// minmax_alpha_beta_pruning(board, player, alpha, beta){

// if is_terminal() != 0{
//     return is_terminal(), board
// }

// else{
//     moves = get_all_moves() // the first number of this array should be the length of the array
//     for array length{
//         minmax()
//     }
//     sort array 
//     if player = min{
//         return smallest value
//     }
//     else{
//         return biggest value
//     }
// }
// }