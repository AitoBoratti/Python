from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from os import system as sys

sys('cls')
question_list = []
for data in question_data:
    question_list.append(Question(data["text"],data["answer"]))
quiz = QuizBrain(question_list)
while quiz.still_has_question():
    answers = quiz.next_question()
    quiz.check_answer(answers)
print("You´ve completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}!")
