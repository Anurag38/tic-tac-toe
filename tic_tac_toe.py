# global variables


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = 'X'

game_still_going = True

winner = None

# The main function which allows you to play
def play_game():

    # display the initial board
    display_board()

    while game_still_going:

        #handle the player's turn
        handle_turn(current_player)

        #check if anyone has won
        check_if_game_over(current_player)

        #if game not over
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")

    elif winner == None:
        print("Tie.")


#Function for displaying the board
def display_board():

    print(board[0] + "  |  " + board[1] + "  |  " + board[2] + "    1 | 2 | 3")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5] + "    4 | 5 | 6")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8] + "    7 | 8 | 9")
    print("\n")


#Function that puts in the player's marker in the board
def handle_turn(current_player):

    position = 0

    print("Current player : " + current_player)
    position = input("Choose a position (1-9) : ")

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:

        print("Invalid positon. Go again")
        position = input("Choose a position (1-9) : ")

    position = int(position) - 1

    check_position(position)

    display_board()



#Function to check if the position entered is already occupied or not
def check_position(position):

    if board[position] == "-":
        board[position] = current_player

    else:
        print("Position is already occupied. Go again")
        # position = int(input("Choose a position (1-9) : ")) - 1
        # check_position(position)
        handle_turn(current_player)



#Function to check if the game is over or not
def check_if_game_over(current_player):

    check_for_winner(current_player)

    check_for_tie()



#Function to check if the player has won or not
def check_for_winner(current_player):

    global game_still_going
    global winner

    #Checking for winner in rows
    if ((board[0] == current_player and board[1] == current_player and board[2] == current_player ) or
        (board[3] == current_player and board[4] == current_player and board[5] == current_player ) or
        (board[6] == current_player and board[7] == current_player and board[8] == current_player )):

        winner = current_player
        game_still_going = False

    #Checking columns for winner
    elif ((board[0] == current_player and board[3] == current_player and board[6] == current_player ) or
          (board[1] == current_player and board[4] == current_player and board[7] == current_player ) or
          (board[2] == current_player and board[5] == current_player and board[8] == current_player )):

        winner = current_player
        game_still_going = False

    #Checking in diagonal for winner
    elif ((board[0] == current_player and board[4] == current_player and board[8] == current_player) or
          (board[2] == current_player and board[4] == current_player and board[6] == current_player)):

        winner = current_player
        game_still_going = False

    else:
        winner = None



def check_for_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False
        return True

    else:
        return False


def flip_player():

    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"

play_game()
