from manim import *

class FillStroke(Scene):
    def construct(self):

        circle = Circle()
        circle.set_fill(BLUE, opacity=0.4).set_stroke(color=RED, width=5)
        self.play(Create(circle))
        self.play(circle.animate.shift(UP*1))
        self.play(circle.animate.shift(DOWN*1))
        self.wait()