from manim import *

class Exercise1(Scene):
    def construct(self):
        b_circle = Circle()
        b_circle.set_color(BLUE)
        b_circle.move_to(LEFT*3)

        r_circle = Circle()
        r_circle.set_color(RED)

        g_circle = Circle()
        g_circle.set_color(GREEN)
        g_circle.move_to(RIGHT*3)

        self.play(Create(b_circle),
            Create(r_circle),
            Create(g_circle))

        self.play(FadeOut(b_circle))
        self.play(FadeOut(r_circle))
        self.play(FadeOut(g_circle))

        y_circle = Circle(radius=2)
        self.play(Create(y_circle))
        self.play(y_circle.animate.shift(RIGHT*3))
        self.wait()