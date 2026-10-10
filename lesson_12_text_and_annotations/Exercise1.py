from manim import *

class Exercise1(Scene):

    def construct(self):

        title = Text("Equation of Circle", font_size=48)
        title.to_edge(UP)

        equation = MathTex(r"x^2 + y^2 = r^2", font_size=36)

        self.play(Write(title))
        self.wait(1)

        self.play(Write(equation))
        self.wait(1)