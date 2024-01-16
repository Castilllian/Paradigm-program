def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        # Проверка по горизонтали
        if all([cell == player for cell in board[i]]):
            return True
        # Проверка по вертикали
        if all([board[j][i] == player for j in range(3)]):
            return True
    # Проверка по диагоналям
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    game_over = False
    while not game_over:
        print_board(board)
        row = int(input(f"Player {players[turn]}, выберите строку (0, 1, 2): "))
        col = int(input(f"Player {players[turn]}, выберите столбец (0, 1, 2): "))
        if board[row][col] == " ":
            board[row][col] = players[turn]
            if check_winner(board, players[turn]):
                print_board(board)
                print(f"Player {players[turn]} выиграл!")
                game_over = True
            elif all([cell != " " for row in board for cell in row]):
                print_board(board)
                print("Ничья!")
                game_over = True
            turn = (turn + 1) % 2
        else:
            print("Эта клетка уже занята, выберите другую.")
            
if __name__ == "__main__":
    main()
