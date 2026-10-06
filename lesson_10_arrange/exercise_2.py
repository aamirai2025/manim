from manim import *

class Arrange(Scene):

    def construct(self):

        circle = Circle()
        square = Square()
        triangle = Triangle()
        star = Star()

        collection = VGroup(
            circle,
            square,
            triangle,
            star
        )

        collection.arrange(
            DOWN,
            buff=0.5
            )

        self.play(Create(collection))

        self.wait()