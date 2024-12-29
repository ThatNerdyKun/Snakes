def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row = int(input(f"Enter the row for {player}: "))
        col = int(input(f"Enter the column for {player}: "))
        if board[row][col] != " ":
            print("Invalid move, try again.")
            continue
        board[row][col] = player
        if check_win(board, player):
            print_board(board)
            print(f"{player} wins!")
            break
        if all(all(row != " " for row in board_row) for board_row in board):
            print_board(board)
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"

tic_tac_toe()