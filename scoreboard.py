from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(-290, 260)
        self.color('black')
        self.hideturtle()
        self.level = 1
        self.afisare_scor()

    def afisare_scor(self):
        self.write(f'Level: {self.level}', move=False, align='left', font=FONT)

    def actualizare_scor(self):
        self.level += 1
        self.clear()
        self.afisare_scor()

    def game_over(self):
        self.goto(-80, 0)
        self.write(f'GAME OVER', move=False, align='left', font=FONT)