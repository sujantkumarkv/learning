from tkinter import *
import random

#from data import Data
#questions= Data()

from quiz_brain import QuizBrain
#obj= QuizBrain(questions)


BG_COLOR = "#375362"
RED_BLUSH= '#BC544B'
GREEN_SEAFOAM= '#3DED97'

QUESTION_BLOCK_WIDTH=300
QUESTION_BLOCK_HEIGHT=300
FONT_NAME= 'Arial'

#question= random.choice(Data())['question']

class QuizUI:
    
    def __init__(self, questions_obj):
        #self.score_count= 0
        self.questions_obj= questions_obj 
        #An obj of this class equals the questions_obj(OBJECT OF QuizBrain) passed above, simply 
        #this class' object has now properties of QuizBrain class from quiz_brain.py.
        self.window= Tk()
        self.window.title('GUI Quiz')
        self.window.config(bg=BG_COLOR, padx=21, pady=21)
        
        self.score_label= Label(text='Score : ', fg='white', bg=BG_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas= Canvas(width=QUESTION_BLOCK_WIDTH, 
                            height=QUESTION_BLOCK_HEIGHT, 
                            bg='white',
                            highlightthickness=0, 
                            )
        self.question= self.canvas.create_text(
            QUESTION_BLOCK_WIDTH/2, QUESTION_BLOCK_HEIGHT/2,
            text= 'question here', 
            width= 0.9 * QUESTION_BLOCK_WIDTH,#this is for text fits in block in window :)
            font=(FONT_NAME, 21, 'italic')
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=51)
        
        #buttons
        true_img= PhotoImage(file="quiz/images/true_btn.png")
        self.true_btn= Button(image=true_img, 
                              highlightthickness=0, 
                              bg=BG_COLOR,
                              command=lambda : self.show_feedback('True'),
                              )
        self.true_btn.grid(row=2, column=1)
        
        false_img= PhotoImage(file="quiz/images/false_btn.png")
        self.false_btn= Button(image=false_img,
                               highlightthickness=0, 
                               bg=BG_COLOR,
                               command=lambda : self.show_feedback('False'),
                               )
        self.false_btn.grid(row=2, column=0)
        
        self.get_next_question()
        #the above line must be above mainloop() & we needed a function call so as to 
        #each time its called, does two actions -
        #1. calls for next question
        #2. updates the canvas 
        
        self.window.mainloop()
        
        
    def get_next_question(self):
        self.canvas.config(bg='white')
        
        if self.questions_obj.still_has_questions():
            question= self.questions_obj.next_question() #next_question() is an original function of 
                                                        #QuizBrain
            self.canvas.itemconfig(self.question, text=question)
        
        else: #WHEN WE REACH THE END OF GAME - disable the buttons as a cool feature.
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')
            self.canvas.itemconfig(self.question, text='You have completed the game ....')

#   def true_clicked(self):
#        self.show_feedback('True')

        
#    def false_clicked(self):
#        self.show_feedback('False')

# THE ABOVE CODE WAS NECESARRY TILL WE USED {command: true/false_clicked} since WE JUST TRIGGER THE FUNCTION,
# & NOT PASS PARAMETERS or use PARAMETHESIS but that ofc inefficient so we use *LAMBDA FUNCTIONS* like in MATLAB.
    
                
    def show_feedback(self, response):

        if self.questions_obj.check_answer(response):
            #self.score_count += 1
            self.canvas.config(bg=GREEN_SEAFOAM)
                      
        else:
            self.canvas.config(bg=RED_BLUSH)
        
        #CODE LINE BELOW EXPLAINED ....    
        #questions_obj is equal to object of QuizBrain so we can tap into it's attribute of question_list & score :)
        
        self.score_label.config(text= f'Score : {self.questions_obj.score}/{len(self.questions_obj.question_list)}')
        self.window.after(5001, self.get_next_question)
        
        #self.window.after(1001, self.canvas.config(bg='white'))
        # HOW TO DEAL WITH THE COLOR ISSUE SAY THE CODE I WROTE ABOVE, THINK IT THIS WAY - 
        # WE CALL {self.get_next_question}, so we gotta to that part of codebase to change canvas to white again,
        # since THE FLOW OF CODE FLOWS THAT WAY :)
        