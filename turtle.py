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

def mim():
  turtle.right(180)


def washla():
  global bla
  turtle.bgcolor("white")
  bla=20
  print(bla)
  turtle.reset()
  turtle.left(90)
  turtle.speed(0)

  
def square():
  global bla
  bla = 10
  a = inp1.get()
  a1 = inp11.get()
  if a1==0:
    a1=1
  for g in range(a1):
    if bla !=10:
      break
    else:
      for i in range(1,5):
        turtle.forward(a)
        turtle.left(90)
    turtle.right(5)


def triangle():
  global bla
  bla=10
  b=inp2.get()
  b1=inp12.get()
  if b1==0:
    b1=1
  for g in range(b1):
    if bla !=10:
      break
    else:
      for i in range(1,4):
        turtle.forward(b)
        turtle.left(120)
    turtle.left(5)

def circle():
  global bla
  bla=10
  c=inp3.get()
  c1=inp13.get()
  if c1==0:
    c1=1
  for g in range(c1):
    if bla !=10:
      break
    else:
      turtle.circle(c)
    turtle.left(5)
#define colors
red=Button(frame,bg="red",fg="red",width=9,command=colorred)
red.grid(row=1,column=0)
blue=Button(frame,bg="blue",fg="blue",width=8,command=colorblue)
blue.grid(row=1,column=1)
SHAPE=Button(frame,bg="white",fg="green",text="ფორმა",width=11,command=turtleshape)
SHAPE.grid(row=1,column=2)
orange=Button(frame,bg="orange",fg="orange",width=8,command=colororange)
orange.grid(row=1,column=3)
yellow=Button(frame,bg="yellow",fg="yellow",width=9,command=coloryellow)
yellow.grid(row=1,column=4)