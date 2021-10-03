from tkinter import Tk
from tkinter import Canvas

def ROUND(a):
  return int(a + 0.5)

def drawDDA(C,x1,y1,x2,y2):
  x,y = x1,y1
  length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
  dx = (x2-x1)/float(length)
  dy = (y2-y1)/float(length)
  for i in range(length):
    x += dx
    y += dy
    C.create_line(ROUND(x), ROUND(y), x + 1, ROUND(y),fill="white") #puts pixel


root = Tk()
C = Canvas(root, bg="black",height=500, width=500)
drawDDA(C,0,0,50,50)
C.pack()
root.mainloop()