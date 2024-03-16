import time
from tkinter import *
import random
TimerEnabled = True
sentences = ["каждую осень птицы улетают на юг","я делаю домашнее задание","кошка тщательно умывает мордочку","весной на деревьях распускаются листики","в город ворвалась зима"]
t_stop = 0
sentence = ""
t_start = 0
best_result = 0
wnd = Tk()
wnd.title = "Главное меню"
wnd.resizable = (True,True)
wnd.geometry("1200x600")
t_run = 0
def speed_typing():
  global t_start
  t_start = time.monotonic()
      #time.sleep(1)
     
def again():
   global t_start     
   global t_stop
   global t_run 
   global ent
   ent.delete(0,END)
#    ent.insert(0,"")
   t_start = 0
   t_stop = 0
   t_run = 0
   label2.configure(text="")
   label3.configure(text= "")
   label1.configure(text= "")


def stop():
  global t_stop
  t_stop = time.monotonic()

def new_sentence():
    global sentences
    global sentence
    sentence = random.choice(sentences)
    label1.configure(text= str(sentence))


def ready():
  global t_stop
  global t_start
  global best_result
  global sentence
  t_run = t_stop - t_start
  if str(ent.get()) == str(sentence):
    label2.configure(text="Правильно")
    t_run = t_stop - t_start
    label3.configure(text= str(t_run))
    if t_run < best_result or best_result == 0:
        best_result = t_run
        label5.configure(text= str(best_result))
  else:
    label2.configure(text="Неправильно")



ent = Entry(wnd,width=20)
ent.place(x = 200,y = 200)

btn1 = Button(wnd,text = "начать",command=speed_typing)
btn1.place(x = 100,y = 200)

btn3 = Button(wnd,text = "стоп",command=stop) 
btn3.place(x = 400,y = 200)

btn4 = Button(wnd,text = "посмотеть результат",command=ready) 
btn4.place(x = 450,y = 200)

btn2 = Button(wnd,text = "новое предложение",command=new_sentence)
btn2.place(x = 250,y = 100)

btn5 = Button(wnd,text = "начать заново",command=again)
btn5.place(x = 200,y = 300)

label1 = Label(wnd,text = "" ,font=("Times New Roman",14))
label1.place(x = 100,y = 150)

label3 = Label(wnd,text = "" ,font=("Times New Roman",14))
label3.place(x = 100,y = 100)

label2 = Label(wnd,text = "" ,font=("Times New Roman",14))
label2.place(x = 10,y = 10)

label4 = Label(wnd,text = "лучший  результат:" ,font=("Times New Roman",14))
label4.place(x = 650,y = 200)

label5 = Label(wnd,text = "" ,font=("Times New Roman",14))
label5.place(x = 650,y = 300)

wnd.mainloop()

# Замеряем время начала выполнения программы
#t_start = time.monotonic()
# здесь код 'main()' программы
#time.sleep(1)
# Замеряем время окончания выполнения программы
#t_stop = time.monotonic()
# вычисляем разницу во времени
#t_run = t_stop - t_start
# 1.0023079550010152
