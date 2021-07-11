from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    #question_bank is created to hv the format just as much is min required, (question, ans) pair.

questions_obj = QuizBrain(question_bank)
quiz_ui= QuizUI(questions_obj)#this line kinda links GUI window with the backend.

#while quiz.still_has_questions():
#    quiz.next_question()

