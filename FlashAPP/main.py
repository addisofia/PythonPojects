
#-----------------create a flash card to translate word from french to english-------------------------
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter import messagebox
import pandas
import random


Green_lite="#daefdf"
Font=("Arial", 20, "bold")
Gen_word=""
after_timer=" None"


#------------------------------------------function------------------------------------------------



#traduct_word = word_list['English'][word_list['French'] == word].to_string(index=False)


def next_word():
      global Gen_word
      global after_timer
      window.after_cancel(after_timer)
      Gen_word = random.choice(french_word)
      canvas.itemconfig(display_word, text=Gen_word)
      canvas.itemconfig(title, text='French')
      canvas.itemconfig(first_image, image=card_front)
      after_timer = window.after(6000, turn_card)


def turn_card():
      english_word=word_dict[Gen_word]
      canvas.itemconfig(title, text='English')
      canvas.itemconfig(display_word, text=english_word)
      canvas.itemconfig(first_image, image=card_back)

def ok_answer():
      global word_list

      word_list = word_list[word_list['French']!= Gen_word]
      print(len(word_list))
      try:
            word_list.to_csv('data/french_words.csv', index=False)
            print("saved")

      except:
            print("not saved")

      else:
           window.after(2000,next_word)






#---------------------------------open file with  pandas to create a french list word--------------------------------#
#with open ('data/french_words.csv',mode='r') as data:
word_list=pandas.read_csv('data/french_words.csv')
word_dict={column.French:column.English for (index,column) in word_list.iterrows()}
french_word=[column.French for(index,column) in word_list.iterrows()]




#-----------------create a GUI interface canvas, Button and all other things  -------------------------


window=Tk()
window.minsize(width=800,height=800)
window.config(padx=100,pady=20,bg=Green_lite)
window.title("Flash card")


#--------- create canvas---------------------------------------------------#

canvas=Canvas()
canvas.config(width=800,height=520,highlightthickness=0,bg=Green_lite)
card_back=PhotoImage(file="image/card_back.png")
card_front=PhotoImage(file="image/card_front.png")
first_image=canvas.create_image(400,260,image=card_front)
canvas.grid(column=0,row=0,columnspan=2)
title=canvas.create_text(400,150,text="French",font=("Arial",20,"italic"),fill="Black")
display_word=canvas.create_text(400,280,text='',font=Font,fill="Black")

#-------- create button ok and  nok--------------------------------------------
right=PhotoImage(file="image/right.png")
wrong=PhotoImage(file="image/wrong.png")
ok_button=Button(image=right,highlightthickness=0,command=ok_answer)
ok_button.grid(column=1,row=1)
nok_button=Button(image=wrong,highlightthickness=0,command=next_word)
nok_button.grid(column=0,row=1)


#------------diplay random word with calling function- and dispaly the traduction ater 5 ms-----------------------#

next_word()
after_id=window.after(6000,turn_card)









window.mainloop()