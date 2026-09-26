from manim import *

class PauseTest(Scene):

    def construct(self):

        circle = Circle()

        self.play(Create(circle))

        self.wait(2)

        self.play(circle.animate.shift(RIGHT*3))

        self.wait()