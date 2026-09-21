from manim import *

class RelativeMovement(Scene):
    def construct(self):

        triangle = Triangle()
        triangle.set_stroke(color=RED, width=5).set_fill(RED, opacity=0.3)
        self.play(Create(triangle))
        self.play(triangle.animate.shift(RIGHT*4))
        self.play(triangle.animate.shift(UP*3))
        self.play(triangle.animate.shift(LEFT*4))
        self.play(triangle.animate.shift(DOWN*3))
        self.wait()