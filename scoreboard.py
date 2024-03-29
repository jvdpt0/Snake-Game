from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setpos(0,250)
        self.color('white')
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
     #   self.setpos(0, 0)
      #  self.write('GAME OVER.', align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        