from manim import *

class RectangleExample(Scene):
    def construct(self):
        rectangle = Rectangle()
        rectangle.width = 3  # Swapped with height
        rectangle.height = 3  # Swapped with width
        rectangle.fill_color = BLUE
        rectangle.stroke_color = WHITE
        rectangle.stroke_width = 2

        self.add(rectangle)
        self.play(DrawBorderThenFill(rectangle))
        self.wait(2)

scene = RectangleExample()
scene.render()