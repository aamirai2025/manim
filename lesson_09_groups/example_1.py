from manim import *

class GroupArrange(Scene):

    def construct(self):

        circle = Circle()
        square = Square()
        triangle = Triangle()

        group = VGroup(circle, square, triangle)

        group.arrange(LEFT, buff=1)

        self.play(Create(circle))
        self.play(Create(square))
        self.play(Create(triangle))

        self.wait(2)

        self.play(group.animate.shift(UP))

        self.wait(2)