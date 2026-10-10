from manim import *

class Exercise4(Scene):

    def construct(self):

        equation1 = MathTex(r"x^2 = 1", font_size=40)
        equation2 = MathTex(r"x^2 = 4", font_size=40)

        self.play(Write(equation1))
        self.wait(1)

        self.play(Transform(equation1, equation2))

        self.wait(1)