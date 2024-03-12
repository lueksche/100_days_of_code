from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
all_turtles = {}


is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

def initiate_turtle(color):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    return turtle

for i, color in enumerate(colors):
    turtle = initiate_turtle(colors[i])
    turtle.penup()
    if i % 2 == 0:
        turtle.goto(-230, 25*i)
    else:
        turtle.goto(-230, -25*(i+1))
    all_turtles[color] = turtle

if user_bet:
    is_race_on = True


print(all_turtles["red"])

# while is_race_on:
#       for key in all_turtles:
#         turtle = all_turtles[key]
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've won! The {winning_color} turtle is the winnner!")
#             else:
#                 print(f"You've lost! The {winning_color} turtle is the winnner!")
#         rand_distance = randint(0, 10)
#         turtle.forward(rand_distance)


while is_race_on:
      for key, value in all_turtles.items():
        if value.xcor() > 230:
            is_race_on = False
            winning_color = value.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winnner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winnner!")
        rand_distance = randint(0, 10)
        value.forward(rand_distance)



my_screen.exitonclick()

# for color in colors:
#     print(color)
    
# screen = Screen()
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


# screen.exitonclick()