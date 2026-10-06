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
            RIGHT,
            buff=1
            )

        self.play(Create(collection))

        self.wait()