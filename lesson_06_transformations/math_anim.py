from manim import *

class MathAnim(Scene):

    def construct(self):

        quad1 = MathTex(r"x^2 + 2x + 1")
        
        quad2 = MathTex(r"(x + 1)^2")

        self.play(Write(quad1))

        self.play(ReplacementTransform(quad1, quad2))

        self.wait(2)