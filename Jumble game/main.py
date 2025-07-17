import random
from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(background='black')
window.geometry("900x900+1000+500")
score = 0
word = ''

scrambled = ['plpea','gnoma','annaba','hveeica','lkaatko','egvnine','aestnrv','iceever','lndono','rrreifa','wllhoo','oohrrr','rtemsa','nnrgimo','lttobe','enp','ourrte','ypco','rraonw','wdie','ievd','elov','klboc','ightr','plmsie','dfea','glneis','ghtkni','opeh']
unscrambled = ['apple','mango','banana','achieve','kolkata','evening','servant','receiver','london','ferrari','hollow','horror','master','morning','bottle','pen','router','copy','narrow','wide','dive','love','block','right','simple','deaf','single','knight','hope']

num = random.randrange(0,len(unscrambled),1)
count = 0

def create_words():
    global num
    num = random.randrange(0,len(unscrambled),1)
    word = scrambled[num]
    label_2.config(text=word)
    entry.delete(0,END)

def check_answer():
    global num,count,score
    if unscrambled[num] == entry.get():
        score += 1
        count = int(count+1)
        messagebox.showinfo('Message','Correct')
    else:
        count = int(count+1)
        messagebox.showinfo('Message','Your wrong')
        
label_1 = Label(window,text='Jumble Word Game',fg='white',bg='black',font=('arial',75))
label_1.grid(row=0,column=0)
label_2 = Label(window,fg='white',bg='black',font=('arial',30),pady=30)
label_2.grid(row=1,column=0)
entry = Entry(window,font=('arial',30),)
entry.grid(row=2,column=0)
button_1 = Button(window,text='check',fg='green',bg='dark gray',width = 10,height=1,font=('arial',30),command=check_answer)
button_2 = Button(window,text='reset',fg='yellow',bg='gray',width = 10,height=1,font=('arial',30),command=create_words)
button_1.grid(row=3,column=0,pady=30)
button_2.grid(row=4,column=0,pady=10)

create_words()

window.mainloop()