import random

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player1 = 'X'
player2 = 'O'

P1WIN = 0
P2WIN = 0


def getBoard():
    return f"[{board[0][0]}][{board[0][1]}][{board[0][2]}]\n[{board[1][0]}][{board[1][1]}][{board[1][2]}]\n[{board[2][0]}][{board[2][1]}][{board[2][2]}]"


def clearBoard(board):
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def placeRandomMove():
    while True:
        randomFirst = random.randint(0, 2)
        randomSecond = random.randint(0, 2)
        if board[randomFirst][randomSecond] == ' ':
            placeMove(player2, randomFirst, randomSecond)
            return


def placeMove(symbol, x, y):
    board[x][y] = symbol


# checks if board is empty
def canPlace(x, y):
    if board[x][y] == " ":
        return True
    return False


def isEmpty():
    for i in board:  # i is a list
        for j in i:  # j is a string
            if j != " ":
                return False

    return True


# checks if the board is full and there are no wins
def isFull():
    for i in board:
        for a in i:
            if a == " ":
                return False

    return True


# check for the 8 ways that someone can win in tictactoe (3 in a row of X or O)
def checkWin():
    # check the horizontal wins
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:

            if board[row][0] == player1:
                return player1
            elif board[row][0] == player2:
                return player2

    # check the vertical wins
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column]:
            if board[0][column] == player1:
                return player1
            elif board[0][column] == player2:
                return player2

    # check the diagonal wins
    # two if statements
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == player1:
            return player1
        elif board[0][0] == player2:
            return player2
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == player1:
            return player1
        elif board[0][2] == player2:
            return player2
    return " "
