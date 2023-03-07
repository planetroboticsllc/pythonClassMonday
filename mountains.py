from turtle import *

pendown()
pensize(2)
color("red", "yellow")
begin_fill()
while True:
    forward(200)
    left(135)
    if abs(pos()) < 1:
        break
end_fill()

penup()
goto(-250, -100)
pendown()
color("black", "brown")
begin_fill()

i = 0
while i < 3:
    forward(200)
    left(120)
    i = i + 1
end_fill()

done()
