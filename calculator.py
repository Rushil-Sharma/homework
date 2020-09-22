from tkinter import * 
from tkinter import messagebox 
import sys
root = Tk()
root.config(bg='blue')
#1,2,3,4,5,6,7,8,9,0,=,+,-,÷,×,C,Exit
calc_display=StringVar()
operator=''
#=======================Functions=========================
def num(numbers):
    global operator
    operator = operator + str(numbers)
    calc_display.set(operator)
def clear():
    global operator
    operator=''
    calc_display.set('')
def equal():
    try:
        global operator
        xyz=str(eval(operator))
        y=(xyz)
        calc_display.set(y)
        operator=''
    except Exception as e:
        messagebox.showerror('Error','Zero division error')
def exit_cal():
    print('sorry to see you go Bye\n  ')
    sys.exit(0)
help_img = PhotoImage(file='C:\\Users\\rushil\\Downloads\\Help.png')
#=======================Buttons===========================
e = Entry(root,text=calc_display,font=('Helvatica',20),bg='black',fg='white')
b1 = Button(root,text='1',font=('Helvatica',35),command=lambda : num(1))
b2 = Button(root,text='2',font=('Helvatica',35),command=lambda : num(2))
b3 = Button(root,text='3',font=('Helvatica',35),command=lambda : num(3))
b4 = Button(root,text='4',font=('Helvatica',35),command=lambda : num(4))
b5 = Button(root,text='5',font=('Helvatica',35),command=lambda : num(5))
b6 = Button(root,text='6',font=('Helvatica',35),command=lambda : num(6))
b7 = Button(root,text='7',font=('Helvatica',35),command=lambda : num(7))
b8 = Button(root,text='8',font=('Helvatica',35),command=lambda : num(8))
b9 = Button(root,text='9',font=('Helvatica',35),command=lambda : num(9))
b0 = Button(root,text='0',font=('Helvatica',35),command=lambda : num(0))
plus = Button(root,text='+',font=('Helvatica',35),command=lambda : num('+'))
minus = Button(root,text='-',font=('Helvatica',38),command=lambda : num('-'))
division = Button(root,text='÷',font=('Helvatica',35),command=lambda : num('/'))
multi = Button(root,text='×',font=('Helvatica',35),command=lambda : num('*'))
equal_to = Button(root,text='=',font=('Helvatica',35),command=equal)
clear = Button(root,text='C',font=('Helvatica',20),padx=40,bg='dark blue',fg='light blue',command=clear)
exit_calc = Button(root,text='Exit',font=('Helvatica',20),padx=20,bg='dark blue',fg='light blue',command=exit_cal)
#=================================Grid=================================
e.grid(row=0,column=1,columnspan=5)
b1.grid(row=1,column=1)
b2.grid(row=1,column=2)
b3.grid(row=1,column=3)
b4.grid(row=2,column=1)
b5.grid(row=2,column=2)
b6.grid(row=2,column=3)
b7.grid(row=3,column=1)
b8.grid(row=3,column=2)
b9.grid(row=3,column=3)
b0.grid(row=2,column=4)
plus.grid(row=1,column=4)
minus.grid(row=3,column=4)
division.grid(row=1,column=5)
multi.grid(row=2,column=5)
equal_to.grid(row=3,column=5)
clear.grid(row=4,column=1,columnspan=2)
exit_calc.grid(row=4,column=4,columnspan=5)
root.mainloop()
print('Sorry to see you go Bye\n   ')
sys.exit(0)