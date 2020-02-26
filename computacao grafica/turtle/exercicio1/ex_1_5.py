import turtle;

def janela():
    lapis = turtle.Pen()

    lapis.color('black', 'blue')

    lapis.begin_fill()

    for x in range(4):
        lapis.forward(50)
        lapis.right(90)

    lapis.penup()
    lapis.left(180)
    lapis.pendown()

    for x in range(4):
        lapis.forward(50)
        lapis.left(90)

    lapis.penup()
    lapis.right(90)
    lapis.pendown()

    for x in range(4):
        lapis.forward(50)
        lapis.left(90)

    for x in range(4):
        lapis.forward(50)
        lapis.right(90)

    
    lapis.end_fill()

def porta():
    lapis = turtle.Pen()

    lapis.color('black', 'brown')

    lapis.begin_fill()

    for x in range(4):
        if x%2==0 :
            lapis.forward(50)
        else:
            lapis.forward(100)
        
        lapis.right(90)

    lapis.end_fill()

    
    lapis.right(90)
    lapis.penup()
    lapis.forward(50)
    lapis.left(90)
    lapis.forward(10)
    lapis.pendown()
    
    lapis.color('black', 'black')
    lapis.begin_fill()
    lapis.circle(5)
    lapis.end_fill()


#janela()
porta()
input()