import numpy as np

board = np.zeros((6, 7), dtype=int)
legal_moves = [6]*7

def proper_print():
    print(np.where(board==-1, 2, board))

def check_move(row, col):
    for i in range(0 if row<=3 else row-3, 3 if row>=2 else row+1):
        for j in range(0 if col<=3 else col-3, 4 if col>=3 else col+1):
            current_board = board[i:i+4, j:j+4]
            for k in range(4):
                if sum(current_board[k])==TURN*4 or sum(current_board[:, k])==TURN*4:
                    return True
            if sum(np.diag(current_board))==TURN*4 or sum(np.diag(current_board[::-1]))==TURN*4:
                return True

def find_row(col):
    return 5-np.where(board[::-1, col]==0)[0][0]

def proper_turn():
    return 1 if TURN==1 else 2

def accept_move():
    while True:
        try:
            move = int(input(f"What is player {proper_turn()}'s move?"))-1
            if move in range(7) and legal_moves[move] != 0:
                legal_moves[move] -= 1
                return move
            continue
        except ValueError:
            continue


TURN = 1
proper_print()
while True:
    move = accept_move()
    row = find_row(move)
    board[row, move] = TURN
    proper_print()
    if check_move(row, move):
        print (f"Player {proper_turn()} has won!")
        break
    if sum(legal_moves)==0:
        print ("TIE GAME")
        break
    TURN *= -1