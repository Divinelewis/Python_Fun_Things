import random

print(""" WELCOME TO THE FAST NUMBER GAME,
          IT IS PLAYED BETWEEN TWO PLAYERS
          ENTER A RANDOM NUMBER FROM 1 - 10 AS YOUR START POINT
          THE NUMBER ENTERED REPRESENTS THE PLAYER HEALTH
          NUMBERS WILL BE GENERATED AT RANDOM
          AND ADDED TO YOUR INITIAL NUMBER REPRESENTING THE PLAYER HEALTH
          WHICH EVER PLAYER'S HEALTH IS THE FIRST TO INCREMENT TO 150+ WINS""")

player1 = input("Player 1, Please enter your name: ")
player2 = input("Player 2, Please enter your name: ")

# The first (two) while loops run to check the entry made by the user
# If a user enters a number greater than 10 it raises a value error

while True:
    try:
        player1_Health = int(input(f"{player1}, Enter a random number, This number represents your player's initial health (Min. 1 Max = 10): "))
        if player1_Health > 10:
            raise ValueError
        break
    except ValueError:
        print("{}, Your number exceeds 10, enter an integer from 1 - 10 ".format(player1))

while True:
    try:
        player2_Health = int(input(f"{player2}, Enter a random number, This number represents your player's initial health (Min. 1 Max = 10): "))
        if player1_Health > 10:
            raise ValueError
        break
    except ValueError:
        print("{}, Your number exceeds 10, enter an integer from 1 - 10 ".format(player2))

# This section of the code is like the regulatory body of the game
# It first takes the number and passes it through the conditions
# The first if statement in the while loop checks if the the player_health of the player exceeds 150
# If it does, it will break the loop
# Else if the number is less than zero, the elif block comes true then
# The elif block takes the initial number of entered by the both players
# And adds it up with a random generated number till it exceeds 150 as monitored by the first if statement
# Then the first if statement rates the winner of the game

while True:
    if player1_Health and player2_Health >= 150:
        print("Game Over!!!")
        if player1_Health > player2_Health:
            print("{} has won the set target of 150+ with a point of {}".format(player1, player1_Health))
        else:
            print("{} has won the set target of 150+ with a point of {}".format(player2, player2_Health))
        break
    
    elif player1_Health and player2_Health > 0:
        player1_Health = player1_Health + random.randint(1, 20)
        print("{} health is = {}".format(player1, player1_Health))
        player2_Health = player2_Health + random.randint(1, 20)
        print("{} health is = {}".format(player2, player2_Health))

    else:
        pass
