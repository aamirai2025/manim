from manim import *

class RunTimeTest(Scene):

    def construct(self):

        circle = Circle()
        circle = circle.move_to(LEFT*3)
        
        self.play(Create(circle))

        self.play(
            circle.animate.shift(RIGHT*6),
            run_time=1
        )

        self.wait()

        self.play(FadeOut(circle))

        circle = circle.move_to(LEFT*3)
        
        self.play(Create(circle))

        self.play(
            circle.animate.shift(RIGHT*6),
            run_time=3
        )

        self.wait()

        self.play(FadeOut(circle))

        circle = circle.move_to(LEFT*3)
        
        self.play(Create(circle))

        self.play(
            circle.animate.shift(RIGHT*6),
            run_time=5
        )

        self.wait()


