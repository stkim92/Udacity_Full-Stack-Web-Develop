import turtle

def draw_rec():
    window = turtle.Screen()
    obj = turtle.Turtle()
    obj.shape("turtle")
    count = 0;
    while(count < 4):
        obj.forward(200)
        obj.right(90)
        count = count + 1
    
    

def draw_circle():
    obj_1 = turtle.Turtle()
    obj_1.circle(150)
    window.exitonclick()
    
draw_rec()
draw_circle()
