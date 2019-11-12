import random
import os

def display(board):
    os.system("clear")
    print('\t\t\tWELCOME TO TIC TAC TOE\n')
    print('\t\t\t         |    |   ')
    print('\t\t\t      {}  | {}  | {}'.format(board[6],board[7],board[8]))
    print('\t\t\t     ____|____|____')
    print('\t\t\t         |    |   ')
    print('\t\t\t      {}  | {}  | {}'.format(board[3],board[4],board[5]))
    print('\t\t\t     ____|____|____')
    print('\t\t\t         |    |   ')
    print('\t\t\t      {}  | {}  | {}'.format(board[0],board[1],board[2]))
    print('\t\t\t         |    |   ')

def win_check(board,ch):
    return (board[0]==board[1]==board[2]==ch or
    board[3]==board[4]==board[5]==ch or
    board[6]==board[7]==board[8]==ch or
    board[6]==board[3]==board[0]==ch or
    board[7]==board[4]==board[1]==ch or
    board[8]==board[5]==board[2]==ch or
    board[6]==board[4]==board[2]==ch or
    board[8]==board[4]==board[0]==ch)
def full_board(board):
    for items in board:
        if items!='X' and items!='O':
            return False
    return True       

def space_checker(board,ch,x):
    return board[x-1]==x


def place_marker(board,ch,x):
    board.remove(x)
    board.insert(x-1,ch)
    display(board) 


def replay():
    s=input("\nDo u want to play more?\n")
    return s=='Y'


def player_2():
    x=int(input('\nPlayer 2: Enter a position\n'))
    while x>9 or x<1:
        print('\nInvalid position\n')
        x=input('\nEnter position\n')

    while(not space_checker(board,ch1,x)):
        print('\nspace already occupied\n')
        x=int(input('\nPlayer2: Enter a position\n'))
    place_marker(board,ch2,x)  
     


def player_1():
    x=int(input('\nPlayer 1: Enter a position\n'))
    while x>9 or x<1:
        print('\nInvalid position\n')
    while(not space_checker(board,ch1,x)):
        print('\nspace alreday occupied\n')
        x=int(input('\nPlayer 1: Enter a position\n'))
    place_marker(board,ch1,x)
    
     
while(1):
    board=[1,2,3,4,5,6,7,8,9]
    h=-1
    display(board)
    ch1=input('\n\n\n\t\t    Player 1: Do u want to be X or O\n')
    while(ch1!='X' and ch1!='O' ):
        print('\nInvalid choice\n')
        ch1=input('\nEnter X or O\n')

    if ch1=='X':
        ch2='O'
    else:
        ch2='X'    
    print('\n\nPlayer 1: {}'.format(ch1))
    print('\nPlayer 2: {}'.format(ch2))

    print('\nDo u want to begin ?')
    a=input('\nEnter Y or N\n')
    if(a=='Y'):
        turn=random.randint(1,2)
        print('\nPlayer {} starts the game'.format(turn))
        if turn==1:
                ct=1
        if turn==2:
                ct=2
        while(1):
            if ct%2!=0:
                player_1()
                if win_check(board,ch1):
                    print('\nPlayer 1X has won the game')
                    print('\n\n\t\t\t\t  GAME END')
                    print('\n\t______________________________________________________________')
                    if replay():
                        h=1
                        break
                    else:
                        h=0
                        break
                elif full_board(board):
                    if replay():
                        h=1
                        break
                    else:
                        h=0
                        break
                ct+=1
            if ct%2==0:   
                player_2() 
                if win_check(board,ch2):
                    print('\nPlayer 2 has won the game')
                    print('\n\n\t\t\t  GAME END')
                    print('\n\t______________________________________________________________')
                    if replay():
                        h=1
                        break
                    else:
                        h=0
                        break
                if full_board(board):
                    print("\nIt's a Tie")
                    print('\n\n\t\t\t GAME END')
                    print('\n\t______________________________________________________________')
                       
                    if replay():
                        h=1
                        break
                    else:
                        h=0
                        break
                ct+=1
            
        if h==1:
            continue
        if h==0:
            break


 


