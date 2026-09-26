from manim import *

class MiniProject(Scene):

    def construct(self):

        circle = Circle().shift(LEFT*4)
        square = Square()
        triangle = Triangle().shift(RIGHT*4)

        self.play(
            LaggedStart(
                Create(circle),
                Create(square),
                Create(triangle),
                lag_ratio=0.2
            ),
            run_time=5
        )

        self.wait(1)

        self.play(
            circle.animate.shift(RIGHT*2),
            triangle.animate.shift(LEFT*2),
            run_time=2
        )

        self.wait(1)

        self.play(square.animate.shift(UP*2),
            run_time=2
        )

        self.wait(1)

        self.play(
            circle.animate.shift(UP*2),
            triangle.animate.shift(UP*2),
            square.animate.shift(DOWN*2),
            run_time=2
        )

        self.wait(2)