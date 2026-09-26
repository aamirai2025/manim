from manim import *

class Properties2(Scene):
    def construct(self):
        square1 = Square()

        square1.generate_target().move_to(RIGHT*3).scale(2).rotate(PI/4).set_color(GREEN)
        

        self.play(Create(square1))

        self.play(MoveToTarget(square1))
        self.wait(2)