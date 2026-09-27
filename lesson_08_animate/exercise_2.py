from manim import *

class Resize(Scene):

    def construct(self):

        square = Square()
        square = square.set_stroke(RED, width=5).set_fill(RED, opacity=0.3)

        self.play(Create(square))

        self.wait(1)

        big = square.animate.scale(2)
        
        self.play(big)

        self.wait(1)

        small = square.animate.scale(0.5)

        self.play(small)

        self.wait()