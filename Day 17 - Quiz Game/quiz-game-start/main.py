from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    Questions = Question(i["question"], i["correct_answer"])
    question_bank.append(Questions)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print("You have completed the quiz !")
print(f"Your final score is {new_quiz.score}/{new_quiz.question_number} !")

#print(question_bank[0].text)
#print(len(question_bank))