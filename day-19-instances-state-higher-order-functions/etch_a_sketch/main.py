from turtle import Turtle, Screen

# Turtle characteristics
hirstle = Turtle()
hirstle.pendown()

# Define needed functions


def move_forwards():
    hirstle.forward(10)


def move_backwards():
    hirstle.backward(10)


def turn_clockwise():
    hirstle.right(10)


def turn_anti_clockwise():
    hirstle.left(10)


def clear_screen():
    hirstle.clear()


# Preparing screen
my_screen = Screen()
my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="d", fun=turn_clockwise)
my_screen.onkey(key="a", fun=turn_anti_clockwise)
my_screen.onkey(key="c", fun=clear_screen)

my_screen.exitonclick()
