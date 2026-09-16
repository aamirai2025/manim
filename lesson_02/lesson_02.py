from manim import *

class CircleSquare(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait(1)

        square = Square()
        self.play(Transform(circle, square))
        self.wait(1)