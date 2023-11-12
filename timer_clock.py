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

# create a function to display the time
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
        canvas.create_line(x1, y1, x2, y2, width=3) #hour mark

    time= strftime("%H:%M:%S").split(':')
    hour_angle = -int(time[0]) * 30  - int(time[1]) / 2
    minute_angle = -int(time[1]) * 6 - int(time[2]) /10
    second_angle = -int (time[2]) * 6

# draw them on the clock
    draw_clock_hand(hour_angle, 60,8,'blue')
    draw_clock_hand (minute_angle, 90, 5, 'green')
    draw_clock_hand(second_angle, 100, 2, 'red')

    canvas.after(1000,draw_the_clock)

def draw_clock_hand(angle, length,width,color):
    x= 200 + length * math.cos(math.radians(angle))
    y= 200 - length * math.sin(math.radians(angle))
    canvas.create_line(200,200,x,y,width=width, fill=color) #clock hand

# call your functions to start the clock
time_update()
draw_the_clock()

root.mainloop()

