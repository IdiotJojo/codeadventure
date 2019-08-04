#Dice Rolling Simulator
#Concepts: Random.randint, integer, while, print

import random

while True:
    prompt = input("Roll Dice? y/n ")
    if prompt == str("y"):
        print(random.randint(1,12))
    else:
        prompt1 = input("Thanks for playing.")
        break
        
