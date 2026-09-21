from manim import *

class VectorAddition(Scene):
    def construct(self):

        vector_a = Arrow(ORIGIN, RIGHT*3, buff=0)
        self.play(Create(vector_a))
        self.wait()

        vector_b = Arrow(RIGHT*3, UP*4 + RIGHT*3, buff=0)
        self.play(Create(vector_b))
        self.wait()

        vector_r = Arrow(ORIGIN, RIGHT*3 + UP*4, buff=0)
        self.play(Create(vector_r))
        self.wait()