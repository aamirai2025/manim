from manim import *

class LagTest(Scene):

    def construct(self):

        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle = circle.move_to(LEFT*3)
        triangle = triangle.move_to(RIGHT*3)

        self.play(
            LaggedStart(
                Create(circle),
                Create(square),
                Create(triangle),
                lag_ratio=0.5
            ),
        )

        self.wait()