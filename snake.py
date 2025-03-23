from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Functions related to the actual snake entity, using turtle.
    create_snake, add_segment, extend, move, up/down/left/right"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates initial snake instance"""
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a segment behind the snake head"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Adds an extra segment to the back of the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake head as well as any segments behind it."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # i forgot what the numbers at the end do, figure out later
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

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