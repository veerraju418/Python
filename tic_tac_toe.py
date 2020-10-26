#tic tac toe game using python
#board
#display board
#play game
#handle turn
#check if win
#check if tie
#flip players
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
game_still_going=True
current_player="X"
winner=None
def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2]+"   "+"1"+"|"+"2"+"|"+"3")
    print(board[3]+"|"+board[4]+"|"+board[5]+"   "+"4"+"|"+"5"+"|"+"6")
    print(board[6]+"|"+board[7]+"|"+board[8]+"   "+"7"+"|"+"8"+"|"+"9")
def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_gameover()
        flip_players()
    if winner=="X" or winner=="0":
        print(winner+" won")
    else:
        print("tie")
        
def handle_turn(player):
    print(player+"'s turn.")
    position=input("choose a position from 1 to 9:")
    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=input("choose a position from 1 to 9:")
            
        position=int(position)-1
        if board[position]=="-":
            valid=True
        else:
            print('You cannot go there')
    board[position]=player
    display_board()
def check_if_gameover():
    check_if_win()
    check_if_tie()
def check_if_win():
    global winner
    row_win=check_rows()
    col_win=check_cols()
    dig_win=check_dig()
    if row_win:
        winner=row_win
    elif col_win:
        winner=col_win
    elif dig_win:
        winner=dig_win
    else:
        winner=None
def check_rows():
    global game_still_going
    row_1=board[0]==board[1]==board[2]!="-"
    row_2=board[3]==board[4]==board[5]!="-"
    row_3=board[6]==board[7]==board[8]!="-"
    if row_1 or row_2 or row_3:
        game_still_going=False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
def check_cols():
    global game_still_going
    col_1=board[0]==board[3]==board[6]!="-"
    col_2=board[1]==board[4]==board[7]!="-"
    col_3=board[2]==board[5]==board[8]!="-"
    if col_1 or col_2 or col_3:
        game_still_going=False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None
def check_dig():
    global game_still_going
    dig_1=board[0]==board[4]==board[8]!="-"
    dig_2=board[6]==board[4]==board[2]!="-"
    if dig_1 or dig_2:
        game_still_going=False
    if dig_1:
        return board[0]
    elif dig_2:
        return board[6]
    else:
        return None
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
        return True
    else:
        return False
def flip_players():
    global current_player
    if current_player=="X":
        current_player="0"
    elif current_player=="0":
        current_player="X"
play_game()

