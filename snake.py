from turtle import Turtle

starting_positions = [(0,0), (-20,0), (-40,0)]

class Snake():
    
    def __init__(self):
        self.snake = []

        # Create snake head
        s = Turtle(shape="square")
        s.color("white")
        s.penup()
        self.snake.append(s)

        # create the rest of the body
        for _ in range(2):
            self.add_segment()



    def add_segment(self):
        snake_len = len(self.snake)
        s = Turtle(shape="square")
        s.color("white")
        s.penup()
        snake_tail_pos = self.snake[-1].pos()
        
        # see if added segmentg is in horizontal or vertical direction
        if self.snake[-1].heading() == 0 or self.snake[-1].heading() == 180:
            s.goto(snake_tail_pos[0]-20, snake_tail_pos[1])
        else:
            s.goto(snake_tail_pos[0], snake_tail_pos[1]-20)
        
        self.snake.append(s)



    def move_forward(self):
        prev_pos = self.snake[0].pos()
        self.snake[0].fd(20)
        for s in self.snake[1:]:
            temp = s.pos()
            s.goto(prev_pos)
            prev_pos = temp



    def move_up(self):
        if not(self.snake[0].heading() == 270):
            self.snake[0].setheading(90)



    def move_dn(self):
        if not(self.snake[0].heading() == 90):
            self.snake[0].setheading(270)



    def move_lf(self):
        if not(self.snake[0].heading() == 0):
            self.snake[0].setheading(180)



    def move_rt(self):
        if not(self.snake[0].heading() == 180):
            self.snake[0].setheading(0)



    def did_snake_ate_food(self, obj):
        return self.snake[0].distance(obj) < 15
    
    def did_snake_ate_itself(self, obj):
        return self.snake[0].pos() == obj.pos()