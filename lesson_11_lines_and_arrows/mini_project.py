from manim import *

class MiniProject(Scene):

    def construct(self):

        A = Dot(color=RED).shift(LEFT * 2)
        B = Dot(color=RED).shift(RIGHT * 2)
        C = Dot(color=RED).shift(UP * 3)

        A_label = MathTex("A").next_to(A, LEFT)
        B_label = MathTex("B").next_to(B, RIGHT)
        C_label = MathTex("C").next_to(C, UP)

        AB = Line(
            A.get_center(),
            B.get_center(),
            color=BLUE,
            buff=0
        )

        BC = Line(
            B.get_center(),
            C.get_center(),
            color=BLUE,
            buff=0
        )

        CA = Line(
            A.get_center(),
            C.get_center(),
            color=BLUE,
            buff=0
        )

        altitude = DashedLine(
            C.get_center(),
            [0, 0, 0],
            color=YELLOW,
            buff=0
        )

        h = MathTex("h").next_to(altitude, RIGHT)

        right_angle = RightAngle(altitude, AB, length=0.3, quadrant=(-1, 1), color=GREEN)

        arc = Angle(
            AB,
            CA,
            radius=0.5,
            color=PURPLE
        )

        theta = MathTex(r"\theta", color=PURPLE).move_to(
            A.get_center() + RIGHT * 0.65 + UP * 0.30
        )

        explain = Text("Acute Angle").next_to(BC, RIGHT)

        curved_arrow = CurvedArrow(
            start_point=explain.get_left() + LEFT * 0.2,
            end_point=theta.get_right() + RIGHT * 0.2 + UP * 0.2
        )

        self.play(
            Create(A),
            Create(A_label),
            Create(B),
            Create(B_label),
            Create(C),
            Create(C_label)
        )

        self.play(
            Create(AB),
            Create(BC),
            Create(CA)
        )

        self.wait()

        self.play(Create(altitude))
        self.wait()

        self.play(Write(h))
        self.wait()

        self.play(Create(right_angle))
        self.wait()

        self.play(Create(arc))
        self.wait()

        self.play(Write(theta))
        self.wait()

        self.play(Create(curved_arrow))
        self.wait()

        self.play(Write(explain))
        self.wait()