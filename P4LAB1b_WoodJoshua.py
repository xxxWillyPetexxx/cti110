import turtle
wn = turtle.Screen()
josh = turtle.Turtle()

josh.penup()

josh.goto(-30,50)
josh.pendown()
josh.pensize(22)
josh.pencolor('blue')

josh.forward(10)
josh.right(90)
josh.forward(120)
josh.circle(-50,180)

josh.penup()

josh.goto(30,50) 
josh.pendown()
josh.pensize(22)
josh.pencolor('red')
josh.right(165)
josh.forward(160)
josh.left(140)
josh.forward(150)

josh.right(130)
josh.forward(150)
josh.left(140)
josh.forward(160)

wn.mainloop()
