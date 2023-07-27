import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
turtle = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(turtle.go_up, "Up")
game_is_on = True


while game_is_on:

    time.sleep(0.1)
    screen.update()
    car.generate_cars()
    car.move()

    if car.detect_collision(turtle):
        scoreboard.game_over()
        game_is_on = False
    if turtle.detect_wall_collision():
        scoreboard.increase_level()
        car.level_up()


screen.exitonclick()

