from manim import *

class AccessMember(Scene):

    def construct(self):

        circle = Circle()
        square = Square()
        triangle = Triangle()

        group = VGroup(circle, square, triangle)
        group.arrange(RIGHT, buff=1)

        self.play(Create(group), run_time=2)
        self.wait(1)

        self.play(group.animate.shift(UP))
        self.wait(2)

        self.play(group.animate.scale(1.5))
        self.wait(2)

        self.play(group.animate.rotate(PI/2))
        self.wait(2)

        self.play(group.animate.move_to(ORIGIN))
        self.wait(2)