import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1 = Player()
screen.listen()
car_manage = CarManager()
level = Scoreboard()

screen.onkeypress(player1.down, "Down")
screen.onkeypress(player1.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manage.create_cars()
    car_manage.move_cars()

    # Detect collision
    for car in car_manage.all_cars:
        if player1.distance(car) < 25:
            level.game_over()
            game_is_on = False

    if player1.ycor() > 280:
        level.update_level()
        player1.reset_pos()
        car_manage.level_up()

screen.exitonclick()
