import turtle

lapis =  turtle.Pen();

def quadrado():
    for x in range(5):
        lapis.forward(50)
        lapis.right(90)

def espaco_depois_quadrado():
    lapis.left(90)
    lapis.penup()
    lapis.forward(50)
    lapis.pendown()



lapis.color('green','green')

lapis.begin_fill()

quadrado()

lapis.end_fill()




espaco_depois_quadrado()



lapis.color('red', 'red')

lapis.begin_fill()
quadrado()
lapis.end_fill()

input()