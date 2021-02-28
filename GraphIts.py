from tkinter import *
tk=Tk()
tk.title("Python Graph")
tk.wm_attributes("-topmost", 1)
tk.resizable(0,0)
canvas=Canvas(tk, width=500, height=500,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
class Graph:
    def __init__(self):
        self.placeholder=False
    def planGraph(self):
        self.placeholer=True
        yCoordinates = []
        for x in range(0, 500):
            yCoordinates.append(round(x/4, 0))
        return yCoordinates
    def graph(self):
        yCoordinates = self.planGraph()
        for x in range(0, 500):
            canvas.create_line(x, yCoordinates[x], x+1, yCoordinates[x]+1)

g=Graph()
g.graph()
