from manim import *

class ChangeColor(Scene):

    def construct(self):

        circle = Circle()
        circle.set_color(WHITE)

        self.play(Create(circle))

        self.wait(1)

        self.play(circle.animate.set_color(RED))

        self.wait(1)

        self.play(circle.animate.set_color(BLUE))

        self.wait(1)

        self.play(circle.animate.set_color(GREEN))

        self.wait(1)