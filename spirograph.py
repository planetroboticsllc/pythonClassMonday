from turtle import *
i = 1
pendown()
pensize(2)
color("red", "yellow")
begin_fill()
while True:
    forward(200)
    left(130)
    if abs(pos()) < 1:
        break
end_fill()

done()
