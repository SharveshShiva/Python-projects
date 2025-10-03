import random
import Words_list 
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

choosen_word = random.choice(Words_list.words_list)

placeholder = ""

for i in choosen_word:
    placeholder+="-"

print(placeholder)

game_over = False
actual_word = []

lives = 6
print("You are going to guess a animal name or a bird name..")

while not game_over:
    print(f"You have {lives} life with you..")
    user_input = input("Enter a letter to guess the word!!:\n").lower()
    display = ""
    
    for i in choosen_word:
        if i == user_input:
            display += i
            actual_word.append(i)
        elif i in actual_word:
            display += i     
        else:
            display += "_" 

    if user_input not in choosen_word:
        lives-=1
        if lives==0:
            print("Game Over..****YOU LOSE****")
            game_over = True

    print(display,"\n") 
    print(stages[lives]) 

    if "_" not in display:
        game_over = True
        print("***************YOU WIN*****************.")  

print(f"The Word is: {choosen_word}")
 

       




 


