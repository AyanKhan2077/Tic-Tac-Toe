from os import system
import random
def print_board(board : list) :
    for i in range(len(board)) :
        print(board[i],end= ' ')
        if i % 3 == 2 : print() 
def win_check(board : list):
    if ''.join(board).isalpha() : return 'TIE'
    for i in range(3) : 
        if board[i] == board[i + 3] == board[i + 6] :   return board[i]
    for i in range(0,7,3):
        if board[i] == board[i + 1] == board[i + 2] :   return board[i]
    if board[0] == board[4] == board[8] :   return board[0]
    if board[2] == board[4] == board[6] :   return board[2]
    return 0
def tictactoi_run(name,player_symbol,bot_symbol,diff_level):
    print(name,player_symbol)
    board = [str(i) for i in range(9)]
    if player_symbol == 'O' :
        idx = random.choice([0,2,4,6,8])
        board[idx] = bot_symbol    
    def play() :
        print_board(board)
        idx = input('Enter a vaid Position >') 
        if idx.isnumeric() :
            idx = int(idx)
            if 0<=idx<=8 and str(board[idx]).isnumeric() :
                board[idx] = player_symbol
                result = win_check(board)
                
                if result : system('cls');print_board(board);return result
                
                ##########################################################
                #easy
                if diff_level == '1' :
                    idx = tictactoi_easy_engine(board)
                #mid
                elif diff_level == '2' :
                    idx = tictactoi_mid_engine(board,bot_symbol,player_symbol)
                #IMPOSSIBLE
                else :
                    idx = tictactoi_impossible_engine(board,bot_symbol,player_symbol)
                ###########################################################
                board[idx] = bot_symbol 
                result = win_check(board)
                if result : system('cls');print_board(board);return result
                system('cls')
            else : 
                system('cls');print('invalid input');play()
        else : 
            system('cls');print('invalid input');play()
    while not "".join(board).isalpha() :
        result = play()
        if result : break
    if result == "TIE" : print("It's a TIE !")
    else :
        print(f"Winner --> {result}\n")
        if result == player_symbol :
            print(f"Congratulations {name} !!\n")
    return
def tictactoi_easy_engine(board:list)->int :
    idx = random.randint(0,8)
    while str(board[idx]).isalpha() : idx = random.randint(0,8)
    return idx
def tictactoi_mid_engine(board:list,bot_symbol,player_symbol)-> int:
    not_possible = [i for i in range(len(board)) if str(board[i]).isalpha() == 0]
    possible = []
    #col
    for i in range(3) :
        if board[i+3] == board[i+6] : possible.append([i,board[i+3]])
        if board[i]  == board[i+6]  : possible.append([i + 3,board[i]])
        if board[i] == board[i + 3] : possible.append([i + 6,board[i]])
    #row
    for i in range(0,7,3):
        if board[i + 1] == board[i + 2] : possible.append([i,board[i+1]]) 
        if board[i + 2] == board[i ]    : possible.append([i + 1,board[i]]) 
        if board[i] == board[i + 1]     : possible.append([i + 2,board[i+1]])
    #diagonal   
    if board[4] == board[8] : possible.append([0,board[4]]) 
    if board[8] == board[0] : possible.append([4,board[8]]) 
    if board[0] == board[4] : possible.append([8,board[0]]) 
    if board[2] == board[4] : possible.append([6,board[2]]) 
    if board[6] == board[4] : possible.append([2,board[4]]) 
    if board[6] == board[2] : possible.append([4,board[6]]) 
    for idx,symbol in possible :
        if symbol == bot_symbol and str(board[idx]).isnumeric() :
            return idx
    for idx,symbol in possible :
        if symbol == player_symbol and str(board[idx]).isnumeric() :
            return idx
    idx = random.randint(0,8)
    #looks like an infinite loop but its not
    while str(board[idx]).isalpha() : 
        idx = random.randint(0,8)
    return idx  
def tictactoi_impossible_engine(board:list,bot_symbol,player_symbol)-> int:
    #TODO
    corners = [0,2,6,8]  
    center = [4]
    rest   = [1,3,5,7]
    if bot_symbol == "O" :
        if str(board[4]).isnumeric() :
            return 4
    # Direct Win/Lose conditions 
    def sol(board) :
        #col
        possible = []
        for i in range(3) :
            if board[i+3] == board[i+6] : possible.append([i,board[i+3]])
            if board[i]  == board[i+6]  : possible.append([i + 3,board[i]])
            if board[i] == board[i + 3] : possible.append([i + 6,board[i]])
        #row
        for i in range(0,7,3):
            if board[i + 1] == board[i + 2] : possible.append([i,board[i+1]]) 
            if board[i + 2] == board[i ]    : possible.append([i + 1,board[i]]) 
            if board[i] == board[i + 1]     : possible.append([i + 2,board[i+1]])
        #diagonal   
        if board[4] == board[8] : possible.append([0,board[4]]) 
        if board[8] == board[0] : possible.append([4,board[8]]) 
        if board[0] == board[4] : possible.append([8,board[0]]) 
        if board[2] == board[4] : possible.append([6,board[2]]) 
        if board[6] == board[4] : possible.append([2,board[4]]) 
        if board[6] == board[2] : possible.append([4,board[6]]) 
        return possible
    possible = sol(board)
    for idx,symbol in possible :
        if symbol == bot_symbol and str(board[idx]).isnumeric() :
            return idx
    for idx,symbol in possible :
        if symbol == player_symbol and str(board[idx]).isnumeric() :
            return idx
    
    #for bot_symbol = O
    if bot_symbol == "O" == board[4]  :
        for idx in rest :
            if str(board[idx]).isnumeric() :
                return idx
            
    #for bot_symbol = X
    corners = [i for i in corners if str(board[i]).isnumeric()]
    if len(corners)>0 :
        idx = random.choice(corners)
        return idx
    return
def tictactoi(play_again = 1):
    if play_again == '0' : return
    print("Welcome! Lets Play tictactoi")
    name = input("Enter your name > ")
    print("Choose your difficulty \n1-easy \n2-medium\nPress Enter for-IMPOSSIBlE")
    cmd = input('1/2/n for easy/medium/IMPOSSIBLE> ')
    player_symbol = input('Want to play first? Press Enter ! \nor Enter 0 > ')
    if player_symbol == '0' : player_symbol = 'O';bot_symbol = 'X'
    else : player_symbol = 'X';bot_symbol = 'O'
    tictactoi_run(name,player_symbol,bot_symbol,cmd)
    cmd = input("1)Enter 0 to exit \n2)press enter to play again.> ")
    return tictactoi(cmd)
if __name__ == "__main__" :
    tictactoi()