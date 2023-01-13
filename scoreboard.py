from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setpos(0,250)
        self.color('white')
        self.count = 0
        self.write(f'Score: {self.count}', align='center', font=('Arial', 24, 'normal'))
    
    def increase_score(self):
        self.count +=1
        self.clear()
        self.write(f'Score: {self.count}', align='center', font=('Arial', 24, 'normal'))
        