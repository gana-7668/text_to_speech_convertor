import tkinter as tk
from tkinter import*
import pyttsx3

engine=pyttsx3.init()
engine.setProperty("rate",140)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
pyttsx3.speak("hello ganesh you write text and i am converting speech." )

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()
    

root=Tk()
root.title("Text to speech")
root.geometry("500x300")
root.config(bg="pink")

textv=StringVar()

obj=LabelFrame(root,text="Text to speech",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lbl=Label(obj,text="Text",font=30)
lbl.pack(side=tk.LEFT,padx=5)


text=Entry(obj,textvariable=textv,font=30,width=35,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="speak",font=20,bg="black",fg="red",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)


root.mainloop()


'''
for i in range(1,6):
    for j in range(1,6):
     print("*",end="")

    print("")    
  

no_rows=int(input("enter the number:"))
for row in range(1,no_rows+1):
    for coloum in range(1,row+1):
        print(coloum,end="")
    print("")    

for row in range(no_rows-1,0,-1):
    for coloum in range(1,row+1):
        print(coloum,end="")
    print("")'''


'''no_rows = int(input ("enter the no. of rows ="))
for row in range(1,no_rows+1):
    for coloum in range (1,row+1):
        print("{0}{1}".format(row,coloum) ,end=" ")
    print()    

for row in range(no_rows-1,0,-1):
    for coloum in range (1,row+1):
         print("{0}{1}".format(row,coloum) ,end=" ")
    print()'''