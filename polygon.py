# program to create polygon using turtle
from turtle import *
import random

def square(length):
    i = 0
    while i < 4:
        forward(length)
        left(90)
        i = i + 1

def polygon(length, sides):
    if sides < 3 or sides > 10:
        return
    i = 0
    while i < sides:
        forward(length)
        left(360/sides)
        i = i + 1

# square(200)
s = int(input("Enter number of sides: "))
l = int(input("Enter length of a side: "))
polygon(l, s)
done()


