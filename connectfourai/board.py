class Board:
    def __init__(self, rows, columns):
        self.board = [[0 for _ in range(columns)] for _ in range(rows)]

    def place_marker(self, player, column):
        for row in reversed(range(len(self.board))):
            if self.board[row][column] == 0:
                self.board[row][column] = player
                return

    def remove_marker(self, column):
        for row in range(len(self.board)):
            if self.board[row][column] != 0:
                self.board[row][column] = 0
                return

    def open_columns(self):
        return [c for c in range(len(self.board[0])) if self.board[0][c] == 0]

    def winning_player(self):
        for four_in_a_row in self.get_rows() + self.get_columns() + self.get_diagonals():
            if four_in_a_row[0] != 0 and len(set(four_in_a_row)) == 1:
                return four_in_a_row[0]
        return 0

    def get_rows(self):
        return [row[c:c + 4] for row in self.board for c in range(len(row) - 3)]

    def get_columns(self):
        return [list(col[r:r + 4]) for col in zip(*self.board) for r in range(len(col) - 3)]

    def get_diagonals(self):
        down_right_diagonals = [[self.board[r + dif][c + dif] for dif in range(4)]
                                for r in range(len(self.board) - 3)
                                for c in range(len(self.board[0]) - 3)]

        up_right_diagonals = [[self.board[r - dif][c + dif] for dif in range(4)]
                              for r in range(3, len(self.board))
                              for c in range(len(self.board[0]) - 3)]

        return down_right_diagonals + up_right_diagonals

    def pretty_print(self):
        row_string = ""
        for r in range(len(self.board)):
            for c in range(len(self.board[r]) - 1):
                row_string += self.get_label(r, c) + "|"
            row_string += self.get_label(r, len(self.board[r]) - 1)
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

    def get_label(self, r, c):
        if self.board[r][c] == 0:
            return " "
        elif self.board[r][c] == 1:
            return "X"
        else:
            return "O"
