from manim import *

class LineBending(Scene):
    def construct(self):
        line = Line(start=LEFT, end=LEFT + 4 * RIGHT)  # Adjust the length as desired

        # Move line from left to the stopping point
        self.play(GrowFromPoint(line, line.get_start()))

        # Bending animation
        control_point = line.get_start() + UP + 4 * RIGHT  # Adjust the control point as desired
        self.play(ApplyMethod(line.put_start_and_end_on, line.get_start(), control_point))

        # Convert to arrow animation
        arrow = Arrow(
            start=line.get_start(),
            end=line.get_end(),
            buff=0,
            tip_length=0.2
        )
        self.play(Transform(line, arrow))

        self.wait(1)

scene = LineBending()
scene.render()