# use random module to generate a random number between 1 and 100 and asks the user to guess the number

import random
def guess_the_number():
    # generate random number between 1 and 100
    random_number = random.randint(1, 100)
    guess = None
    
    print("I'm thinking of a number between 1 and 100.")
    
    # keep prompting the user until they guess correctly
    while guess != random_number:
        # ask the user to make a guess
        guess = int(input("Take a guess: "))
        
        # check if the guess is correct, too high, or too low
        if guess < random_number:
            print("Too Low! Try again.")
        elif guess > random_number:
            print("Too High! Try again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly.")
            
            
guess_the_number()