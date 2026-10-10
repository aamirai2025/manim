from manim import *

class MiniProject(Scene):

    def construct(self):

        title = Text("Right Triangle", font_size=36, color=RED).to_edge(UP)

        subtitle = Text("Pythagoras Theorem: ", font_size=26, color=BLUE)
        subt_math = MathTex(r"a^2 + b^2 = c^2", font_size=40).next_to(subtitle, RIGHT)

        subhead = VGroup(subtitle, subt_math).move_to(UP*2.5).set_x(0)

        A_dot = Dot(color=BLUE).shift(LEFT*2 + DOWN*2)
        B_dot = Dot(color=BLUE).shift(RIGHT*2 + DOWN*2)
        C_dot = Dot(color=BLUE).shift(RIGHT*2 + UP)

        A_label = MathTex("A", color=BLUE).next_to(A_dot, DOWN)
        B_label = MathTex("B", color=BLUE).next_to(B_dot, DOWN)
        C_label = MathTex("C", color=BLUE).next_to(C_dot, UP)

        AB = Line(A_dot.get_center(), B_dot.get_center(), color=YELLOW, buff=0)
        BC = Line(B_dot.get_center(), C_dot.get_center(), color=YELLOW, buff=0)
        AC = Line(A_dot.get_center(), C_dot.get_center(), color=RED, buff=0)

        base = MathTex(r"a", font_size=40, color=YELLOW).next_to(AB, DOWN)
        perp = MathTex(r"b", font_size=40, color=YELLOW).next_to(BC, RIGHT)
        hypo = MathTex(r"c", font_size=40, color=RED).move_to(AC.point_from_proportion(0.5) + UP*0.4)

        ra = RightAngle(Line(B_dot.get_center(), A_dot.get_center()), BC, length=0.3)

        aa = Angle(AB, AC, radius=0.5)

        theta = MathTex(r"\theta").move_to(LEFT*1.2 + DOWN*1.7)

        equation = MathTex("a^2", "+", "b^2", "=", "c^2", font_size=40).shift(DOWN*3.5)

        equation.set_color_by_tex("a^2", YELLOW)
        equation.set_color_by_tex("b^2", YELLOW)
        equation.set_color_by_tex("c^2", RED)

        self.play(Write(title))

        self.play(Write(subhead))

        self.play(
            Create(A_dot),
            Create(B_dot),
            Create(C_dot)
        )

        self.play(
            Write(A_label),
            Write(B_label),
            Write(C_label)
        )

        self.play(
            Create(AB),
            Create(BC)
        )

        self.play(Create(AC))

        self.play(Write(base), Write(perp))
        self.play(Write(hypo))

        self.play(Create(ra),
                  Create(aa))

        self.play(Write(theta))

        self.play(Write(equation))

        self.wait()