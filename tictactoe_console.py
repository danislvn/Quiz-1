def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    win_conditions = [
        [0, 1, 2],  
        [3, 4, 5],  
        [6, 7, 8],  
        [0, 3, 6],  
        [1, 4, 7],  
        [2, 5, 8],  
        [0, 4, 8],  
        [2, 4, 6],  
    ]
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_board_full(board):
    return all(cell in ["X", "O"] for cell in board)


def get_player_move(board, player_mark):
    while True:
        try:
            move = int(input(f"  Player {player_mark}, choose a position (1-9): "))
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
            elif board[move - 1] in ["X", "O"]:
                print("That spot is already taken! TRY ANOTHER ONE.")
            else:
                return move - 1  # Convert to 0-based index
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    print("=" * 40)
    print("  Welcome to Tic Tac Toe! :))))))))))))")
    print("=" * 40)
    print("\nPositions are numbered like this (use these to pick your move):")
    print("\n 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 \n")

    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    current = 0  

    while True:
        print_board(board)
        player = players[current]

        index = get_player_move(board, player)
        board[index] = player

        if check_winner(board, player):
            print_board(board)
            print(f" Player {player} wins! Congratulations!\n")
            break

        #Check for draw
        if is_board_full(board):
            print_board(board)
            print(" It's a draw! Well played both!\n")
            break

        #Switch to the other player
        current = 1 - current  

    again = input("Play again? YES / NO: ").strip().lower()
    if again == "YES":
        play_game()
    else:
        print("\nThanks for playing! PAALAM \n")

play_game()

