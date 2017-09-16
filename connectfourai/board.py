class Board:
    def __init__(self, rows, columns):
        self.board = [[0 for _ in range(columns)] for _ in range(rows)]

    def placeMarker(self, player, column):
        for row in reversed(range(len(self.board))):
            if self.board[row][column] == 0:
                self.board[row][column] = player
                return

    def openColumns(self):
        return [c for c in range(len(self.board[0])) if self.board[0][c] == 0]

    def winningPlayer(self):
        for four_in_a_row in self.getRows() + self.getColumns() + self.getDiagonals():
            if four_in_a_row[0] != 0 and len(set(four_in_a_row)) == 1:
                return four_in_a_row[0]
        return 0

    def getRows(self):
        return [row[c:c + 4] for row in self.board for c in range(len(row) - 3)]

    def getColumns(self):
        return [list(col[r:r + 4]) for col in zip(*self.board) for r in range(len(col) - 3)]

    def getDiagonals(self):
        down_right_diagonals = [[self.board[r + dif][c + dif] for dif in range(4)]
                                for r in range(len(self.board) - 3)
                                for c in range(len(self.board[0]) - 3)]

        up_right_diagonals = [[self.board[r - dif][c + dif] for dif in range(4)]
                              for r in range(3, len(self.board))
                              for c in range(len(self.board[0]) - 3)]

        return down_right_diagonals + up_right_diagonals

    def prettyPrint(self):
        row_string = ""
        for r in range(len(self.board)):
            for c in range(len(self.board[r]) - 1):
                row_string += self.getLabel(r, c) + "|"
            row_string += self.getLabel(r, len(self.board[r]) - 1)
            print(row_string)
            row_string = ""

        column_labels = ""
        divider = ""
        for c in range(len(self.board[0]) - 1):
            column_labels += str(c + 1) + "|"
            divider += "--"
        column_labels += str(len(self.board[0]))
        divider += "-"

        print(divider)
        print(column_labels)
        print()

    def getLabel(self, r, c):
        if self.board[r][c] == 0:
            return " "
        elif self.board[r][c] == 1:
            return "X"
        else:
            return "O"


b = Board(6, 7)
b.prettyPrint()

b.placeMarker(1, 0)

b.prettyPrint()

b.placeMarker(2, 0)

b.placeMarker(1, 0)
b.placeMarker(2, 0)

b.placeMarker(1, 0)
b.placeMarker(2, 0)

b.placeMarker(1, 2)
b.placeMarker(2, 2)

b.placeMarker(1, 2)
b.placeMarker(2, 2)

b.placeMarker(1, 1)
b.placeMarker(2, 6)

b.placeMarker(1, 1)
b.placeMarker(2, 1)

b.placeMarker(1, 6)
b.placeMarker(2, 3)

b.prettyPrint()

print(b.winningPlayer())
