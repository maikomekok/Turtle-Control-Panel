import turtle
from tkinter import*
turtle.speed(0)
i = 0
bla = 10 
#main Functions
def colorred():
  turtle.color("red")

def colorblue():
  turtle.color("blue")

def colororange():
  turtle.color("orange")

def coloryellow():
  turtle.color("yellow")

def turtleshape():
  shapes=["arrow",'turtle', 'circle', 'square', 'triangle', 'classic']
  global i
  if i==len(shapes):
    i=0
    turtle.shape(shapes[int(i)])
    i+=1
  else:
    turtle.shape(shapes[int(i)])
    i+=1

'''arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.'''

root=Tk()
root.title("კუს კონტროლის პანელი")
frame=Frame(root)
frame.pack()
ekr=turtle.Screen()
turtle.tiltangle(90)
inp1=IntVar(root)
inp2=IntVar(root)
inp3=IntVar(root)
inp11=IntVar(root)
inp12=IntVar(root)
inp13=IntVar(root)