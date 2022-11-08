
from logic import make_empty_board, get_winner, board_update, other_player

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'X'
    round = 0

    while winner == None and round <= 9:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        print('Current Player:', player)
        for row in board:
            print(row)
        # TODO: Input a move from the player.
        while True:
            row = int(input("Place at which row: "))
            col = int(input("Place at which column: "))
        # TODO: Update the board.
            if(board_update(board, row, col, player)):
                break
        # TODO: Update who's turn it is.
        round = round + 1
        winner = get_winner(board)
        player = other_player(player)
    
    # Report the final result
    if winner == None:
        print("Dead Heat!")
    else:
        print('Game Stopped! The winner is', winner)