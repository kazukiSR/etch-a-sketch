from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forward():
    pen.forward(5)
def rotate_left():
    pen.left(5)
def rotate_right():
    pen.right(5)
def move_back():
    pen.back(5)
def clear():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="a", fun=rotate_left)
screen.onkeypress(key="d", fun=rotate_right)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()