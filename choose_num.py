import numpy as np


""" generates the random number """

#creates random number using numpy random module
random_num = np.random.randint(1,101)
print(random_num)

#user_guess = int(input("Enter your guess: "))

"""
for chances in range(10):
    if user_guess == random_num: 
        print("On point!")
        break
    elif user_guess > random_num:
        print("Too big!")
        user_guess = int(input("Enter your next guess:"))
    elif user_guess < random_num:
        print("Too small!")
else:
    print("Try again")
    
"""
#a function for the game itself, each if statement are the different game modes
def the_game():
    game_mode = int(input("Enter which mode: "))
    if game_mode == 1:
        user_guess = int(input("Enter your guess: "))
        chances = 0
        while chances < 9:
            if user_guess == random_num:
                print("On point!")
                break
            elif user_guess > random_num:
                user_guess = int(input("Too big, guess again:"))
                chances += 1
            elif user_guess < random_num:
                user_guess = int(input("Too small, guess again:")) 
                chances += 1   
        else:
            print("Sorry, out of tries for easy mode")
    elif game_mode == 2:
        user_guess = int(input("Enter your guess: "))
        chances = 0
        while chances < 4:
            if user_guess == random_num:
                print("On point!")
                break
            elif user_guess > random_num:
                user_guess = int(input("Too big, guess again:"))
                chances += 1
            elif user_guess < random_num:
                user_guess = int(input("Too small, guess again:"))
                chances += 1    
        else:
            print("Sorry, out of tries for medium mode")
    elif game_mode == 3:
        user_guess = int(input("Enter your guess: "))
        chances = 0
        while chances < 2:
            if user_guess == random_num:
                print("On point!")
                break
            elif user_guess > random_num:
                user_guess = int(input("Too big, guess again:"))
                chances += 1
            elif user_guess < random_num:
                user_guess = int(input("Too small, guess again:"))
                chances += 1    
        else:
            print("Sorry, out of tries for hard mode")
    else:
        print("Not a valid mode")        


# def check_guess():
#create James mode



