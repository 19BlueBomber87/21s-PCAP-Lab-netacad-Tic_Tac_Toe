#Tic_Tac_toe
import random
import time
def computer_speech(text):
    for chr in text:
        print(chr, end=" ", flush=True)
        time.sleep(.1)
def update_game(text):
        for chr in text:
            print(chr, end="", flush=True)
            time.sleep(.001)
x = """+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+)"""
s_list = [1,2,3,4,6,7,8,9]
def display_board(x):
    computer_speech("BWHAHAHAHA!!!\nI get the first move!\n")
    computer_speech("Game Starting\n")
    update_game(x)
def enter_move():
    turn_count = 0
    z = x[:]
    s_list_game = s_list[:]
    while turn_count <= 8:
        s_number = input("\nEnter a Square's Number: ")
        try:
            s_number = int(s_number)
        except ValueError:
            print("Only numbers 1-9.\nTerminating program, Error, Error\n <@:D")
        if s_number in s_list_game:
            y = z[:].replace(str(s_number), "O")
            update_game(y)
            index_num = s_list_game.index(s_number)
            del s_list_game[index_num]
            computer_speech("\nComputer Is Thinking. . . . . . .")
            time.sleep(2)
            random_num = random.choice(s_list_game)
            w = y[:].replace(str(random_num), "X")
            index_rand = s_list_game.index(random_num)
            del s_list_game[index_rand]
            print("\nTrun Number [",turn_count + 1, "]\nBelow are the choices that are left:\n",s_list_game)
            update_game(w)
            z = w[:]
            turn_count += 1
            # if O wins
            o_win = ("O","O","O")
            x_win =("X","X","X")
            x_win_diag = ("X","X")
            laugh = "HAHAHAHAHAHAHAHAHA\nHAHAHAHAHAHAHA"
            if (z[56], z[64], z[72]) == o_win:
                print("You Win!!")
                break
            elif (z[56], z[160], z[264]) == o_win:
                print("You Win!!")
                break
            elif (z[264], z[272], z[280]) == o_win:
                print("You Win!!")
                break
            elif (z[72], z[176], z[280]) == o_win:
                print("You Win!!")
                break
            # if X wins
            elif (z[56],z[64],z[72]) == x_win:
                print("You Lose!")
                computer_speech(laugh * 5)
                break
            elif (z[56],z[160],z[264]) == x_win:
                print("You Lose!")
                computer_speech(laugh * 5)
                break
            elif (z[264], z[272], z[280]) == x_win:
                print("You Lose!")
                computer_speech(laugh * 5)
                break
            elif (z[72], z[176], z[280]) == x_win:
                print("You Lose!")
                computer_speech(laugh * 5)
                break
                #Diag
            elif (z[56], z[280]) == x_win_diag:#1
                print("You Lose!")
                computer_speech(laugh * 5)
                break
            elif (z[72], z[264]) == x_win_diag:#2
                print("You Lose!")
                computer_speech(laugh * 5)
                break
            elif (z[64], z[272]) == x_win_diag:
                print("You Lose!")
                computer_speech(laugh * 5)
                break
            elif (z[160], z[176]) == x_win_diag:
                print("You Lose!")
                computer_speech(laugh * 5)
                break
def start_game(t = True):
    start_game = input("Start Game?: ")
    while t == True:
        if start_game.upper() == "YES":
                display_board(x)
                enter_move()
                again = input("\nAgain?")
                again = again.upper()
                if again != "YES":
                    print("See Ya Later")
                    t = False
        else:
            t = False
            print("Good Bye")
start_game()
#Win_Key[]
#print(z[56]) # 1
#print(z[64]) #2
#print(z[72]) # 3
#print(z[160]) #4
#print(z[168]) # x
#print(z[176]) # 6
#print(z[264]) #7
#print(z[272]) # 8
#print(z[280]) #9