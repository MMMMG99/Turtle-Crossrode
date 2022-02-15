import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

sandu = Player()
scor = Scoreboard()

screen.listen()
screen.onkey(sandu.move_forward, 'w')

lista = []
generare_masini = 0
viteza = 0.1
coeficient_de_dificultate = 6

game_is_on = True
while game_is_on:
    #generam masinile intr-un mod cat mai convenabil astfel incat sa nu se genereze dintr-odata un numar
    #foarte mare care sa compromita sansele jucatorului
    if generare_masini % coeficient_de_dificultate == 0:
        masini = CarManager()
        lista.append(masini)

    for masina in lista:
        #cand se termina jocul
        if sandu.distance(masina) < 20:
            game_is_on = False
            scor.game_over()

        #cand masinile trec de dimensiunile ecranului
        if masina.xcor() < -300:
            masina.hideturtle()
            del masina
        else:
            masina.miscare_masini()

    #cand jucatorul ajunge la finalul nivelului
    if sandu.ycor() > 280:
        sandu.finish()
        scor.actualizare_scor()
        viteza *= 0.7
    generare_masini += 1

    time.sleep(viteza)
    screen.update()

screen.exitonclick()
