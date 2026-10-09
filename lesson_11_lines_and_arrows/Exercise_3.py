from manim import *

class Exercise3(Scene):

    def construct(self):

        circle = Circle()
        circle.move_to(LEFT*3)
        square = Square()
        triangle = Triangle()
        triangle.move_to(RIGHT*3).rotate(PI/2)

        arrow_1 = Arrow(start=circle.get_right(), end=square.get_left(), buff=0)
        arrow_2 = Arrow(start=square.get_right(), end=triangle.get_left(), buff=0)

        self.play(Create(circle))
        self.play(Create(arrow_1))
        self.play(Create(square))
        self.play(Create(arrow_2))
        self.play(Create(triangle))

        self.wait(1)