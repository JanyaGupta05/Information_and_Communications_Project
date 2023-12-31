from manim import *

class RectangleExample(Scene):
    def construct(self):
        rectangle = Rectangle()
        rectangle.height = 3
        rectangle.width = 2
        rectangle.stroke_color = WHITE
        rectangle.stroke_width = 4

        self.play(Create(rectangle))
        self.wait(2)

scene = RectangleExample()
scene.render()
