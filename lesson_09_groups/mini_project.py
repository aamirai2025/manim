from manim import *

class MiniProject(Scene):

    def construct(self):

        circle = Circle()
        triangle = Triangle()
        square = Square()

        group = VGroup(circle, triangle, square)
        group.arrange(RIGHT, buff=0.5)

        self.play(Create(group))
        self.wait(2)

        self.play(group.animate.shift(UP))
        self.wait(2)

        self.play(group.animate.scale(1.5))
        self.wait(2)

        self.play(group.animate.rotate(PI), run_time=2)
        self.wait(2)

        self.play(group[1].animate.shift(UP))
        self.wait(2)