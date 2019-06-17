from turtle import*

shape("circle")
shapesize(5,1,2)
fillcolor("blue")
pencolor("purple")

penup()
goto(0,-100)

for i in range(72):
  forward(10)
  left(5)
  tilt(7.5)
  stamp()

exitonclick()