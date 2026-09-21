from manim import *

class Arrows(Scene):
    def construct(self):

        arrow = Arrow(LEFT, RIGHT)
        self.play(Create(arrow))
        self.wait()

        arrow = Arrow(RIGHT, LEFT)
        arrow.move_to(DOWN*2)
        self.play(Create(arrow))
        self.wait()

        arrow = Arrow(ORIGIN, LEFT*3)
        self.play(Create(arrow))
        self.wait()

        vector = Arrow(ORIGIN, RIGHT*3 + UP*4)
        self.play(Create(vector))
        self.wait()