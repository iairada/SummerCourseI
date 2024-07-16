import random

# ...

def main():
    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    while not game_over:
        # Ask for Player 1 Input
        if turn == 0:
            col = int(input("Player 1 Make your Selection (0-6):"))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                    print("PLAYER 1 WINS!")
                    game_over = True

        # Computer Player 2
        else:
            col = random.randint(0, COLUMN_COUNT-1)

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    print("PLAYER 2 WINS!")
                    game_over = True

        print_board(board)

        turn += 1
        turn = turn % 2

if __name__ == "__main__":
    main()
