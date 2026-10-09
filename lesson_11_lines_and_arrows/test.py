from manim import *
import math as m

class Exercise1(Scene):

    def construct(self):

        base = Line([-2, 3,0], [2, 3, 0])
        perp = Line([-3.5, 0, 0], [-3.5, 3, 0])
        hyp = Line([-3, 0, 0], [1, 3, 0])

        self.play(Create(base))
        self.wait(1)

        self.play(Create(perp))
        self.wait(1)

        self.play(Create(hyp))
        self.wait(1)

        self.play(base.animate.shift(DOWN*3))
        self.wait(1)

        self.play(perp.animate.shift(RIGHT*5.5))
        self.wait(1)

        self.play(hyp.animate.shift(RIGHT))
        self.wait(1)