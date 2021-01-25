from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    segments = []

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('green')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    # def move(self):
    #     for seg_num in range(len(self.segments) - 1 , 0, -1):
    #         new_x = self.segments[seg_num - 1].xcor()
    #         new_y = self.segments[seg_num - 1].ycor()
    #         self.segments[seg_num].goto(new_x, new_y)
    #     self.head.forward(MOVE_DISTANCE)

    def move(self):
        for seg_number in range(len(self.segments) - 1):
            segments_rev = self.segments[::-1]
            new_x = segments_rev[seg_number + 1].xcor()
            new_y = segments_rev[seg_number + 1].ycor()
            segments_rev[seg_number].goto(new_x, new_y)
            self.segments = segments_rev[::-1]
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


