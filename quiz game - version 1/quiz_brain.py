class Quiz_brain:
    def __init__(self,quiz_list):
        self.quiz_number = 0
        self.quiz_list = quiz_list
        self.score = 0

    def next_question(self):
        current = self.quiz_list[self.quiz_number]
        user_input = input(f"Q.{self.quiz_number+1}: {current.text} (True/False): ")
        self.quiz_number+=1
        self.check_answer(user_input, current.answer)

    def still_has_questions(self):
        if self.quiz_number < len(self.quiz_list):
            return True
        else:
            return False

    def check_answer(self, user_input, correct):
        if user_input.lower() == correct.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct}.")
        print(f"Your current score is: {self.score}/{self.quiz_number}")
        print("\n")
