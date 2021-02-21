from tkinter import *
import random
import string


def genrate_pasword():
    pasword=[]
    for i in range(5):
        alpha =random.choice(string.ascii_letters)
        symbols=random.choice(string.punctuation)
        number=random.choice(string.digits)
        pasword.append(alpha)
        pasword.append(symbols)
        pasword.append(number)
    y=" ".join(str(x) for x in pasword)
    lbl.config(text=y)



root=Tk()
root.geometry("300x300")
btn=Button(root,text="Genrate pasword", command=genrate_pasword)
btn.grid(row=2, column=2)
lbl =Label(root,font =("times",15,"bold"))
lbl.grid(row=4,column=2)
root.mainloop()
