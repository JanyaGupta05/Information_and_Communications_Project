from manim import *

class DrawBox(Scene):
    def construct(self):
        # Set up the box parameters
        width = 4
        height = 3
        depth = 2
        box_color = BLUE

        # Create the box
        box = Cube(side_length=width, fill_color=box_color, fill_opacity=0.8, stroke_width=0.3)
        
        # Position the box
        box.shift(UP * height / 2)

        # Add the box to the scene
        self.add(box)

        # Add labels to the box
        label_width = MathTex("W").scale(0.8)
        label_height = MathTex("H").scale(0.8)
        label_depth = MathTex("D").scale(0.8)

        label_width.next_to(box, RIGHT)
        label_height.next_to(box, UP)
        label_depth.next_to(box, OUT)

        self.add(label_width, label_height, label_depth)

        # Show the result
        self.wait()

# Create the animation
scene = DrawBox()
scene.render()
