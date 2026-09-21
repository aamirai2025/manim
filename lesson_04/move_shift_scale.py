from manim import *

class MoveShiftScale(Scene):
    def construct(self):

        circle = Circle()
        self.play(Create(circle))
        self.wait()

        self.play(circle.animate.shift(RIGHT*3))
        self.play(circle.animate.shift(LEFT*6))
        self.wait()

        self.play(FadeOut(circle))
        self.wait()

        square = Square()
        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.wait()
        square.set_color(RED)
        self.wait()
        square.set_color(GREEN)
        self.wait()
        square.set_opacity(0.1)
        self.wait()
        self.play(FadeOut(square))

        circle = Circle()
        circle.set_stroke(color=RED, width=12)
        circle.set_fill(color=BLUE, opacity=1)
        self.play(Create(circle))
        self.wait()