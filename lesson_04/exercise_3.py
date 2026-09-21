from manim import *

class Rotation(Scene):
    def construct(self):

        square = Square(side_length=2)
        square.set_color(BLUE)
        square.set_fill(BLUE, opacity=0.3)
        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(square.animate.rotate(PI/4))
        self.wait()
