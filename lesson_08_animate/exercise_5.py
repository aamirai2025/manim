from manim import *

class ComboTransform(Scene):

    def construct(self):

        square = Square()

        square.set_color(WHITE)

        self.wait(1)

        self.play(square.animate.shift(2*RIGHT))

        self.wait(1)

        self.play(square.animate.shift(2*UP))

        self.wait(1)

        self.play(square.animate.scale(2))

        self.wait(1)

        self.play(square.animate.rotate(PI/4))

        self.wait(1)

        self.play(square.animate.set_color(RED))

        self.wait(1)