from manim import *

class Shift(Scene):
    def construct(self):
        text = Text("PIR Problem",font_size=30)
        text.shift(UP * 3)
        self.play(Write(text))
        self.wait(35)
        self.play(FadeOut(text))
        text1 = Text("(N, K ) MDS code",font_size=30)
        text1.shift(UP * 3)
        
        self.play(Write(text1))
        self.wait(6)
        # Create an oval
        oval = Circle()
        oval.stretch(2, 1)  # Stretch the circle along the y-axis
        oval.shift(LEFT * 4)
        oval.set_fill(color=RED, opacity=0.5)
        text2 = Text("k",font_size=18)
        text2.shift(UP * 1 + LEFT * 4)
        text3 = Text("Sub-Packets",font_size=18)
        text3.shift(UP * 0.5 + LEFT * 4)
        oval1 = Circle()
        oval1.stretch(2, 1)  # Stretch the circle along the y-axis
        oval1.shift(RIGHT * 4)
        oval1.set_fill(color=RED, opacity=0.5)
        text4 = Text("N",font_size=18)
        text4.shift(UP * 1 + RIGHT * 4)
        text5 = Text("Sub-Packets",font_size=18)
        text5.shift(UP * 0.5 + RIGHT * 4)
        oval.set_stroke(color=RED)
        oval1.set_stroke(color=RED)  
        self.play(Create(oval))
        
        self.play(Write(text2),Write(text3))
        self.wait(1)
        start_point = [-2, 0, 0]
        end_point = [2, 0, 0]
        curved_arrow = CurvedArrow(start_point, end_point, angle=-TAU/4)
        text6 = Text("This code tolerates upto N-k errors", font_size=26)
        text6.shift(DOWN * 2)
        text7 = Text("The best known achievable scheme for MDS coded PIR problem has a Retrieval Rate of:", font_size=20)
        tex8 = Tex("$R=1-R_{C}$",font_size=24)
        text7.shift(DOWN * 3)
        tex8.shift(DOWN * 3.3)
        self.play(Create(curved_arrow))
        self.wait(1)
        self.play(Create(oval1))
        self.play(Write(text4),Write(text5))
        self.wait(1)
        self.play(FadeIn(text6))
        self.wait(0.5)
        self.play(FadeIn(text7))
        self.play(FadeIn(tex8))
        self.wait(5)
        

