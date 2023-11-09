# import tkinter, time, and datetime
from tkinter import * 
import time
from datetime import datetime

# configue your  GUI
root=Tk()
root.config(background='black')
root.title('BMB_clock')
root.geometry('400x300')

# create a function to display the date and time 
def clock():
    hour=time.strftime('%H')
    minute=time.strftime('%M')
    second=time.strftime('%S')
    day= time.strftime('%A')
    month= time.strftime('%m')
    year = time.strftime('%y')
    labe1.config(text= hour + ':' + minute + ':' + second)
    labe1.after(1000, clock)
    label2.config(text=day + ';' + month + ':' + year)

# config the time label
labe1= Label(root, text='', font='times, 48', fg='#033a06', bg='black')
labe1.pack(pady=15)

# config the date label
label2= Label(root, text='', font='times,20', fg='#012703', bg='black')
label2.pack(pady=30)


clock()





root.mainloop()