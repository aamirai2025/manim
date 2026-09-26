from manim import *

class MultipleTransforms(Scene):
    def construct(self):
        
        circle1 = Circle().move_to(LEFT*3)
        circle2 = Circle()
        circle3 = Circle().move_to(RIGHT*3)

        square = Square().move_to(LEFT*3)
        triangle = Triangle()
        pentagon = RegularPolygon(n=5).move_to(RIGHT*3)

        self.add(circle1, circle2, circle3)

        self.play(
            Transform(circle1, square),
            Transform(circle2, triangle),
            Transform(circle3, pentagon)
        )

        self.wait()