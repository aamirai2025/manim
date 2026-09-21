from manim import *

class GeometricComposition(Scene):
    def construct(self):

        # Circle
        circle = Circle(radius=1)
        circle.move_to(LEFT * 3 + UP * 1.5)
        circle.set_color(BLUE)
        circle.set_fill(BLUE, opacity=0.3)

        # Square
        square = Square(side_length=2)
        square.move_to(ORIGIN + UP * 1.5)
        square.set_color(RED)
        square.set_fill(RED, opacity=0.3)

        # Triangle
        triangle = Triangle()
        triangle.move_to(RIGHT * 3 + UP * 1.5)
        triangle.set_color(GREEN)
        triangle.set_fill(GREEN, opacity=0.3)

        # Rectangle
        rectangle = Rectangle(
            width=3,
            height=1.5
        )
        rectangle.move_to(LEFT * 2 + DOWN * 2)
        rectangle.set_color(YELLOW)

        # Line
        line = Line(
            LEFT * 3,
            RIGHT * 3
        )
        line.shift(DOWN * 3)

        # Dot
        dot = Dot()
        dot.move_to(RIGHT * 2 + DOWN * 2)
        dot.set_color(ORANGE)

        # Arrow
        arrow = Arrow(
            LEFT * 1.5,
            RIGHT * 1.5
        )
        arrow.shift(RIGHT * 2 + DOWN * 2)

        # Create everything
        self.play(
            Create(circle),
            Create(square),
            Create(triangle),
            Create(rectangle),
            Create(line),
            Create(dot),
            Create(arrow)
        )

        self.wait()