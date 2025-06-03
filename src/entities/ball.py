from turtle import Turtle

STARTING_POSITION = (0, 0)

class Ball(Turtle):
    def __init__(self):
        #1. Inherit from turtle
        super().__init__()

        #2. Features
        self.shape("circle")
        self.color("BlueViolet")

        #3. Preparing for no trail
        self.penup()

        #4. How it moves
        self.x_move = 10
        self.y_move = 10
        self.speed(0.1)

        #5. Starting position
        self.goto(0, 0)

        #6. Speed
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverses direction on the y-axis when bouncing off the Paddle"""
        self.y_move *= -1

    def bounce_x(self):
        """Reverses direction on the x-axis when bouncing off the Paddle"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets the ball position after a point"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x() #Ball faces first the person who didn't score



