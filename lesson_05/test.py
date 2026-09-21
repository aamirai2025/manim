from manim import *

class PositioningDemo(Scene):
    def construct(self):

        title = Text("Positioning Objects")
        title.to_edge(UP)

        circle = Circle()
        circle.move_to(ORIGIN)

        square = Square()
        square.to_edge(LEFT)

        triangle = Triangle()
        triangle.to_corner(DR)

        label = Text("Circle")
        label.next_to(circle, RIGHT)

        self.play(
            Write(title),
            Create(circle),
            Create(square),
            Create(triangle),
            Write(label)
        )

        self.wait()