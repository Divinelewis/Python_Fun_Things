"""
- Create a function that checks the user input
- The function compares the user input with the correct answer
- If the user input is different from the correct answer is allows the user to try again
- The function also allows the user to make two attempts
- If the user input is not correct in the two attempts, it prints the correct answer to the screen
- The function also scores users between 3 points to 1 point depending on the attempt made before getting the correct answer
- The lesser the trail the greater the point (3 points - one attempt, 2 points - two attempts, 1 point - 3 attempts)"""

def check_guess(guess, answer):

#the "global" keyword is used to indicate that score is a global variable
    global score
    Guess_in_progress = True
    Attempt_made = 0

    while Guess_in_progress and Attempt_made < 3:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score = (score + 3) - Attempt_made
            Guess_in_progress = False

        else:
            if Attempt_made < 2:
                guess = input('Sorry, wrong answer, try again ')
            Attempt_made += 1

    if Attempt_made == 3:
        print('\n The correct answer is ' + answer)

#create a score variable and set its initial value to zero
score = 0

print("Guess the animal\n")

#print the questions and getting user inputs
#The \n characters are combined to make a new line
#While the \ is used to break a string to a newline if we dont want it bigger than our screen width

guess1 = input('1. Which bear lives at the north pole\n \
(A) Polar bear\n (B) Crocodile\n (C) Shark\n \
Type A, B, or C\n')
check_guess(guess1, 'A')

print("\n")
guess2 = input('2. Which is the fastest land animal?\n \
(A) Lion\n (B) Tiger\n (C) Cheetah\n \
Type A, B, or C\n')
check_guess(guess2, 'c')

print("\n")
guess3 = input('Which is the largest animal?\n \
(A) Blue whale\n (B) shark\n (C) Elephant\n \
Type A, B, or C\n')
check_guess(guess3, 'a')

#prints the final score of the player
#str() is used to typecast the integer to a string because the you cannot concatenate a string and an integer 
print('\nYour score is ' + str(score))
