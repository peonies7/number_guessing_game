import numpy as np


""" generates the random number """

#creates random number using numpy random module
random_num = np.random.randint(1,101)
print(random_num)

user_guess = int(input("Enter your guess: "))

if user_guess == random_num:
    print("On point!")
elif user_guess > random_num:
    print("Too big!")
elif user_guess < random_num:
    print("Too small!")
    



