from manim import *

class BasicGroup(Scene):

    def construct(self):

        circle = Circle()
        square = Square()
        triangle = Triangle()

        group = VGroup(circle, square, triangle)

        group.arrange(RIGHT, buff=1)

        self.play(Create(group))

        self.wait(2)

        self.play(group.animate.shift(UP))

        self.wait(2)