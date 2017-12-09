import turtle

def draw():

    window = turtle.Screen()
    obj = turtle.Turtle()
    obj.shape("turtle")
    obj.forward(200)
    obj.right(90)
    obj.forward(100)
    obj.right(90)
    obj.forward(200)
    obj.right(90)
    obj.forward(100)
    obj.right(90)

    obj_1 = turtle.Turtle()
    obj_1.circle(150)
    window.exitonclick()
    
draw()
