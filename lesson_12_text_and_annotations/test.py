from manim import *

class Test(Scene):

    def construct(self):

        c = MathTex(r"c", color=RED).to_edge(UP)

        c_copy = MathTex(r"c", color=RED).to_edge(UP)

        target = MathTex(r"c^2", color=RED).to_edge(DOWN)

        self.play(Write(c))
        self.wait(2)

        self.add(c_copy)

        self.play(c_copy.animate.to_edge(DOWN), run_time=3)

        self.play(Transform(c_copy, target))

        self.wait()
