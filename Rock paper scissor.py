import random
import ascii
user_input = int(input("Enter a number, Type 0 for Rock, Type 1 for Scissor, Type 2 for Paper:\n"))
computer_number = random.randint(0,2)
# 0 - rock
# 1 - scissor
# 2 - paper

if user_input == 0:
    print(ascii.rock)
elif user_input == 1:
    print(ascii.scissors)
elif user_input == 2:
    print(ascii.paper)
else:
    print("Invalid Input")
    exit()
    
print("Computer Chose:")

if computer_number == 0:
    print(ascii.rock)
elif computer_number == 1:
    print(ascii.scissors)
else:
    print(ascii.paper)

if user_input == 0 and computer_number == 2:
    print("Computer Wins!!")
if user_input == 2 and computer_number == 0:
    print("You Win!!")
if user_input == 1 and computer_number == 0:
    print("Computer Wins!!")
if user_input == 0 and computer_number == 1:
    print("You Win!!")
if user_input == 2 and computer_number == 1:
    print("Computer Wins!!")
if user_input == 1 and computer_number == 2:
    print("You Win!!")
if user_input == computer_number:
    print("Match Draw!!")




