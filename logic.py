
def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    # Gain all the possible cases
    pos = []
    # Get each row
    pos.extend(board)
    # Get each colomn
    for col in range(3):
        pos.append([row[col] for row in board])
    # Get each diagonal
    pos.append([board[0][0],board[1][1],board[2][2]])
    pos.append([board[0][2],board[1][1],board[2][0]])

    # Test each case
    for case in pos:
        if (case[0] != None) and case[0]==case[1] and case[0]==case[2]:
            return case[0]
    return None

def board_update(board, row, col, player):
    # Check input legality
    if row < 1 or row > 3 or col < 1 or col > 3:
        print('Go beyond the boundaries. Try again!')
        return False
    # Check if the cell is occupied
    if board[row-1][col-1] != None:
        print('Elements already present. Try again!')
        return False
    # Assign the val and return
    board[row-1][col-1] = player
    return True

def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'X':
        return 'O'
    else:
        return 'X'