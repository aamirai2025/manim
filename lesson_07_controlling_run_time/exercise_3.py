from manim import *

class SimMove(Scene):

    def construct(self):

        circle = Circle()
        square = Square()

        circle = circle.move_to(LEFT*3)
        square = square.move_to(RIGHT*3)

        self.play(Create(circle), Create(square))

        self.play(
            circle.animate.shift(RIGHT*6),
            square.animate.shift(LEFT*6)
        )

        self.wait()