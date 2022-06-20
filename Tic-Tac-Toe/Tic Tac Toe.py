# -------------Global Variables----------------

game_is_still_on = True

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Display a Tic Tac Toe board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Who won ? or tie?
winner = None

# Who's turn it is?
current_player = "X"


def play_game():
    # Display initial board
    display_board()

    # While the game is still going
    while game_is_still_on:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # game has ended
    if winner == "X" or winner == "O":
        print(winner + " won ")
    elif winner == None:
        print("Tie")


def handle_turn(player):
    print(player + " 's turn. ")
    position = int(input("Choose a position form 1-9: "))
    position = position - 1

    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    # setup global variable
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonal
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_rows():
    # setup global variable
    global game_is_still_on

    # equal to each other but not equal to "-"
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_is_still_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # setup global variable
    global game_is_still_on

    # equal to each other but not equal to "-"
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_is_still_on = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]

    return


def check_diagonals():
    # setup global variable
    global game_is_still_on

    # equal to each other but not equal to "-"
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    if diag_1 or diag_2:
        game_is_still_on = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return


def check_if_tie():
    global game_is_still_on

    if "-" not in board:
        game_is_still_on = False

    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = 'X'
    return


play_game()