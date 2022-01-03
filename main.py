from TicTacToeBoard import TicTacToeBoard as TTTBoard

# Set up game
board = TTTBoard()
print("Welcome to Tic Tac Toe! Player 1 will be X's, and player 2 will be O's.")
board.display_board()
turn_count = 0

# Alternate turns until game is over
while not board.check_winner():
    if turn_count % 2 == 0:
        board.play_turn("X")
        turn_count += 1
    else:
        board.play_turn("O")
        turn_count += 1
