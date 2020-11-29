

the_game_board = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

game_board_keys = []

for key in the_game_board:
    game_board_keys.append(key)



def printgame_board(game_board):
    print(game_board['1'] + '|' + game_board['2'] + '|' + game_board['3'])
    print('-+-+-')
    print(game_board['4'] + '|' + game_board['5'] + '|' + game_board['6'])
    print('-+-+-')
    print(game_board['7'] + '|' + game_board['8'] + '|' + game_board['9'])

#Now we get to name our players
if __name__ == "__main__":
 
    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")
 
    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")

# This is the function for determining where the X and Os are placed
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printgame_board(the_game_board)
        print("It's your move," + turn + ".Chose your place?")

        move = input()        

        if the_game_board[move] == ' ':
            the_game_board[move] = turn
            count += 1
        else:
            print("Can't go there.\n Please try again")
            continue

        # This checks to see if anyone has has won after 5 moves.  The game will end if there is a win 
        if count >= 5:
            if the_game_board['1'] == the_game_board['2'] == the_game_board['3'] != ' ': # all the way across the top ends the game
                printgame_board(the_game_board)
                print("\nGame Over.\n")                
                print("  " +turn + " has won. ")                
                break
            elif the_game_board['4'] == the_game_board['5'] == the_game_board['6'] != ' ': # game ends if  won across the middle
                printgame_board(the_game_board)
                print("\nGame Over.\n")                
                print("  " +turn + " has won. ")
                break
            elif the_game_board['7'] == the_game_board['8'] == the_game_board['9'] != ' ': # all the way across the bottom wins and ends game
                printgame_board(the_game_board)
                print("\nGame Over.\n")                
                print("  " +turn + " has won. ")
                break
            elif the_game_board['7'] == the_game_board['4'] == the_game_board['1'] != ' ': # left side down wins and ends game
                printgame_board(the_game_board)
                print("\nGame Over.\n")                
                print("  " +turn + " has won. ")
                break
            elif the_game_board['8'] == the_game_board['5'] == the_game_board['2'] != ' ': # middle all the way down wins
                printgame_board(the_game_board)
                print("\nGame Over.\n")                
                print("  " +turn + " has won. ")
                break
            elif the_game_board['9'] == the_game_board['6'] == the_game_board['3'] != ' ': # right side down wins the game
                printgame_board(the_game_board)
                print("\nGame Over.\n")                
                print("  " +turn + " has won. ")
                break 
            elif the_game_board['1'] == the_game_board['5'] == the_game_board['9'] != ' ': # a diagonal win ends the game
                printgame_board(the_game_board)
                print("\nGame Over.\n")                
                print("  " +turn + " has won. ")
                break
            elif the_game_board['7'] == the_game_board['5'] == the_game_board['3'] != ' ': # a diagonal win ends the game
                printgame_board(the_game_board)
                print("\nGame Over.\n")                
                print("  " +turn + " has won. ")
                break 

        # If the game_board is full and there is no winner then it is a tie.
        if count == 9:
            print("\nGame Over.\n")                
            print("Tie game")

        # This changes the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # This is an option asking if you want to play another game
    restart = input("Would you like to play again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in game_board_keys:
            the_game_board[key] = " "

        game()

if __name__ == "__main__":
    game()
