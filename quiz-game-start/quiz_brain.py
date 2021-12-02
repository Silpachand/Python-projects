class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        i = 0
        while i < len(self.question_list):
            current_question = self.question_list[self.question_num]
            self.question_num += 1
            user = input(f"Q. {self.question_num} : {current_question.text} (True/False) : ")
            if current_question.answer.lower() == user.lower() :
                self.score += 1
                print("You got it right!!!")
            else:
                print("That's wrong!")
            print(f"The correct answer was : {current_question.answer}")
            print(f"Current score is : {self.score}/ {i+1}")
            print("\n")
            i += 1
        return self.score