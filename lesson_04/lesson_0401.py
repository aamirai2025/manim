from manim import *

class CreateCircle(Scene):
    def construct(self):

        circle = Circle()
        self.play(Create(circle))
        self.wait()

        circle2 = Circle(radius=2)
        self.play(Create(circle2))
        self.wait()

        square = Square(side_length=4)
        self.play(Create(square))
        self.wait()

        rectangle = Rectangle(width=8, height=6)
        self.add(rectangle)
        self.wait()
