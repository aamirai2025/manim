from manim import *

class Exercise2(Scene):
    def construct(self):
        square = Square(side_length=1)
        self.play(Create(square))
        self.play(square.animate.scale(2))
        self.play(square.animate.scale(0.5))
        self.wait()
