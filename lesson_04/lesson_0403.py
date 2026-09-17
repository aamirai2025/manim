from manim import *

class LinesAndDots(Scene):
    def construct(self):

        self.wait()
        dot = Dot(radius=0.1)
        dot.move_to(LEFT*2)
        self.add(dot)
        self.wait()

        dot = Dot(radius=0.1)
        dot.move_to(RIGHT*5)
        self.add(dot)
        self.wait()

        line = Line(LEFT*2, RIGHT*5)
        self.play(Create(line))
        self.wait()

        dot = Dot(radius=0.1)
        dot.move_to(UP*4)
        self.add(dot)
        self.wait()

        dot = Dot(radius=0.1)
        dot.move_to(DOWN*4)
        self.add(dot)
        self.wait()

        line = Line(UP*5, DOWN*5)
        self.play(Create(line))
        self.wait()