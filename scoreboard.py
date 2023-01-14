from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setpos(0,250)
        self.color('white')
        self.count = 0
        self.write(f'Score: {self.count}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write('GAME OVER.', align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.count +=1
        self.clear()
        self.write(f'Score: {self.count}', align=ALIGNMENT, font=FONT)
        