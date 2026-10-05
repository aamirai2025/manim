from manim import *

class Rotation(Scene):

    def construct(self):

        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI/2))
        self.wait(1)