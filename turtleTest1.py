from turtle import *

counter = 0
sides = 8
while counter < sides:
    forward(100)
    left(360/sides)
    counter = counter + 1

circle(100)

done()


