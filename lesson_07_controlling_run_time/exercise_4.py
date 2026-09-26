from manim import *

class SeqMove(Scene):

    def construct(self):

        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle = circle.move_to(LEFT*2)
        square = square.move_to(RIGHT*2)
        triangle = triangle.move_to(UP*2)

        self.play(
            Create(circle),
            Create(square),
            Create(triangle)
        )

        self.play(circle.animate.shift(RIGHT*4))
        self.play(square.animate.shift(UP*2 + LEFT*2))
        self.play(triangle.animate.shift(DOWN*2 + LEFT*2))

        self.wait()