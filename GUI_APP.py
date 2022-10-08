# GUI - graphical user interface 

# libraries 
# 1. tkinter 
# 2. pYQt
# 3. turtle

import tkinter as ttk
app = ttk.Tk()
app.title("my app")
app.geometry('600x400')

ttk.Label(app, text = 'a simple Text Lable'). place(x=50 , y=50)
ttk.Label (app, text  = 'anas khan'  ).place(x= 20 , y=20)
ttk.Label (app, text  = 'awasthi'  ).place(x= 10 , y=70)



app.mainloop()
