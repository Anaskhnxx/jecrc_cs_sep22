# GUI - graphical user interface

# libraries
# 1. tkinter
# 2. pYQt
# 3. turtle

import tkinter as ttk
app = ttk.Tk()
app.title("my app")
app.geometry('600x400')

msg = ttk.Variable(app)
result = ttk.Variable(app)
# print(msg.get())
# msg.set('empty')
# print(msg.get())

f1 = ttk.Variable(app)
f1. set('0')
f2 = ttk.Variable(app)
f2.set('0')

#ttk.Label(app, text = 'a simple Text Lable'). place(x=50 , y=50)
#ttk.Label(app , textvariable=msg,font='algerian' ).place(x=100 , y= 70)


ttk.Entry(app,  textvariable=f1, font=('Arial', 22)).place(x=50, y=200)
ttk.Entry(app, textvariable=f2, font=('Arial', 22)).place(x=150, y=200)

ttk.Label(app, text='Result is:').place(x=100, y=300)
ttk.Label(app, textvariable=result, font=('arial', 22)).place(x=100, y=330)
# def abc ():
#   print ('wow')
# msg.set('jp tera man kare ')

# ttk.Button(app, text = 'isko click krdo' , command  = abc ).place(x= 100 , y=100)


# ttk.Button(app, text = 'ye wala bhi h ' , command  = lambda:msg.set('pta nhi')).place(x= 100 , y=130)


def calci(op):
    print('i will calculate')
    result.set(eval(f1.get()+op+f2.get()))


ttk.Button(app, text='+', command=lambda: calci('+'),
           font=('Arial', 22)).place(x=50, y=240)
ttk.Button(app, text='-', command=lambda: calci('-'),
           font=('Arial', 22)).place(x=100, y=240)
ttk.Button(app, text='*', command=lambda: calci('*'),
           font=('Arial', 22)).place(x=150, y=240)
ttk.Button(app, text='/', command=lambda: calci('/'),
           font=('Arial', 22)).place(x=200, y=240)

box = ttk.Listbox(app , height= 5, fg = 'red', activestyle='dotbox')
box.insert(1, 'sample1')
box.insert(2, 'sample2')
box.insert(3, 'sample3')
box.place(x=350 , y=40)

def show():
    print(box.get(box.curselection()))

ttk.Button(app , text = 'show' , command=show).place(x=350 , y= 250)


app.mainloop()
