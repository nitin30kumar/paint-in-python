from tkinter import *

width = 800
height = 450

def quit_paint():
    import sys;sys.exit()

def paint(event):
    python_green = "#476042"
    x1,y1 = (event.x-1),(event.y-1)
    x2,y2 = (event.x+1),(event.y+1)
    w.create_oval(x1,y1,x2,y2,fill = python_green)

root = Tk()
root.title("Painting using ovals")

w = Canvas(root,width = width , height = height)
w.pack(expand = YES, fill = BOTH)
w.bind("<B1-Motion>",paint)

msg = Label(root,text="Press and Drag the mouse to draw").pack(side=BOTTOM)

Button(root,text="QUIT",bg="green",fg="violet",command=quit_paint())

mainloop()
