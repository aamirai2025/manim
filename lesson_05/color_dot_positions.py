from manim import *

class ColorDotPositios(Scene):

    def construct(self):

        dot1 = Dot([2, 2, 0])
        dot1.set_color(RED)

        dot2 = Dot([-2, 2, 0])
        dot2.set_color(BLUE)
        
        dot3 = Dot([-2, -2, 0])
        dot3.set_color(GREEN)
        
        dot4 = Dot([2, -2, 0])
        dot4.set_color(ORANGE)

        line1 = Line(
            dot1.get_center(),
            dot2.get_center()
        )

        line2 = Line(
            dot2.get_center(),
            dot3.get_center()
        )

        line3 = Line(
            dot3.get_center(),
            dot4.get_center()
        )

        line4 = Line(
            dot4.get_center(),
            dot1.get_center()
        )

        self.play(
            Create(dot1),
            Create(dot2),
            Create(dot3),
            Create(dot4),
            Create(line1),
            Create(line2),
            Create(line3),
            Create(line4)
        )

        self.wait()