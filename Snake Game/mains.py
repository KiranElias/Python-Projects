from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Scoreboard
screen=Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600,height=600)
screen.tracer(0)

start_pos=[(0,0),(-20,0),(-40,0)]
segments=[]

snake=Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    if snake.segments[0].distance(food)<15:
        food.refresh()
        score.increas_score()
        snake.extend()

    if snake.segments[0].xcor()>280 or  snake.segments[0].xcor()<-280 or  snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        score.game_over()
        game_is_on=False

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            game_is_on=False
            score.game_over()
            
            
screen.exitonclick()