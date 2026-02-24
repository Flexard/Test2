
#variables

player1 = "X"
player2 = "O"


board = [
["_","_","_"],
["_","_","_"],
["_","_","_"]
    ]


#----functions----

def display_board(board):

    print(board[0])
    print(board[1])
    print(board[2])


def place_thing(x,y,player_1):
    if player == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "O"

def player_1_turn():
    print("PLAYER 1 (X)")
    x = input("Enter A, B or C co-ord:")
    y = int(input("enter 1, 2 or 3 co-ord:"))


def player_2_turn():
    print("PLAYER 2 (O)")
    x = input("Enter A, B or C co-ord:")
    y = int(input("enter 1, 2 or 3 co-ord:"))
    place_thing(x,y,1)

def plot_turn():
    if x == "A" and y == 1:
        print




#def player_1():

#def player_2():

#----Start----

display_board(board)

#board
for x in range(0,len(board)):
    print(x+1,end="")
    for y in range(0,len(board[x])):
        print("|_",end="|")
    print()
print("  A  B  C")

player_1_turn()
























