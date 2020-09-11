import turtle
turtle.penup()
turtle.goto(-300,300)
for i in range(0,6):
    turtle.goto(-300,300-(100*i))
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()

	
turtle.penup()
turtle.goto(-300,300)
turtle.right(90)
for i in range(0,6):
    turtle.goto(-300+(100*i),300)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()

turtle.exitonclick()
