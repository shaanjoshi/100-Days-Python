from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)      #Here we have created an object "new_question" useing "Question" class
    question_bank.append(new_question)


print(question_bank)         #to understand







