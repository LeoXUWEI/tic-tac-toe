
from logic import Game

if __name__ == '__main__':
    game = Game()
    board = game.make_empty_board()
    winner = None
    player = 'X'
    round = 0
    
    game_mode = input("Please input your game mode (PvP or PvE):")

    while winner == None and round <= 9:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        print('Current Player:', player)
        for row in board:
            print(row)
        # TODO: Input a move from the player.
        while True:
            if game_mode == 'PvP' or player == 'X':
                row = int(input("Place at which row: "))
                col = int(input("Place at which column: "))
            elif game_mode == 'PvE':
                row, col = game.get_random_position(board)

        # TODO: Update the board.
            if(game.board_update(board, row, col, player)):
                break
        # TODO: Update who's turn it is.
        round = round + 1
        winner = game.get_winner(board)
        player = game.other_player(player)
    
    # Report the final result
    if winner == None:
        print("Dead Heat!")
    else:
        print('Game Stopped! The winner is', winner)