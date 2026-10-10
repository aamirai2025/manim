from manim import *

class Exercise5(Scene):

    def construct(self):

        equation = MathTex("a^2","+", "b^2", "=", "c^2")

        equation.set_color_by_tex("a^2", RED)
        equation.set_color_by_tex("b^2", GREEN)
        equation.set_color_by_tex("c^2", YELLOW)

        self.play(Write(equation))
        self.wait(1)