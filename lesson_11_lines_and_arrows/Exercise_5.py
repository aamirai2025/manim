from manim import *

class Exercise5(Scene):

    def construct(self):

        A_dot = Dot(color=BLUE).shift(LEFT * 2)
        B_dot = Dot(color=RED).shift(RIGHT * 2)

        A_label = MathTex("A").next_to(A_dot, LEFT)
        B_label = MathTex("B").next_to(B_dot, RIGHT)

        self.play(Create(A_dot))
        self.wait()

        self.play(Write(A_label))
        self.wait()

        self.play(Create(B_dot))
        self.wait()

        self.play(Write(B_label))
        self.wait()

        line = always_redraw(lambda: Line(A_dot.get_center(), B_dot.get_center(), buff=0, color=YELLOW))

        self.play(Create(line))

        self.play(B_dot.animate.move_to([-2, 4, 0]), run_time=3)
        self.wait()