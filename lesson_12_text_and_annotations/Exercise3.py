from manim import *

class Exercise3(Scene):

    def construct(self):

        d_title = Text("Notation of Derivative:", font_size=26)
        d_math = MathTex(r"\frac{dy}{dx}", font_size=40).next_to(d_title, RIGHT*1.25)
        calculus = VGroup(d_title, d_math).move_to(LEFT*2 + UP*2)

        t_title = Text("Symbol of Angle:", font_size=26)
        t_math = MathTex(r"\theta", font_size=40).next_to(t_title, RIGHT*1.25)
        trig = VGroup(t_title, t_math).move_to(LEFT*2)

        a_title = Text("Algebraic Expression:", font_size=26)
        a_math = MathTex(r"\frac{x+1}{x-1}", font_size=40).next_to(a_title, RIGHT*1.25)
        algebra = VGroup(a_title, a_math).move_to(LEFT*2 + DOWN*2)

        self.play(Write(calculus[0]))
        self.wait(1)

        self.play(Write(calculus[1]))
        self.wait()

        self.play(Write(trig[0]))
        self.wait(1)

        self.play(Write(trig[1]))
        self.wait(1)

        self.play(Write(algebra[0]))
        self.wait(1)

        self.play(Write(algebra[1]))
        self.wait(1)