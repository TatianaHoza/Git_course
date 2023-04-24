from tkinter import *
import time

root = Tk()
root.geometry('300x400')



canvas = c = Canvas(root, width=70, height=190, bg="black")
r = c.create_oval(10, 10, 60, 60, fill="#ff0000")
y = c.create_oval(10, 70, 60, 120, fill="#808000")
g = c.create_oval(10, 130, 60, 180, fill="#008000")
def upd(event):
    global r, g, y, c 
    state = 0
    if state == 0:
        state = 1
        canvas.itemconfigure(r, fill='#800000')
        canvas.itemconfigure(y, fill='#ffff00')
        c.after(500,upd)
    if state == 1:
        state = 2
        canvas.itemconfigure(y, fill='#808000')
        canvas.itemconfigure(g, fill='#00ff00')
        c.after(500,upd)
    if state == 2:
        state = 0
        canvas.itemconfigure(y, fill='#808000')
        canvas.itemconfigure(g, fill='#008000')
        c.after(500,upd)
def pom(event):
    global x, y
    x = event.x
    y = event.y
    pm.post(event.x_root, event.y_root)
mainmenu = Menu(root)

pm = Menu(tearoff=0)
pm.add_command(label='Старт')

c.bind('<Button-3>',pom)

c.pack()
root.mainloop()