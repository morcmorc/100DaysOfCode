from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

question_bank = []
for entry in question_data:
    quest = Question(entry["text"],entry["answer"])
    question_bank.append(quest)

quiz = Quiz_Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
score = quiz.score
print(f"Youf final score was {score}/{len(question_bank)}")