from board import Board
from minimax import minimax

b = Board(6, 7)

b.place_marker(1, 0)
b.place_marker(1, 6)

b.place_marker(2, 2)
b.place_marker(2, 4)

b.pretty_print()

print(minimax(b, 2, 5))
