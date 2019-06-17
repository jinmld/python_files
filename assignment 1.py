import turtle

barlow = turtle.Turtle()
barlow.clear()
barlow.color("blue")
barlow.shape("turtle")
barlow.speed(2)

barlow.forward (100)

barlow.clear()

for c in range(4):
	barlow.forward(100)
	barlow.left(90)

barlow.clear()

for t in range (3):
	barlow.forward(100)
	barlow.left(120)

barlow.clear()

for r in range (2):
	barlow.forward(100)
	barlow.left(90)
	barlow.forward(50)
	barlow.left(90)

barlow.clear()

#5 pentagon
barlow.forward(108)
barlow.left(73)
barlow.forward(108)
barlow.left(70)
barlow.forward(108)
barlow.left(75)
barlow.forward(108)
barlow.left(70)
barlow.forward(108)

barlow.clear()
barlow.left(72)

#6 hexagon
barlow.forward(108)
barlow.left(60)
barlow.forward(108)
barlow.left(60)
barlow.forward(108)
barlow.left(60)
barlow.forward(108)
barlow.left(60)
barlow.forward(108)
barlow.left(60)
barlow.forward(108)

barlow.clear()

#7 septagon
barlow.forward(100)
barlow.left(52)
barlow.forward(100)
barlow.left(52)
barlow.forward(100)
barlow.left(52)
barlow.forward(100)
barlow.left(52)
barlow.forward(100)
barlow.left(52)
barlow.forward(100)
barlow.left(52)
barlow.forward(100)

barlow.clear()

barlow.circle(100)

barlow.clear()

barlow.forward(180)
barlow.left(90)
barlow.forward(100)
barlow.left(120)
barlow.forward(150)
