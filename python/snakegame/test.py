import turtle
import random
import time

screen = turtle.Screen()
screen.title("Faaltu saa Simple SNAKE GAME")
screen.setup(width=700, height=700)
screen.bgcolor("black")
starting_positions = [0, -20, -40]  # Since each turtle is 20px long & we are taking 3 to make our initial snake.
# bauaa = turtle.Turtle(shape="square")
#bauaa.color("white")
bauaas_list= []
#screen.tracer(n=0)

for position in range(3):
    new_bauaa = turtle.Turtle(shape="square")
    new_bauaa.color("white")
    new_bauaa.penup()
    new_bauaa.goto(x=starting_positions[position], y=0)
    bauaas_list.append(new_bauaa)

# screen.update()
first_turtle= bauaas_list[0]
for _ in range(3):
    first_turtle.forward(20)
    time.sleep(3)
    second_turtle = bauaas_list[1]
    second_turtle.goto(first_turtle.pos())
    time.sleep(3)
    third_turtle = bauaas_list[2]
    third_turtle.goto(second_turtle.pos())

# game_is_on= True
# while game_is_on:
#     screen.update()
#     time.sleep(0.09)
#
#     # for turtle_segment in bauaas_list: ##PROBLEM WITH THIS LOOP CODE IS IF WE TURN A TURTLE, OTHER 2 WILL KEEP
#     #     turtle_segment.forward(20)    ## ON MOOVING FORWARDS BCZ THAT'S WHAT SAID; INSTEAD BETTER APPROCH IS TO MAKE
#                                          ## FOLLOW EACH TURTLE THE PATH OF THE TURTLE IN-FRONT OF IT.
#
#     first_turtle= bauaas_list[0]
#     first_turtle.forward(20)
#     print(first_turtle.pos())
#
screen.exitonclick()


