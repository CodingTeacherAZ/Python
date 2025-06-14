 ##### IMPORTS #####
import random
import time

##### FUNCTIONS #####
def start_game():
   ## these global state variables need to reset at each new game  ##
    global tic_tac_toe
    tic_tac_toe = [
    [" ", " ", " A ", "  ", " B ", "  ", " C "],
    ["1", " ", "   ", " | ", "   ", " | ", "   " ],
    [" ", " ", "-------------------------------" ],
    ["2", " ", "   ", " | ", "   ", " | ", "   " ],
    [" ", " ", "--------------------------------" ],
    ["3", " ", "   ", " | ", "   ", " | ", "   " ],
    ]

    global playable_indices
    playable_indices = {
    "1A": (1, 2),
    "1B": (1, 4),
    "1C": (1, 6),
    "2A": (3, 2),
    "2B": (3, 4),
    "2C": (3, 6),
    "3A": (5, 2),
    "3B": (5, 4),
    "3C": (5, 6),
    }
    global user_moves
    user_moves = []
    global computer_moves
    computer_moves= []                    

    global user_marker, computer_marker
    global player
    global playing
    global games_played
    global user_wins
    

    ### Start of the game ####
    if games_played == 0:
        print("Let's play a game of tic-tac-toe!  ")
    else:
        print("Great game! 👏🏼" )
        playing = input("Would you like to play again? ").lower() == 'y'

    if playing:
        print("________________________________________________________")
        user_marker, computer_marker = player_tokens()
        display_board(user_marker)
        player = random.randint(0, 1)
        print("The first player is determined by coin toss.")
        time.sleep(2)
        if player == 0:
            print("You won the coin toss! 🙌🏼")
        else:
            print("Computer wins the toin coss.")
    else:
        playing = False

def player_tokens():
    while True:
        user_token = input("Do you want to be ❎ or 🅾️? ").upper()
        if user_token in ['X', 'O']:
            break
        else:
            print("Oops, try again!")

    if user_token == "X":
        user_token = "❎"
        computer_token = "🅾️"
    else:
        computer_token = "❎"
        user_token = "🅾️"
    return (user_token, computer_token)

def display_board(token, row = None, col = None):
    global tic_tac_toe
    if row != None:
        tic_tac_toe[row][col] = token
    for r in tic_tac_toe:
        for c in r:
            print(c, end=" ")
        print()
    return

def user_move():
    global playable_indices
    global user_moves
    print("________________________________________________________")
    print("Your move.")
    while True:
        col_letter = input("Which column do you select: A, B, or C? ").upper()
        if col_letter in ['A', 'B', 'C']:
            break  
        else:
            print("Oops, invalid input, please try again")

    while True:
        row_number = input("Which row do you select: 1, 2, or 3? ")
        if row_number in ['1', '2', '3']:
            break
        else:
            print("Oops, invalid input, please try again")

    coordinates = row_number + col_letter

    if coordinates not in playable_indices:
        print("Invalid move")
    else:
        marker = playable_indices[coordinates]
        user_moves.append(coordinates)
        del playable_indices[coordinates]
        return marker

def computer_move():
    global playable_indices
    global computer_moves
    print("________________________________________________________")
    print("Computer's move.")
    move_options = []
    for key in playable_indices:
        move_options.append(key)
    select_move = random.randint(0,len(move_options)-1)
    coordinates = move_options[select_move]
    marker = playable_indices[coordinates]
    computer_moves.append(coordinates)
    del playable_indices[coordinates]
    time.sleep(random.randint(2,4))
    return marker

def end_game(plays_list):
    global winning_combinations
    global playable_indices
    global player
    global games_played
    global user_wins
    for win_list in winning_combinations.values():
        if win_list.issubset(set(plays_list)):
            if player == 0:
                print("Very nice!  You have won the game. 🏆")
                games_played +=1
                user_wins +=1
                return True
            else:
                print("The computer has won this game.")
                games_played +=1
                return True
    if len(playable_indices) == 0:
        print("The game is a draw.  ⚔️ There is no winner.")
        games_played +=1
        return False

##### STATE VARIABLES #####
winning_combinations = {
    1: {"1A", "1B", "1C"},
    2: {"2A", "2B", "2C"},
    3: {"3A", "3B", "3C"},
    4: {"1A", "2A", "3A"},
    5: {"1B", "2B", "3B"},
    6: {"1C", "2C", "3C"},
    7: {'1A', '2B', '3C'},
    8: {'1C', '2B', '3A'},
    }

game_over= False

playing = True
user_wins = 0
games_played = 0

##### GAME PLAY LOOP #####
while playing:
    start_game()
    if not playing:
        break
    while len(playable_indices) > 0 and not game_over :
        if player == 0:  # user
            while True:
                marker = user_move()
                if marker:
                    row, col = marker
                    break
            display_board(user_marker, row, col)
            game_over = end_game(user_moves)
            print()
            player = 1
        else:
            row,col = computer_move()
            display_board(computer_marker,row, col)
            game_over = end_game(computer_moves)
            print()
            player = 0
    
print("________________________________________________________")
print("We played", games_played, "games.  You won", user_wins," of those games.")
print("Great job! 😇")




'''
------ Making the Computer Smart ----
Basic Moves:
Start with a set of basic moves that the computer should prioritize. These moves can include:
    Winning moves: Check if the computer can win the game on the current move.
    Blocking moves: Check if the opponent (user) is about to win, and block them.
    Center move: If available, consider taking the center spot as it's strategically strong.
    Corner moves: Corners are also strong positions, so consider them.
    Edge moves: If no other good move is available, choose an edge.

Evaluation Function:
Create an evaluation function that assigns a score to each potential move.
This function can take into account factors like:
    The number of computer pieces in a row, column, or diagonal.
    The number of user pieces in a row, column, or diagonal.
    The importance of the move (e.g., center, corner, or edge).
    Potential for a winning move in the next turn.
    Potential for a block to prevent the user from winning.

Minimax Algorithm:
Implement the minimax algorithm with alpha-beta pruning.
This algorithm explores different moves and their consequences recursively, considering both the
computer's and the user's moves. It aims to find the best move for the computer by
maximizing its chances of winning and minimizing the user's chances.

Depth-Limited Search:
To make the algorithm efficient, you can limit the depth of the search tree.
You may not need to explore all possible moves but instead focus on a few moves ahead.

Randomization:
Introduce an element of randomness to the computer's decision-making.
This can make the game feel less predictable and more human-like.

Testing and Tuning:
Test your AI against human players and fine-tune its behavior.
You may need to adjust the evaluation function or the depth of the
search based on how well it performs.

Game State Representation:
Ensure that your game state representation allows you to easily evaluate and simulate moves.
Having an efficient way to check for winning conditions and available moves is crucial.

Handling Corner Cases:
Consider how your AI will handle special cases, such as when the user or the computer
is one move away from winning. In such cases, the AI should prioritize
winning or blocking rather than following a general strategy.

Difficulty Levels:
Optionally, you can implement different difficulty levels,
allowing users to choose how challenging they want the computer opponent to be. For easier levels,
the computer can make more random moves, while for harder levels, it can use advanced strategies.

'''
