import math
from tkinter import *
tk=Tk()
tk.title("Python Graph")
tk.wm_attributes("-topmost", 1)
tk.resizable(0,0)
canvas=Canvas(tk, width=500, height=500,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
class Circle:
    def drawCircle(self, h, k, r):
        xcoords = []
        ycoords = []
        for x in range(0, r):
            for y in range(0, r):
                if math.ceil(math.sqrt(x*x + y*y)) == r:
                    xcoords.append(x)
                    ycoords.append(y)            
        for x in range(0, len(xcoords)):
            canvas.create_line(xcoords[x]+r, ycoords[x]+r, xcoords[x]+1+r, ycoords[x]+1+r)            
        for x in range(0, len(xcoords)):
            canvas.create_line(-xcoords[x]+r, ycoords[x]+r, -xcoords[x]+1+r, ycoords[x]+1+r)            
        for x in range(0, len(xcoords)):
            canvas.create_line(xcoords[x]+r, -ycoords[x]+r, xcoords[x]+1+r, -ycoords[x]+1+r)            
        for x in range(0, len(xcoords)):
            canvas.create_line(-xcoords[x]+r, -ycoords[x]+r, -xcoords[x]+1+r, -ycoords[x]+1+r)
c=Circle()
c.drawCircle(250, 500, 200)
tk.update()
