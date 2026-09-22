from manim import *

class MathText(Scene):

    def construct(self):

        circle = Circle(radius=2)
        circle.set_stroke(RED, width=5)

        label1 = MathTex("A")
        label2 = MathTex("B")
        label3 = MathTex("C")
        label4 = MathTex("D")

        label1.next_to(circle, RIGHT, buff=0.5)
        label2.next_to(circle, LEFT, buff=0.5)
        label3.next_to(circle, UP, buff=0.5)
        label4.next_to(circle, DOWN, buff=0.5)

        self.play(
            Create(circle),
            Write(label1),
            Write(label2),
            Write(label3),
            Write(label4)
        )

        self.wait()