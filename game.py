from snake import Snake
from turtle import Screen, Turtle
from food import Food
import time

class Game():
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600) 
        self.screen.tracer(0)

        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.color("white")
        self.writer.penup()
        self.writer.goto(0, 260)   

        self.score = 0
        self.update_screen_title()

        self.snake = Snake()
        self.food = Food()
        self.screen.update()

        self.screen.listen()
        self.screen.onkey(self.snake.move_up,"Up")
        self.screen.onkey(self.snake.move_dn,"Down")
        self.screen.onkey(self.snake.move_lf,"Left")
        self.screen.onkey(self.snake.move_rt,"Right")

        self.game_on = True

        self.start_playing()

    def start_playing(self):

        while self.game_on:
            time.sleep(0.1)
            self.snake.move_forward()
            
            if self.snake.did_snake_ate_food(self.food):
                self.snake.add_segment()
                self.score += 1
                self.update_screen_title()
                self.food.change_food_pos()
            
            if self.snake.did_snake_ate_itself():
                self.game_on = False

            self.screen.update()

    def update_screen_title(self):
        self.writer.clear()
        self.writer.write(f"Your Score: {self.score}", align="center", font=("Aerial", 20, "normal"))