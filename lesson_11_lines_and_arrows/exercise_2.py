from manim import *

class Exercise2(Scene):

    def construct(self):

        vector = Arrow(start=ORIGIN, end=[3, 2, 0], buff=0)
        label = MathTex("\\vec{v}")

        self.play(Create(vector))
        self.play(Write(label.next_to(vector.get_end(), UP)))

        self.wait()