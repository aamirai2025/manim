from manim import *

class Exercise4(Scene):

    def construct(self):

        A = LEFT*2 + DOWN*2
        B = RIGHT*2 + DOWN*2
        C = LEFT*2 + UP

        triangle = Polygon(A, B, C)

        A_label = MathTex("A").next_to(A, LEFT)
        B_label = MathTex("B").next_to(B, RIGHT)
        C_label = MathTex("C").next_to(C, UP)

        A_dim = A + LEFT*1
        C_dim = C + LEFT*1

        dim = DoubleArrow(
            start=A_dim,
            end=C_dim,
            buff=0
        )
        
        h = MathTex("h").next_to(dim, LEFT)

        self.play(Create(triangle))

        self.play(
            Write(A_label),
            Write(B_label),
            Write(C_label)
        )
        
        self.play(
            Create(dim),
            Write(h)
        )
        
        self.wait(1)


