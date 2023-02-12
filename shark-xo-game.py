import os
from os import system
import sys
from colorama import Fore
from time import sleep
os.system('cls' if os.name=='nt' else 'clear')
clearConsole = lambda:os.system('cls' if os.name in ('nt','dos') else 'clear')

# ------ colors
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
y = r


player = ""
p1 = 0
p2 = 0

row1 = [0 , 1 , 2]
row2 = [3 , 4 , 5]
row3 = [6 , 7 , 8]

def animation(p):
    for i in p:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.0001)

logo = Fore.YELLOW+"""
    ██╗  ██╗ ██████╗        ██████╗  █████╗ ███╗   ███╗███████╗
    ╚██╗██╔╝██╔═══██╗      ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
     ╚███╔╝ ██║   ██║█████╗██║  ███╗███████║██╔████╔██║█████╗  
     ██╔██╗ ██║   ██║╚════╝██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
    ██╔╝ ██╗╚██████╔╝      ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
    ╚═╝  ╚═╝ ╚═════╝        ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝"""

def banner():
    animation(logo)
    print(""" 

           \033[1;37mDeveloper  \033[1;34m: \033[1;31mayushi-pranshu
           \033[1;37mGithub     \033[1;34m: \033[1;31msincryptshark
           \033[1;37mInstagram  \033[1;34m: \033[1;31m@0891322930""")

banner()

def update_game():
    # to display the game
    print('\n')
    okay = '              '
    print(okay,Fore.GREEN,row1[0],Fore.RED,"┃",Fore.GREEN,row1[1],Fore.RED,"┃",Fore.GREEN,row1[2])
    print(okay,Fore.RED,"━━━━━━━━━━━━━")
    print(okay,Fore.GREEN,row2[0],Fore.RED,"┃",Fore.GREEN,row2[1],Fore.RED,"┃",Fore.GREEN,row2[2])
    print(okay,Fore.RED,"━━━━━━━━━━━━━")
    print(okay,Fore.GREEN,row3[0],Fore.RED,"┃",Fore.GREEN,row3[1],Fore.RED,"┃",Fore.GREEN,row3[2])

def ins1(pos,name):
    # for adding in row 1
        row1.remove(pos)
        row1.insert(pos, name)

def ins2(pos,name):
    # for adding in row 2
        new_pos = int(pos) - int(3)
        row2.remove(pos)
        row2.insert(new_pos, name)

def ins3(pos,name):
    #for adding in row 3
        new_pos = int(pos) - int(6)
        row3.remove(pos)
        row3.insert(new_pos, name)

def check_winer():

    # Player1
    if row1.count("X") == 3:
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 1 ] Won !")
        return True
    elif row2.count("X") == 3:
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 1 ] Won !")
        return True
    elif row2.count("X") == 3:
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 1 ] Won !")
        return True
    elif row3[0] == "X" and row2[1] == "X" and row1[2] == "X":
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 1 ] Won !")
        return True
    elif row1[0] == "X" and row2[1] == "X" and row3[2] == "X":
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 1 ] Won !")
        return True
    elif row3[0] == "X" and row2[0] == "X" and row1[0] == "X":
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 1 ] Won !")
        return True
    elif row3[1] == "X" and row2[1] == "X" and row1[1] == "X":
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 1 ] Won !")
        return True
    elif row3[2] == "X" and row2[2] == "X" and row1[2] == "X":
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 1 ] Won !")
        return True

    #Player2
    elif row1.count("O") == 3:
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 2 ] Won !")
        return True
    elif row2.count("O") == 3:
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 2 ] Won !")
        return True
    elif row2.count("O") == 3:
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 2 ] Won !")
        return True
    elif row3[0] == "O" and row2[1] == "O" and row1[2] == "O":
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 2 ] Won !")
        return True
    elif row1[0] == "O" and row2[1] == "O" and row3[2] == "O":
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 2 ] Won !")
        return True
    elif row3[0] == "O" and row2[0] == "O" and row1[0] == "O":
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 2 ] Won !")
        return True
    elif row3[1] == "O" and row2[1] == "O" and row1[1] == "O":
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 2 ] Won !")
        return True
    elif row3[2] == "O" and row2[2] == "O" and row1[2] == "O":
        print(r+"\n└─"+w+"\033[1;37mPlayer [ 2 ] Won !")
        return True
    else:
        return False

while True:

    #title = (f"It's {player} turn       Player(1) Played {p1} times       Player(2) Played {p2} times")
    #system("title " + title)
    
    update_game()
    if check_winer():
        input(" \n Press Enter To Quit: ")
        break

    player = "Player(1)"
    player1 = int(input(r+"\n\n └─> "+w+"\033[1;37mPlayer Choice [ 1 ] : "+r))
    if player1 < 3:
        ins1(player1,"X")
    elif player1 >= 3 and player1 < 6:
        ins2(player1, "X")
    elif player1 >= 6 and player1 < 9:
        ins3(player1, "X")
    p1 +=1
    clearConsole()

    update_game()
    if check_winer():
        dff = input(" \n Do you want to play Again [y/n]:  ")
        if dff=='y' or dff=='Y':
            system('python shark-xo-game.py')
        else:
            sys.exit()
        break

    player = "Player(2)"
    player2 = int(input(r+"\n\n └─> "+w+"\033[1;37mPlayer Choice [ 2 ] : "+r))
    if player2 < 3:
        ins1(player2,"O")
    elif player2 >= 3 and player2 < 6:
        ins2(player2, "O")
    elif player2 >= 6 and player2 < 9:
        ins3(player2, "O")
    p2 += 1
    clearConsole()




