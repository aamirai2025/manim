from manim import *

class Simultaneous(Scene):

    def construct(self):

        circle = Circle()
        circle = circle.set_color(WHITE)

        self.play(Create(circle))

        self.wait(1)

        self.play(circle.animate.shift(2*RIGHT).scale(2).set_color(RED))

        self.wait(1)