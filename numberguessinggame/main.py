import random
import art

print(art.logo)

print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 to 100")

difficulty = input("Type 'Easy' or 'Hard': ")
difficulty = difficulty.title()

def getting_difficulty():
    if difficulty == "Hard":
        print("You have 5 attempts to guess the number")
        guess = 5
        return guess
    else:
        print("You have 10 attempts to guess the number")
        guess = 10
        return guess

def number_guess(times):
    random_no = random.randint(1,100)
    attempts = True
    while attempts:
        num = int(input("Enter the number for guessing: "))
        if random_no > num:
            print("Too Low")
            times-=1
            if times == 0:
                print("Your attempts are finished and the game is over..")
                print(f"The number is {random_no}")
                attempts = False
            else:
                print(f"You are losing a attempt and {times} attempts are more.")
        elif random_no < num:
            print("Too High")
            times-=1
            if times == 0:
                print("Your attempts are finished and the game is over..")
                print(f"The number is {random_no}")
                attempts = False
            else:
                print(f"You are losing a attempt and {times} attempts are more.")
        else:
            print(f"You have guessed the number correctly {random_no}")
            attempts = False

number_guess(getting_difficulty())