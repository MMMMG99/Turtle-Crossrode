from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(350, random.randint(-240, 240))
        self.shape('square')
        self.color(COLORS[random.randint(0, len(COLORS) - 1)])
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.setheading(LEFT)

    def miscare_masini(self):
        self.forward(STARTING_MOVE_DISTANCE)