from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_POSITIONS=20
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
    
    def create_snake(self):
        for i in STARTING_POSITIONS:
           self.add_segment(i)
    def add_segment(self,i):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(i)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
         for seg_num in range(len(self.segments)-1,0,-1):
            newx=self.segments[seg_num-1].xcor()
            newy=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(newx,newy)

         self.segments[0].forward(MOVE_POSITIONS)
    

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)