from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        self.blocks = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POS:
            block = Turtle(shape='square')
            block.color('white')
            block.penup()
            block.goto(position)
            self.blocks.append(block)

    def move(self):
        for block in range(len(self.blocks)-1, 0, -1):

            new_x = self.blocks[block-1].xcor()
            new_y = self.blocks[block-1].ycor()
            self.blocks[block].goto(new_x, new_y)
        self.blocks[0].forward(MOVE_DISTANCE)

    def up(self):
        for block in range(len(self.blocks)-1, 0, -1):

            new_x = self.blocks[block-1].xcor()
            new_y = self.blocks[block-1].ycor()
            self.blocks[block].goto(new_x, new_y)
        self.blocks[0].setheading(90)

    def down(self):
        for block in range(len(self.blocks)-1, 0, -1):

            new_x = self.blocks[block-1].xcor()
            new_y = self.blocks[block-1].ycor()
            self.blocks[block].goto(new_x, new_y)
        self.blocks[0].setheading(270)

    def right(self):
        for block in range(len(self.blocks)-1, 0, -1):

            new_x = self.blocks[block-1].xcor()
            new_y = self.blocks[block-1].ycor()
            self.blocks[block].goto(new_x, new_y)
        self.blocks[0].setheading(0)

    def left(self):
        for block in range(len(self.blocks)-1, 0, -1):

            new_x = self.blocks[block-1].xcor()
            new_y = self.blocks[block-1].ycor()
            self.blocks[block].goto(new_x, new_y)
        self.blocks[0].setheading(180)
