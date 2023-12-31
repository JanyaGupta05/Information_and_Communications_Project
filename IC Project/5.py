from manim import*

class NextToExample(Scene):
    def construct(self):
        # Create two squares
        square1 = Square()
        square2 = Square(fill_opacity= 0.5, fill_color=ORANGE)
        square3 = Square(fill_opacity= 0.5, fill_color=BLUE).next_to(square1, LEFT, buff=0.1)

        # Position square2 next to square1
        square2.next_to(square1, RIGHT, buff=0.1)

        # Add the squares to the scene
        # self.add(square1)


        grp = VGroup(square1, square2) 
        grp2 = VGroup(square3)

        grp3 = grp + grp2

        self.play(DrawBorderThenFill(grp2), DrawBorderThenFill(grp))

        self.play(grp3.animate.shift(0.75*LEFT))

        # grp3 -= grp2

        self.play((grp3-grp2).animate.shift(UP))
        self.play((grp3-grp2-square1).animate.shift(DOWN))



        self.wait(2)
