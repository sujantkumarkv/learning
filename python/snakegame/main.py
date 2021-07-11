import turtle
import time
import snake
import food
import scoreboard

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

screen = turtle.Screen()
screen.title("Faaltu saa SNAKE GAME")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
# bauaa = turtle.Turtle(shape="square")
# bauaa.color("white")
screen.tracer(n=0)
# screen.update()

# OBJECT CREATION ::
snake = snake.Snake()
food = food.Food()
score = scoreboard.ScoreBoard()
##########################################
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.first_turtle.distance(food) < 15:
        snake.extend()
        food.new_pos()
        score.update_score()

    if snake.first_turtle.xcor() > 340 or snake.first_turtle.xcor() < -340 or snake.first_turtle.ycor() > 340 or snake.first_turtle.ycor() < -340:
        game_is_on = False
        score.game_over()

    # Detect collision with its own body:
    ### for bauaa in snake.bauaas_list:
    #     #Need to bypass finding distance of 1st_turtle(snake's head) with itself
    #     if bauaa == snake.first_turtle:
    #         continue
    #     # If yes, trigger GAME OVER .###
    # The code above is lengthy so we use slicing to simply get hold of all elements of bauaas_list except 1st one(head)
    for bauaa in snake.bauaas_list[1:]:
        if snake.first_turtle.distance(bauaa) < 10:
            # first loop wil give first_turtle(bauaa1) only so its distance is DEF <11; So we get GAME OVER immediately.
            game_is_on = False
            score.game_over()

screen.exitonclick()
