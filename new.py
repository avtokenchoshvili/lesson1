from turtle import *


speed(20)
penup()
goto(-300,-350)
pendown()
title("house")

#Walls
width(10)
color("black")
forward(600)
left(90)
forward(500)
left (90)
forward(600)
left(90)
forward(500)
left (90)


#door

penup
goto(-100,-350)
pendown
color("red")
begin_fill()
left(90)
forward(130)
right(90)
forward(70)
right(90)
forward(130)
end_fill()



#roof


penup()
goto(300,150)
pendown()
color("red")
begin_fill()
right(120)
forward(360)
left(62)
forward(340)
end_fill()


penup()
goto(-300,-50)
pendown()
color("yellow")
begin_fill()
left(148)
forward(200)
right(90)
forward(100)
left(-90)
forward(200)
end_fill()



penup()
goto(-200,-50)
pendown()
color("red")
left(90)
forward(100)




color("red")
penup()
goto(-300,-100)
pendown()
left(90)
forward(200)


penup()
goto(300,-150)
pendown()
color("yellow")
begin_fill()
left(180)
forward(200)
right(90)
forward(100)
right(90)
forward(200)
end_fill()

penup()
goto(200,-150)
pendown()
color("red")
left(90)
forward(100)




penup()
goto(300,-100)
pendown()
color("red")
left(90)
forward(200)


exitonclick()