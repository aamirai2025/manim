from manim import *

class CircleAnimate(Scene):

    def construct(self):

        circle = Circle()

        self.play(circle.animate.shift(RIGHT*3))
        self.play(circle.animate.shift(LEFT*6))
        self.play(circle.animate.shift(RIGHT*3))

        self.wait()