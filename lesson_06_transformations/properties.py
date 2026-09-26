from manim import *

class Properties(Scene):
    def construct(self):
        square1 = Square()
        square2 = Square().move_to(RIGHT*3).scale(2).rotate(PI/4).set_color(GREEN)

        self.play(Create(square1))
        self.wait(1)
        self.play(Transform(square1, square2))
        self.wait(2)
        