import random
from turtle import Turtle
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.change_food_pos()

    
    def change_food_pos(self):        
        food_pos_x = random.randint(-20,20)*10
        food_pos_y = random.randint(-20,20)*10
        self.teleport(food_pos_x, food_pos_y)

