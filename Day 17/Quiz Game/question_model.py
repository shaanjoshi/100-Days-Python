#Step 1- Creating question class
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
    def __repr__(self):
        return f"{self.text},{self.answer}"
    
        
# new_q = Question("asass", "False")        #way of putting question manually
# print(new_q.text)

#Step 2- #Creating lists of question object from data



        