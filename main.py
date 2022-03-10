from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forward():
    pen.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()