from manim import* 

class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
        text1 = Text("The Capacity of Private Information",font_size=35)
        text2 = Text("Retrieval from Coded Databases",font_size=35)
        text1.shift(UP * 1.5)
        text2.shift(UP * 1)
        self.play(FadeIn(text1),FadeIn(text2))
        text3 = Text("Meemansa Pandey",font_size=30)
        text4 = Text("Janya Gupta",font_size=30)
        text5 = Text("2022102036",font_size=30)
        text6 = Text("2022102033",font_size=30)
        text3.shift(DOWN * 2 + LEFT * 4)
        text4.shift(DOWN * 2 + RIGHT * 4)
        text5.shift(DOWN * 2.5 + LEFT * 4)
        text6.shift(DOWN * 2.5 + RIGHT * 4)
        self.play(FadeIn(text3),FadeIn(text4),FadeIn(text5),FadeIn(text6))
        self.wait(2)


