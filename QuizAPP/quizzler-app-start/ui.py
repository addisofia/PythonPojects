from question_model import Question
from tkinter import Tk, Canvas, Button, PhotoImage, Label,Entry
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"



class Quizinterface :
    def __init__(self,quiz_brain:QuizBrain):
        self.window=Tk()
        self.quiz = quiz_brain

        self.window.title("QUIZ")
        self.window.minsize(width=800,height=800)
        self.window.config(padx=200,pady=120,bg=THEME_COLOR)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.canvas.grid(column=0,row=1,columnspan=2,padx=20,pady=20)

        self.text_q=self.canvas.create_text(150, 125,text="start",width=200, font=("Arial",15,"italic"))

        self.image1=PhotoImage(file="images/true.png")
        self.image2=PhotoImage(file="images/false.png")

        self.ok_button=Button(image=self.image1,command=self.check_true)
        self.ok_button.grid(column=0,row=2)


        self.nok_button=Button(image=self.image2,command=self.check_false)
        self.nok_button.grid(column=1,row=2)

        self.score_i=Label(text=" Score:0",font=("Arial",10,"bold"),bg=THEME_COLOR,fg="white")
        self.score_i.grid(column=1,row=0)


        self.next()

        self.window.mainloop()

    def next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            ques_text=self.quiz.next_question()
            self.canvas.itemconfig(self.text_q,text=ques_text)
        else:
            self.canvas.itemconfig(self.text_q,text="you reach the end of the quiz")
            self.ok_button.config(state="disabled")
            self.nok_button.config(state="disabled")

    def check_true(self):
        self.feed_back(self.quiz.check_answer("True"))


    def check_false(self):
        self.feed_back(self.quiz.check_answer("False"))

    def feed_back(self,iscorrect):
        if iscorrect:
            self.score_i.config(text=f"score:{self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(2000, self.next)



