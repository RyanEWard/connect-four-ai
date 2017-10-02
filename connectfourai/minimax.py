import timeit

def switch(player):
    return 2 if player == 1 else 1


def minimax_helper(board, player, max_depth, current_depth):
    current_board_winner = board.winning_player()

    # search depth is reached or game is over
    if current_depth >= max_depth or len(board.open_columns()) == 0 or current_board_winner != 0:
        if current_board_winner != 0 and current_board_winner == 1:
            return 1.0 / current_depth, 1
        elif current_board_winner == 2:
            return -1.0 / current_depth, 1
        else:
            return 0, 1

    nodes_eval = 0
    # recur over possible player 1 moves, the maximizing player
    if player == 1:
        best_value = -float("inf")
        best_move = -1
        for move in board.open_columns():
            board.place_marker(player, move)
            value, nodes_eval_move = minimax_helper(board, switch(player), max_depth, current_depth + 1)
            board.remove_marker(move)

            nodes_eval += nodes_eval_move
            if value > best_value:
                best_value = value
                best_move = move
        if current_depth == 1:
            return best_move, best_value, nodes_eval
        return best_value, nodes_eval

    # recur over possible player 2 moves, the minimizing player
    else:
        best_value = float("inf")
        best_move = -1
        for move in board.open_columns():
            board.place_marker(player, move)
            value, nodes_eval_move = minimax_helper(board, switch(player), max_depth, current_depth + 1)
            board.remove_marker(move)

            nodes_eval += nodes_eval_move
            if value < best_value:
                best_value = value
                best_move = move
        if current_depth == 1:
            return best_move, best_value, nodes_eval
        return best_value, nodes_eval


def minimax(board, player, max_depth):
    time_start = timeit.default_timer()
    (move, value, nodes_evaluated) = minimax_helper(board, player, max_depth, 1)
    return move, value, nodes_evaluated, (timeit.default_timer() - time_start)
