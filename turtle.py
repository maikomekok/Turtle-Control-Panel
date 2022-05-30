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
square=Button(frame,text="კვად.",bg="white",fg="black",width=6,bd=4,command=square)
square.grid(row=2,column=1)
lab1=Label(frame,text="სიგრძე-->")
lab1.grid(row=2,column=2)
disp1=Entry(frame,textvariable=inp1,width=6,bd=4)
disp1.grid(row=2,column=3)
dire1=Button(frame,text="<->",bg="white",fg="blue",bd=4,command=mim)
dire1.grid(row=2,column=0)
disp11=Entry(frame,textvariable=inp11,width=6,bd=4,bg="light grey")
disp11.grid(row=2,column=4)


triangle=Button(frame,text="სამკ.",bg="white",fg="black",width=6,bd=4,command=triangle)
triangle.grid(row=3,column=1)
lab2=Label(frame,text="სიგრძე-->")
lab2.grid(row=3,column=2)
disp2=Entry(frame,textvariable=inp2,width=6,bd=4)
disp2.grid(row=3,column=3)
dire2=Button(frame,text="<->",bg="white",fg="blue",bd=4,command=mim)
dire2.grid(row=3,column=0)
disp12=Entry(frame,textvariable=inp12,width=6,bd=4,bg="light grey")
disp12.grid(row=3,column=4)


circle=Button(frame,text="წრე",bg="white",fg="black",width=6,bd=4,command=circle)
circle.grid(row=4,column=1)
lab3=Label(frame,text="რადიუსი-->")
lab3.grid(row=4,column=2)
disp3=Entry(frame,textvariable=inp3,width=6,bd=4)
disp3.grid(row=4,column=3)
dire3=Button(frame,text="<->",bg="white",fg="blue",bd=4,command=mim)
dire3.grid(row=4,column=0)
disp13=Entry(frame,textvariable=inp13,width=6,bd=4,bg="light grey")
disp13.grid(row=4,column=4)

def circlif():
  global bla
  bla=10
  c=0
  coloros = [
#reddish colors
(1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
#orangey colors
(1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
#yellowy colors
(1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
#greenish colors
(0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
#blueish colors
(0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)]
  for f in range(91):
    if bla !=10:
      break
    elif c==len(coloros):
      c=0
      co=coloros[c]
      turtle.color(co)
      c=c+1
    else:
      co=coloros[c]
      turtle.color(co)
      c=c+1
    turtle.forward(100)
    turtle.back(100)
    turtle.left(4)



def spiral():
  global bla
  bla=10
  colors1=["red","purple","blue","green","yellow","orange"]
  turtle.speed(0)
  turtle.bgcolor("black")
  for x in range(360):
    if bla !=10:
      break
    turtle.color(colors1[x%6])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(59)
spir=Button(frame,text="სპირალი",bg="Turquoise",fg="Tomato",width=8,bd=4,command=spiral)
spir.grid(row=5,column=0)
washla=Button(frame,text="გასუფთავება",bg="BurlyWood",fg="LightCyan",width=30,bd=4,command=washlai)
washla.grid(row=5,columnspan=5)
rain=Button(frame,text="სპირალი",bg="Turquoise",fg="Tomato",width=8,bd=4,command=circlif)
rain.grid(row=5,column=4)


root.mainloop()