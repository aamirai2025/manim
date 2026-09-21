from manim import *

class MiniProject(Scene):
    def construct(self):
        circle = Circle(radius=1)
        circle.move_to(LEFT*3 + UP*1.5)
        circle.set_color(BLUE)
        circle.set_fill(BLUE, opacity=0.3)

        square = Square(side_length=2)
        square.move_to(ORIGIN + UP*1.5)
        square.set_color(RED)
        square.set_fill(RED, opacity=0.3)

        triangle = Triangle()
        triangle.move_to(RIGHT*3 + UP*1.5)
        triangle.set_color(GREEN)
        triangle.set_fill(GREEN, opacity=0.3)

        rectangle = Rectangle(width=3, height=1.5)
        rectangle.move_to(LEFT*2 + DOWN*2)
        rectangle.set_color(YELLOW)

        line = Line(LEFT*3, RIGHT*3)
        line.shift(DOWN*3)

        dot = Dot()
        dot.move_to(RIGHT*2 + DOWN*2)
        dot.set_color(ORANGE)

        arrow = Arrow(LEFT*1.5, RIGHT*1.5)
        arrow.shift(RIGHT*2 + DOWN*2)

        self.play(Create(circle),
            Create(square),
            Create(triangle),
            Create(rectangle),
            Create(line),
            Create(dot),
            Create(arrow))
        
        self.wait()
        