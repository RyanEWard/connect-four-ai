from board import Board
from minimax import minimax


def player_selection():
    human_player = 0
    while human_player == 0:
        try:
            human_player = int(input("Select player ('1' or '2'):"))
            if human_player != 1 and human_player != 2:
                raise ValueError
        except ValueError:
            print("Invalid player selection.")
            human_player = 0
    print()
    print("Player " + str(human_player) + " selected. You are going first. Your board marker is '"
          + Board.get_label(human_player) + "'.")
    print()
    return human_player


def print_initial_instructions():
    print()
    print("Connect Four game.")


def print_game_over(board, human_player):
    board.pretty_print()
    if board.winning_player() != 0:
        print("Game over. Connect four for player " + str(board.winning_player()) + "!")
        if board.winning_player() == human_player:
            print("You won.")
        else:
            print("You lost.")
    else:
        print("Game over. Tie.")


def human_player_turn(board, human_player):
    print("It is your turn. Select a column to drop your marker on.")
    print()
    board.pretty_print()

    move = -1  # cannot use 0 since that is a valid column move
    while move == -1:
        try:
            move = int(input("Select a column to drop your marker on:"))
            move = move - 1  # subtracting one for zero-index columns
            if move not in board.open_columns():
                raise ValueError
        except ValueError:
            print("Invalid column selection.")
            move = -1

    board.place_marker(human_player, move)
    print("Column " + str(move + 1) + " selected.")
    print()


def computer_player_turn(board, computer_player):
    print("It is the computer's turn. Computer is making a move.")
    print()
    board.pretty_print()

    (move, value, nodes_evaluated, time_taken) = minimax(board, computer_player, 7)

    board.place_marker(computer_player, move)

    print(str(nodes_evaluated) + " game states evaluated in " + str(time_taken) + " seconds.")
    print("Computer selected column " + str(move + 1) + " for its marker.")
    print()


def main():
    b = Board(6, 7)
    print_initial_instructions()
    human_player = player_selection()
    computer_player = 1 if human_player == 2 else 2

    current_player = 1

    while b.winning_player() == 0 and len(b.open_columns()) != 0:
        if current_player == human_player:
            human_player_turn(b, human_player)
        else:
            computer_player_turn(b, computer_player)
        current_player = 1 if current_player == 2 else 2

    print_game_over(b, human_player)


main()
