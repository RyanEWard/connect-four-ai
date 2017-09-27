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
    if human_player == 1:
        print("Player 1 selected. You are going first. Your board marker is 'X'.")
    else:
        print("Player 2 selected. You are going second. Your board marker is 'O'.")
    print()
    return human_player


def initial_instructions():
    print("")
    print("Connect Four game.")
    human_player = player_selection()

b = Board(6, 7)

initial_instructions()

b.place_marker(1, 0)
b.place_marker(1, 0)
b.place_marker(1, 6)

b.place_marker(2, 2)
b.place_marker(2, 4)

b.pretty_print()

print(minimax(b, 2, 6))
