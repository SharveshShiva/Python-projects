import art
import random
import game_data

print(art.logo)

def printing_name(number, what):
    """ This function is used for printing the name position and place of the celebrity. """
    data_new = game_data.data[number]
    name = ""
    position = ""
    place = ""

    for i in data_new:
        if i == "name":
            name = data_new[i]
        if i == "description":
            position = data_new[i]
        if i == "country":
            place = data_new[i]
    if what == "a":
        return f"Compare A: {name}, a {position}, from {place}."
    if what == "b":
        return f"Against B: {name}, a {position}, from {place}."

def higher_lower(a, b):
    """ This function is used to compare the followers of a and b and give it as a computer's perspective. """
    followers_a = game_data.data[a]["follower_count"]
    followers_b = game_data.data[b]["follower_count"]
    choice = ""
    if followers_a > followers_b:
        choice = "A"
        return choice
    else:
        choice = "B"
        return choice

def play(input_1, point, random_number, random_number_1):
    """ This is the main logic of the program we compare the followers of a and b to give its correct or wrong. """
    random_3 = random.randint(0, 49)
    if input_1 == higher_lower(random_number_1,random_number):
        point += 1
        no_a = printing_name(random_number, "a")
        no_b = printing_name(random_3, "b")
        print("\n" * 20)
        return no_a, no_b, point, random_3
    else:
        return "over"

score = 0
random_number_1 = random.randint(0, 49)
random_number = random.randint(0,49)
should_continue = True
first_a = printing_name(random_number_1, "a")
first_b = printing_name(random_number, "b")
while should_continue:
    print(first_a)
    print(art.vs)
    print(first_b)
    more_followers = input("Who has more followers? Type 'A' or 'B': ").upper()
    if play(more_followers,score,random_number, random_number_1) != "over":
        first_a, first_b, score, random_3 = play(more_followers,score,random_number,random_number_1)
        print(f"You are right! current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        should_continue = False
    random_number_1 = random_number
    random_number = random_3
