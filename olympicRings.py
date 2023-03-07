from turtle import *

radius = 100
dist = 2 * radius + 20
pensize(7)

# circle 1
penup()
goto(-200, 100)
color("blue")
pendown()
circle(radius)

# circle 2
penup()
forward(dist)
color("black")
pendown()
circle(radius)

# circle 3
penup()
forward(dist)
color("red")
pendown()
circle(radius)

# circle 4
penup()
goto(-200 + radius, 100 - radius)
color("yellow")
pendown()
circle(radius)

# circle 5
penup()
forward(dist)
color("green")
pendown()
circle(radius)

done()
