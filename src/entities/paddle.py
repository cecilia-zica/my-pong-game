from turtle import Turtle

PADDLE_MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, initial_position):
        #1. Inherit from turtle
        super().__init__()

        #2. Features
        self.shape("square")
        self.shapesize(5,1)
        self.color("Aquamarine")

        #3. Preparing for no trails
        self.penup()

        # 4. Inicial position of paddle
        self.goto(initial_position)  # USA o argumento recebido

    def move_up(self):
        new_y = self.ycor() + PADDLE_MOVE_DISTANCE
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - PADDLE_MOVE_DISTANCE
        self.sety(new_y)





