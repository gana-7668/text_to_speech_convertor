from tkinter import*
from datetime import date

root=Tk()
root.title("age calculator")
root.geometry("700x500")
root.config(bg="grey")

def calculatorage():
    today=date.today()
    birthDate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year - birthDate.year - ((today.month,today.day)<(birthDate.month,birthDate.day))
    Label(text=f"{namevalue.get()} your age is {age}",font=30,bg="black",fg="red").place(x=250,y=410)


label= Label(root,text="\U0001F618""AGE CALCULATOR""\U0001F618",font=("time new roman",30,"bold"),bg="orange",fg="white")
label.place(x=150,y=40,height=50,width=450)

Label(text="NAME : ",font=23,bg="black",fg="red").place(x=100,y=150)
Label(text="YEAR : " ,font=23,bg="black",fg="red").place(x=100,y=200)
Label(text="MONTH : ",font=23,bg="black",fg="red").place(x=100,y=250)
Label(text="DAY : ",font=23,bg="black",fg="red").place(x=100,y=300)


namevalue=StringVar()
yearvalue=StringVar()
monthvalue=StringVar()
dayvalue=StringVar()

nameEntry=Entry(root,textvariable=namevalue,width=30,bd=3,font=20)
nameEntry.place(x=200,y=150)

yearEntry=Entry(root,textvariable=yearvalue,width=30,bd=3,font=20)
yearEntry.place(x=200,y=200)

monthEntry=Entry(root,textvariable=monthvalue,width=30,bd=3,font=20)
monthEntry.place(x=200,y=250)

dayEntry=Entry(root,textvariable=dayvalue,width=30,bd=3,font=20)
dayEntry.place(x=200,y=300)

Button(text="AGE CALCULATE",font=20,bg="black",fg="red",width=20,height=2,command=calculatorage).place(x=210,y=350)






root.mainloop()

