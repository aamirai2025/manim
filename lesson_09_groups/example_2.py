from manim import *

class AddToGroup(Scene):

    def construct(self):

        circle = Circle()
        square = Square()

        group = VGroup(circle, square)

        triangle = Triangle()

        group.add(triangle)

        group.arrange(RIGHT)

        self.play(Create(group))

        self.play(group.animate.set_color(GREEN))

        self.wait(2)