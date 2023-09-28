from turtle import Turtle, Screen

neens = Turtle()
screen = Screen()



def move_forward():
    neens.forward(10)

def move_backwards():
    neens.backward(10)

def turn_right():
    neens.right(10)

def turn_left():
    neens.left(10)

def clear_screen():
    neens.clear()
    neens.penup()
    neens.home()
    neens.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)









screen.exitonclick()