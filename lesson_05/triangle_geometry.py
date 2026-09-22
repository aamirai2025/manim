from manim import *

class TriangleGeometry(Scene):

    def construct(self):

        dot1 = Dot([0, 2, 0])
        dot1.set_color(RED)

        dot2 = Dot([-1.5, 0, 0])
        dot2.set_color(RED)

        dot3 = Dot([1.5, 0, 0])
        dot3.set_color(RED)

        line1 = Line(
            dot1.get_center(),
            dot2.get_center()
        )

        line2 = Line(
            dot2.get_center(),
            dot3.get_center()
        )

        line3 = Line(
            dot1.get_center(),
            dot3.get_center()
        )

        label1 = MathTex("A")
        label2 = MathTex("B")
        label3 = MathTex("C")

        label1.next_to(dot1, UP)
        label2.next_to(dot2, LEFT)
        label3.next_to(dot3, RIGHT)

        self.play(
            Create(dot1),
            Create(dot2),
            Create(dot3),
            Create(line1),
            Create(line2),
            Create(line3),
            Write(label1),
            Write(label2),
            Write(label3)
        )

        self.wait()