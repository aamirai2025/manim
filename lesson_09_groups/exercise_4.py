from manim import *

class AccessMember(Scene):

    def construct(self):

        circle = Circle()
        square = Square()
        triangle = Triangle()

        group = VGroup(circle, square, triangle)
        group.arrange(RIGHT, buff=1)

        self.add(group)

        self.play(group.animate.shift(UP))
        self.wait(2)

        self.play(group[1].animate.shift(DOWN))
        self.wait(2)

