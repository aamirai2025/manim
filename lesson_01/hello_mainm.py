from manim import *

class TextAnim(Scene):
    def construct(self):
        text = Text("Hello! Manim.")
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
