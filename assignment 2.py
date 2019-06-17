import turtle, time
t=turtle.Turtle()
x=5
for i in range (6):
  x=x*2
  for i in range (4):
    t.forward(x)
    t.right(90)  
       
    
t.hideturtle()
time.sleep(2)
t.showturtle()
t.clear()

x=5
for i in range (6):
  x=x*2
  for i in range(3):
    t.forward(x)
    t.right(120)


t.hideturtle()
time.sleep(2)
t.showturtle()
t.clear()

x=5
for i in range (6):
  x=x*2
  for i in range (5):
    t.forward(x)
    t.right(72)

t.hideturtle()
time.sleep(2)
t.showturtle()
t.clear()

x=5
for i in range (6):
  x=x*2
  for i in range (6):
    t.forward(x)
    t.right(60)