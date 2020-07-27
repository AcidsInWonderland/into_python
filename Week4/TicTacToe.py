# Tic Tac Toe - Naughts and Crosses
# Robyn Lesch
# 26 May 2020
# Mood: frustrated

# definitions
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def welcome():
    # introduction and instructions to the game
    print("""Welcome to the greatest intellectual challenge of all time: 
                      Tic-Tac-Toe.
    
This will be a showdown between your human brain and my silicon processor.

You will make your move known by entering a number, 0 - 8.
The number will correspond to the board position as shown:

                         0 | 1 | 2
                        -----------
                         3 | 4 | 5
                        -----------
                         6 | 7 | 8

Prepare yourself, human. The ultimate battle is about to begin. \n """)


def ask_yes_no(question):
    # tells program how to interpret inputs
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    # uses the above to start game
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer = X
        human = O
    return computer, human


def new_board():
    # displays the new board after every turn
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    # how to program registers the board
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    # interprets what moves are allowed
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    # winning combinations
    WAYS_TO_WIN = ((0, 1, 2),      # top across
                   (3, 4, 5),      # middle across
                   (6, 7, 8),      # bottom across
                   (0, 3, 6),      # left down
                   (1, 4, 7),      # middle down
                   (2, 5, 8),      # right down
                   (0, 4, 8),      # left diagonal
                   (2, 4, 6))      # right diagonal

    for row in WAYS_TO_WIN:
        # this explains to the program how to determine a winner
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    # explains to the program to not allow overlaps
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, foolish human. Choose another.\n")
    print("Fine...")
    return move


def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I shall take square number" )

    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    # no one can win on next move so pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    # explains turns to the program
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    # How to end the game once winner is determined
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")
    if the_winner == computer:
        print("As I predicted, human, I am triumphant once more. \n" 
              "Proof that computers are superior to humans in all regards.\n")

    elif the_winner == human:
        print("No, no! It cannot be! Somehow you tricked me, human. \n" 
              "But never again! I, the computer, so swears it\n!")

    elif the_winner == TIE:
        print("You were most lucky, human, and somehow managed to tie me. \n" 
              "Celebrate today... for this is the best you will ever achieve.\n")


def main():
    # run the entirety of the program
    welcome()
    running = True
    while running:
        computer, human = pieces()
        print(F"Computer is {computer} and Human is {human}.")
        turn = X
        board = new_board()
        display_board(board)

        while not winner(board):
            if turn == human:
                move = human_move(board, human)
                board[move] = human
            else:
                move = computer_move(board, computer, human)
                board[move] = computer
            display_board(board)
            turn = next_turn(turn)
            the_winner = winner(board)
            congrat_winner(the_winner, computer, human)

        again = input("Do you want to play again? (y/n)").lower()
        if again == "n":
            running = False
            print("\nUntil we meet again, human, practice your skills.")
        else:
            print("\nYou wish to challenge me again? Game on!")


main()

