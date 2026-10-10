from manim import *

class Exercise2(Scene):

    def construct(self):

        A_dot = Dot(color=BLUE).shift(LEFT*2)
        B_dot = Dot(color=BLUE).shift(RIGHT*2)
        C_dot = Dot(color=BLUE).shift(UP*3)

        A_label = Tex("A", font_size=24).next_to(A_dot, DOWN)
        B_label = Tex("B", font_size=24).next_to(B_dot, DOWN)
        C_label = Tex("C", font_size=24).next_to(C_dot, UP)

        triangle = Polygon(A_dot.get_center(), B_dot.get_center(), C_dot.get_center(), color=BLUE)

        self.play(Create(triangle))

        self.play(FadeIn(A_dot), FadeIn(B_dot), FadeIn(C_dot))

        self.play(Write(A_label), Write(B_label), Write(C_label))

        self.wait(1)