from question_model import Question
from data import easy,hard
from quiz_brain import Quiz_brain

ask_user = input("Enter your difficulty  (Easy/Hard)?: ").lower()
question_bank = []

if ask_user == "easy":
    enter_your_choice = input("Enter the genre your going to play  (Animal/History/Sports/Film/GK)?: ").lower()
    if enter_your_choice == "animal":
        question_data = easy[1]
    elif enter_your_choice == "history":
        question_data = easy[0]
    elif enter_your_choice == "sports":
        question_data = easy[2]
    elif enter_your_choice == "film":
        question_data = easy[3]
    elif enter_your_choice == "gk":
        question_data = easy[4]
    else:
        exit()

else:
    enter_your_choice = input("Enter the genre your going to play  (Animal/History/Sports/Film/GK)?: ").lower()
    if enter_your_choice == "animal":
        question_data = hard[1]
    elif enter_your_choice == "history":
        question_data = hard[0]
    elif enter_your_choice == "sports":
        question_data = hard[2]
    elif enter_your_choice == "film":
        question_data = hard[3]
    elif enter_your_choice == "gk":
        question_data = hard[4]
    else:
        exit()

for i in range(len(question_data)):
    text = question_data[i]["question"]
    answer = question_data[i]["correct_answer"]
    new_question = Question(text,answer)
    question_bank.append(new_question)

quiz_brain = Quiz_brain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz..")
print(f"Your final score is {quiz_brain.score}/{len(question_bank)}")