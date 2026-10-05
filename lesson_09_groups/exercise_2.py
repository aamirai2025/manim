from manim import *

class AddToGroup(Scene):

    def construct(self):

        circle = Circle()
        square = Square()

        group = VGroup(circle, square)

        triangle = Triangle()

        group.add(triangle)

        group.arrange(DOWN, buff=1)

        self.play(Create(group))

        self.wait(1)

        self.play(group.animate.shift(RIGHT))

        self.wait(2)