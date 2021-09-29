from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align='center',font=("Arial",24,"normal"))
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over \nYour score is {self.score}",align='center',font=("Arial",24,"normal"))
        

    def increas_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()