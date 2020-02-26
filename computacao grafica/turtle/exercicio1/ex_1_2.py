import turtle

lapis = turtle.Pen()

lapis.color('red', 'green')

lapis.begin_fill()

for x in range(5):
    lapis.forward(100)
    lapis.right(90)

lapis.left(90)
lapis.penup()
lapis.forward(50)
lapis.pendown

for x in range(5):
    lapis.forward(100)
    lapis.right(90)

lapis.end_fill()

input()