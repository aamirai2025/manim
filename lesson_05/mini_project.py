from manim import *

class CoordinateDiagram(Scene):
    def construct(self):

        # Coordinate plane
        plane = NumberPlane()

        # Points
        A = Dot([2, 2, 0])
        B = Dot([-2, -1, 0])
        C = Dot([3, -1, 0])

        # Triangle
        AB = Line(A.get_center(), B.get_center())
        BC = Line(B.get_center(), C.get_center())
        CA = Line(C.get_center(), A.get_center())

        # Labels
        label_A = MathTex("A").next_to(A, UP)
        label_B = MathTex("B").next_to(B, DOWN)
        label_C = MathTex("C").next_to(C, DOWN)

        # Animation
        self.play(Create(plane))

        self.play(
            Create(A),
            Create(B),
            Create(C)
        )

        self.play(
            Create(AB),
            Create(BC),
            Create(CA)
        )

        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C)
        )

        self.wait()