print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")

road = input('You\'re at a cross road. Where do you want to go?\n     Type "left" or "right"\n').lower()
if road == "left":
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake.\n  Type "wait" to wait for a boat. Type "swim" to swim to swim across.\n').lower()
    if lake == "wait":
        island = input("You arrive at the island unharmed. There us a house with 3 doors.\n   One red, One yellow and One blue. Which colour do you choose?\n").lower()
        if island == "red":
            print("You have entered a room full of fire.... Game Over!!!")
        elif island == "yellow":
            print("You have entered the treasure island... Congrats the treasure is yours!!")
        elif island == "blue":
            print("You have entered a room surrounded full of water... Game Over!!!")
        else:
            print("Game Over!!!")
    else:
        print("You have attacked by the piranhas!! Game Over!!!")
else:
    print("By turning right you missed the treasure island route!!Game Over!!!")