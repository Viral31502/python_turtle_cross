from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 1
DOWN = -1
FACE_UPWARD = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(FACE_UPWARD)

    def move(self, direction):
        steps = MOVE_DISTANCE * direction
        self.forward(steps)

    def move_up(self):
        self.move(UP)

    def down(self):
        self.move(DOWN)

    def reset_pos(self):
        self.goto(STARTING_POSITION)
