import turtle
from tkinter import*
turtle.speed(0)
i = 0
bla = 10 
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