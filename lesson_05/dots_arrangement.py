from manim import *

class DotsArrangement(Scene):

    def construct(self):

        dot1 = Dot()
        dot1.set_color(RED).move_to(RIGHT*3)

        label1 = Text("RIGHT")
        label1.set_color(RED).next_to(dot1, RIGHT)

        self.play(
            Create(dot1),
            Write(label1)
        )

        dot2 = Dot()
        dot2.set_color(RED).move_to(LEFT*3)

        label2 = Text("LEFT")
        label2.set_color(RED).next_to(dot2, LEFT)

        self.play(
            Create(dot2),
            Write(label2)
        )

        dot3 = Dot()
        dot3.set_color(RED).move_to(UP*3)

        label3 = Text("UP")
        label3.set_color(RED).next_to(dot3, UP)

        self.play(
            Create(dot3),
            Write(label3)
        )

        dot4 = Dot()
        dot4.set_color(RED).move_to(DOWN*3)

        label4 = Text("DOWN")
        label4.set_color(RED).next_to(dot4, DOWN)

        self.play(
            Create(dot4),
            Write(label4)
        )

        self.wait()