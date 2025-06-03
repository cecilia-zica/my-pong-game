from turtle import Screen
from entities.paddle import Paddle
from entities.ball import Ball
from entities.scoreboard import Scoreboard
import time

PADDLE_STARTING_POSITIONS =  [(-350, 0), (350, 0)]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0) #turn off automatic updates

# --- Variables creation---
paddle_left = Paddle(PADDLE_STARTING_POSITIONS[0])
paddle_right = Paddle(PADDLE_STARTING_POSITIONS[1])
ball = Ball()
scoreboard = Scoreboard()

# --- Variables for continuous movement---
# Left Paddle
paddle_left_moving_up = False
paddle_left_moving_down = False
# Right Paddle
paddle_right_moving_up = False
paddle_right_moving_down = False

# --- Functions for beggin the moviment ---
def begin_mov_paddle_left_up():
    global paddle_left_moving_up
    paddle_left_moving_up = True

def begin_mov_paddle_left_down():
    global paddle_left_moving_down
    paddle_left_moving_down = True

def begin_mov_paddle_right_up():
    global paddle_right_moving_up
    paddle_right_moving_up = True

def begin_mov_paddle_right_down():
    global paddle_right_moving_down
    paddle_right_moving_down = True

# --- Functions for beggin the moviment ---
def stop_mov_paddle_left_up():
    global paddle_left_moving_up
    paddle_left_moving_up = False

def stop_mov_paddle_left_down():
    global paddle_left_moving_down
    paddle_left_moving_down = False

def stop_mov_paddle_right_up():
    global paddle_right_moving_up
    paddle_right_moving_up = False

def stop_mov_paddle_right_down():
    global paddle_right_moving_down
    paddle_right_moving_down = False


screen.listen()

# Left Paddle (W and S)
screen.onkeypress(begin_mov_paddle_left_up, "w")
screen.onkeyrelease(stop_mov_paddle_left_up, "w")
screen.onkeypress(begin_mov_paddle_left_down, "s")
screen.onkeyrelease(stop_mov_paddle_left_down, "s")

# Right Paddle (Up and Down)
screen.onkeypress(begin_mov_paddle_right_up, "Up")
screen.onkeyrelease(stop_mov_paddle_right_up, "Up")
screen.onkeypress(begin_mov_paddle_right_down, "Down")
screen.onkeyrelease(stop_mov_paddle_right_down, "Down")

game_is_on = True
GAME_SPEED = 0.08  # less = faster

while game_is_on:
    # 1. Update the screen to show changes
    screen.update()

    # 2. Stop the game for a little time
    time.sleep(GAME_SPEED)

    # 3. ball moving
    ball.move()

    # --- Update Paddle Position Based on State ---
    if paddle_left_moving_up:
        paddle_left.move_up()
    elif paddle_left_moving_down:
        paddle_left.move_down()

    elif paddle_right_moving_up:
        paddle_right.move_up()
    elif paddle_right_moving_down:
        paddle_right.move_down()

    # --- Detect collision with wall ---
    elif ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # --- Detect collision with Paddle ---
    elif ball.distance(paddle_left) < 50 and ball.xcor() < -320\
            or ball.distance(paddle_right) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # --- Detect NOT collision with Paddle ---
    elif ball.xcor() > 380:
        ball.reset()
        scoreboard.point_for_left_player()


    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.point_for_right_player()






















screen.exitonclick()