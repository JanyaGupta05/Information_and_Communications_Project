from manim import *

class GrowingAndRotatingArrow(Scene):
    def construct(self):
        # Create the arrow
        arrow = Arrow(start=[-1, 0, 0], end=[1, 0, 0], color=WHITE)

        # Animate the growth of the arrow
        self.play(GrowArrow(arrow))

        # Animate the rotation of the arrow
        self.play(Rotate(arrow, angle=-PI/2, about_point=arrow.get_start()))

        # Wait for a few seconds
        self.wait(2)

scene = GrowingAndRotatingArrow()
scene.render()