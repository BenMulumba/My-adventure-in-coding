import tkinter as tk
from time import strftime
import math

#  settings for the look of the clock
root = tk.Tk()
root.title('BMB clock')

canvas = tk.Canvas(root,width=400,height=400,bg='white')
canvas.pack()

label =tk.Label(root,font=('arial', 14, 'bold'), background='white', foreground='black')
label.pack(anchor='center')

# creat a function to display the time
def time_update():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000,time_update)

# draw the clock using canvas
def draw_the_clock():
    canvas.delete('all')
    canvas.create_oval(10, 10,390,390, width=2) #clock face

    for i in range(12):
        angle = -i * 30
        x1 = 200 + 160 * math.cos(math.radians(angle))
        y1 = 200 - 160 * math.sin(math.radians(angle))
        x2 = 200 + 180 * math.cos(math.radians(angle))
        y2 = 200 - 180 * math.sin(math.radians(angle))
        canvas.create_line(x1, y1, x2, y2, width=3)

# call your functions to start the clock
time_update()
draw_the_clock()

root.mainloop()

