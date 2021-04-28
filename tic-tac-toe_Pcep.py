import time
from random import randrange
# x[0][0],x[0][8],x[0][16],x[0][24] = "+", "+", "+", "+"
# x[4][0],x[4][8],x[4][16],x[4][24] = "+", "+", "+", "+"
# x[8][0],x[0][8],x[0][16],x[0][24] = "+", "+", "+", "+"
#I <3 git  <@:D
#######
#<@:D tele-type
def computer_speech(text):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(.004)
######
x = [["-" for i in range(26)] for d in range(13)]# build the entire board matrix
board_start = [1,2,3,4,"X",6,7,8,9]
board = board_start[:]
def display_board(board):
    for i in range(0,25,8):
        x[0][i], x[4][i], x[8][i], x[12][i]= "+" * 4
        x[1][i], x[2][i], x[3][i], x[5][i], x[6][i], x[7][i], x[9][i], x[10][i], x[11][i] = "|" * 9
    spaces = [1,3,5,7,9,11]
    for j in spaces:
        for i in range(1,8):
            x[j][i] = " "
        for i in range(9,16):
            x[j][i] =" "
        for i in range(17,24):
            x[j][i] = " "
    for i in range(25):
        if x[2][i] == "-":
            x[2][i] = " "
        if x[6][i] == "-":
            x[6][i] = " "
        if x[10][i] == "-":
            x[10][i] = " "
    #update board list and convert the result to string for computer_speech()
    x[2][4] = str(board[0])
    x[2][12] =str(board[1])
    x[2][20] =str(board[2])
    x[6][4] = str(board[3])
    x[6][12] = str(board[4])
    x[6][20] =str(board[5])
    x[10][4] = str(board[6])
    x[10][12] = str(board[7])
    x[10][20] =str(board[8])
    #Printing the board
    for j in range(13):
        for i in range(25):
            computer_speech(x[j][i])
        print()
def enter_move(board):
    _check = True
    while _check:
        try:
            player_move = int(input("#"))
            if player_move in board:
                board[player_move - 1] = "O"
                _check = False
            else:
                print("The ", player_move," square is taken")
        except ValueError:
            print("Only numbers!!\nPlease Enter a #: ")
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
def make_list_of_free_fields(board):
    if x[2][4] == str(board_start[0]):
        free_list.append((1,1))
    elif (1,1) in free_list:
        free_list.remove((1,1))
    if x[2][12] == str(board_start[1]):
        free_list.append((1,2))
    if x[2][20] == str(board_start[2]):
        free_list.append((1,3))
    if x[6][4] == str(board_start[3]):
        free_list.append((2,1))
    if x[6][12] == str(board_start[4]):
        pass #Center Square
    if x[6][20] == str(board_start[5]):
        free_list.append((2,3))
    if x[10][4] == str(board_start[6]):
        free_list.append((3,1))
    if x[10][12] == str(board_start[7]):
        free_list.append((3,2))
    if x[10][20] == str(board_start[8]):
        free_list.append((3,3))
    print("Spaces Left")
    print(free_list)
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
def victory_for(board, sign):
    if sign == "O":
        if x[2][4] == sign and x[2][12] == sign and x[2][20] == sign:
            return True
        if x[2][4] == sign and x[6][4] == sign and x[10][4] == sign:
            return True
        if x[10][4] == sign and x[10][20] == sign and x[2][20] == sign:
            return True
        if x[2][20] == sign and x[6][20] == sign and x[10][20] == sign:
            return True
                                            
    elif sign == "X":
        if x[2][4] == sign and x[2][12] == sign and x[2][20] == sign:
            return True
        if x[2][4] == sign and x[6][4] == sign and x[10][4] == sign:
            return True
        if x[10][4] == sign and x[10][20] == sign and x[2][20] == sign:
            return True
        if x[2][20] == sign and x[6][20] == sign and x[10][20] == sign:
            return True
        ############
        if x[2][4] == sign and x[10][20] == sign:
            return True
        if x[2][20] == sign and x[10][4] == sign:
            return True
        if x[6][4] == sign and x[6][20] == sign:
            return True
        if x[2][12] == sign and x[10][12] == sign:
            return True
    else:
        return False # keeps the game going
def draw_move(board):
# The function draws the computer's move and updates the board.
    computer_move = randrange(1,10)
    while True:
        if computer_move in board:
                board[computer_move - 1] = "X"
                break
        else:
            computer_move = randrange(1,10)
            
    # if computer_move in board:
    #     board[computer_move - 1] = "X"
free_list = []
display_board(board)
make_list_of_free_fields(board)
while not victory_for(board, "O") and not victory_for(board, "X"):
    enter_move(board)
    draw_move(board)
    if victory_for(board, "X") == True:
        break
    display_board(board)
    free_list = []
    make_list_of_free_fields(board)
if victory_for(board_start,"O"):
    print("You win")
if victory_for(board_start,"X"):
    print("You lose.  HaHa <@:D")
