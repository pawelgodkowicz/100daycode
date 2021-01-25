from question_model import Question, LoadQuizData
from quiz_brain import QuizBrain

# Json data downloaded from: https://opentdb.com/
load_data = LoadQuizData('api.json')
quiz_data = load_data.data

question_bank = []
for question in quiz_data:
    question_category = question['category']
    question_text = question['question']
    question_correct_answer = question['correct_answer']
    new_question = Question(question_category, question_text, question_correct_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f'Your final score was: {quiz.score}/{quiz.question_number}')

