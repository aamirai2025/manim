from manim import *

class Test(Scene):

    def construct(self):

        A = Dot([-2, -1, 0])
        B = Dot([2, -1, 0])
        C = Dot([0, 2, 0])

        AB = Line(
            A.get_center(),
            B.get_center()
        )

        BC = Line(
            B.get_center(),
            C.get_center()
        )

        CA = Line(
            C.get_center(),
            A.get_center()
        )

        self.play(Create(A), Create(B), Create(C))

        self.wait(1)

        self.play(
            Create(AB),
            Create(BC),
            Create(CA)
        )

        self.wait(1)

        label_A = MathTex("A").next_to(A, DOWN)
        label_B = MathTex("B").next_to(B, DOWN)
        label_C = MathTex("C").next_to(C, UP)

        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C)
        )

        self.wait(2)

        altitude_A = DashedLine(
            C.get_center(),
            [0, -1, 0]
        )

        self.play(Create(altitude_A))

        self.wait(1)