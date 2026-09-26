from manim import *

class LagTest(Scene):

    def construct(self):

        circle1 = Circle().shift(LEFT*3)
        circle2 = Circle()
        circle3 = Circle().shift(RIGHT*3)

        self.play(LaggedStart(Create(circle1), Create(circle2), Create(circle3), lag_ratio=0.2, run_time=5))

        self.wait()