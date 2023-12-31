from manim import *

class RectangleExample(Scene):
    def construct(self):
        rectangle = Rectangle()
        rectangle.width = 9
        rectangle.height = 5
        rectangle.stroke_color = WHITE
        rectangle.stroke_width = 4

        self.add(rectangle)
        self.play(DrawBorderThenFill(rectangle))
        self.wait(2)

scene = RectangleExample()
scene.render()