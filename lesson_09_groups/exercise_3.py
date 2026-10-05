from manim import *

class AccessMember(Scene):

    def construct(self):

        circle = Circle()
        square = Square()
        triangle = Triangle()

        group = VGroup(circle, square, triangle)

        group.arrange(RIGHT, buff=1)

        self.play(Create(group))

        self.wait(1)

        self.play(group[0].animate.set_color(RED))
        self.play(group[1].animate.set_color(GREEN))
        self.play(group[2].animate.set_color(BLUE))

        self.wait(2)

        self.play(group.animate.shift(UP))

        self.wait(2)