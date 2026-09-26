from manim import *

class Test(Scene):

    def construct(self):

        circle = Circle()

        self.play(Create(circle), run_time=5)

        self.wait()