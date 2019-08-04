#Guess the number the program randomly generates.
#Concepts: random, variables, integers, input/output, print, while loops, it/else statements

import random
            #guess program
while True:
    x = random.randint(1,10)
    prompt = int(input("Geuss between 1 and 10: "))
    if prompt == x:
            print("You guessed correct!")
    else:
        print("You guessed " + str(prompt) + ", the correct number was " + str(x))
        close_Game = input("Try again? y/n: ")
        if close_Game == str("n"):
            input("Thanks for playing! ")
            break
