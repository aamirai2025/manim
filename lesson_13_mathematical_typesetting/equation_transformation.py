from manim import *

class EquationTransformation(Scene):
    def construct(self):
        eq1 = MathTex(
            r"x^2 + 2x + 1"
        )

        eq2 = MathTex(
            r"(x+1)^2"
        )

        self.play(Write(eq1))
        self.wait(1)

        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(2)
