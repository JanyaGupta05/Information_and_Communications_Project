from manim import *

class TexTextExample(Scene):
    def construct(self):

        tex = Tex("$y_{1,1}^{[1]} = h_{1}^{[T]}w_{1}^{[1]}$",font_size=25) 
        tex.shift( UP * 2  + LEFT * 5)

        self.play(Write(tex))

scene = TexTextExample()
scene.render()
