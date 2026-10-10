from manim import *

class Test(Scene):

    def construct(self):

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=6,
            axis_config={
                "include_numbers": True,
            },
        )

        self.play(Create(axes))
        self.wait(2)