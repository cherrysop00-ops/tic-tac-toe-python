'''

   |   |
---+---+---
   |   |
-+-+---+---
   |   |

 
'''
print("          TIC-TAC-TOE")
game_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0

def game_board(game_list):
    print(f'''
           {game_list[0]} | {game_list[1]} | {game_list[2]}
          ---+---+---
           {game_list[3]} | {game_list[4]} | {game_list[5]}
          ---+---+---
           {game_list[6]} | {game_list[7]} | {game_list[8]}   
    ''')

def winner(g ,player):
    if((g[0] == g[1] == g[2] == player) or 
       (g[0] == g[4] == g[8] == player) or 
       (g[0] == g[3] == g[6] == player) or
       (g[1] == g[4] == g[7] == player) or
       (g[2] == g[5] == g[8] == player) or
       (g[2] == g[4] == g[6] == player) or
       (g[3] == g[4] == g[5] == player) or
       (g[6] == g[7] == g[8] == player)
    ):
        return player
    
    elif all(type(i) == str for i in g):
        return "tie"

    else:
        return None
    

game_board(game_list)
player_1 = input("Choose one[X/O]:").upper()
player_2 = "O" if "X" in player_1 else "X"
print("place your pieces in the slots that appear")

while True:
    while True:
        player_1_input = int(input(f"{player_1} turn :"))
        if(player_1_input <= 9 and player_1_input >= 1):
            if(game_list[player_1_input - 1] == f"{player_2}"):
                print(f"the place is already occupied by {player_2}")
            else:    
                game_list[player_1_input - 1] = player_1
                game_board(game_list)
                break


        else:
            print("place your piece in the given range of position")
            player_1_input = int(input(f"{player_1} turn :"))

    verdict = winner(game_list, player_1)
    if verdict is not None:
        if(verdict == "tie"):
            print("It's a tie")
            break
        else:
            print(f"{verdict} is the winner")
            break
            
    while True:
        player_2_input = int(input(f"{player_2} turn :"))
        if(player_2_input <= 9 and player_2_input >= 1):
            if(game_list[player_2_input - 1] == f"{player_1}"):
                print(f"the place is already occupied by {player_1}")
            else:
                game_list[player_2_input - 1] = player_2
                game_board(game_list)
                break
            
        else:
            print("place your piece in the given range of position")
            player_2_input = int(input(f"{player_2} turn :"))
    
    verdict = winner(game_list, player_2)
    if verdict is not None:
        if(verdict == "tie"):
            print("It's a tie")
            break
        else:
            print(f"{verdict} is the winner")
            break
