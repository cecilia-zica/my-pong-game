from turtle import Turtle

SCREEN_HEIGHTT = 600
ALIGNMENT = "center"
FONT = ("Courier New", 36, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("BlueViolet")
        self.penup()
        self.hideturtle()
        self.y_position = SCREEN_HEIGHTT / 2 - 50
        self.update_score()

    def update_score(self):
        self.clear()

        #l_score position
        self.goto(-100, self.y_position)
        self.write(self.l_score, align = ALIGNMENT, font = FONT)

        #Visual division
        self.goto(0, self.y_position)
        self.write("|", align=ALIGNMENT, font=FONT)

        #r_score position
        self.goto(100, self.y_position)
        self.write(self.r_score, align = ALIGNMENT, font = FONT)

    def point_for_left_player(self):
        self.l_score += 1
        self.update_score()

    def point_for_right_player(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
