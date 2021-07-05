import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.dy = -0.35
        self.dx = 0.35
        self.penup( )
        self.shape("circle")
        self.color("white")
        self.speed = 1.5
