from manim import *

class MobjectsTransformations(Scene):
    def construct(self):

        triangle = Triangle()
        self.play(Create(triangle))
        self.wait()

        triangle.scale(2)
        self.wait()

        triangle.rotate(PI/4)
        self.wait()

        triangle.shift(RIGHT)
        self.wait()