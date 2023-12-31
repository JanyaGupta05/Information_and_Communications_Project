
from manim import *

class ShiftBox(Scene):
    def construct(self):
        # Create the RoundedRectangles
        RoundedRectangle1 = RoundedRectangle(width=3, height=6)
        

        RoundedRectangle2 = RoundedRectangle(width=3, height=6)
        

        RoundedRectangle3 = RoundedRectangle(width=3, height=6)

        RoundedRectangle4 = RoundedRectangle(width=2.5, height=1.33)

        RoundedRectangle5 = RoundedRectangle(width=2.5, height=1.33)

        RoundedRectangle6 = RoundedRectangle(width=2.5, height=1.33)

        RoundedRectangle7 = RoundedRectangle(width=2.5, height=1.33)

        RoundedRectangle8 = RoundedRectangle(width=2.5, height=1.33)

        RoundedRectangle9 = RoundedRectangle(width=2.5, height=1.33)

        RoundedRectangle10 = RoundedRectangle(width=2.5, height=1.33)

        RoundedRectangle11 = RoundedRectangle(width=2.5, height=1.33)

        RoundedRectangle12 = RoundedRectangle(width=2.5, height=1.33)
        

        # Add the RoundedRectangles to the scene
        self.play(Create(RoundedRectangle1))
        
        # Shift RoundedRectangle1 to the right side of the page
        self.play(RoundedRectangle1.animate.shift(LEFT * 5))
        

        # # Add RoundedRectangle2 to the scene
        self.play(Create(RoundedRectangle2))
        

        # # Shift RoundedRectangle2 to a second point
        self.play(RoundedRectangle2.animate.shift(RIGHT * 5))
        

        # # Add RoundedRectangle3 to the scene
        # self.play(Create(RoundedRectangle3))
        # self.wait(1)

        # Shift RoundedRectangle3 to a third point
        self.play(RoundedRectangle3.animate.shift(LEFT * 1.5))
        
        
        line1 = Arrow(start=[-7, 3.5, 0], end=[-5, 3.5, 0], buff=0, tip_length=0)
        arrow1 = Arrow(start=[-5, 3.75, 0], end=[-5, 2.75, 0])
        tex1 = Tex("$Q_{1}^{[i]}$",font_size=25)
        tex1.shift(UP * 3.7 + LEFT * 6.5)
        tex2 = Tex("$I(Q_{1}^{[i]};i)=0$",font_size=25)
        tex2.shift(UP * 3.2 + LEFT * 6)
        self.play(Create(line1),Write(tex1),Write(tex2))
        self.play(Create(arrow1))

        self.play(RoundedRectangle4.animate.shift(UP * 2).shift(LEFT * 5))
        tex3 = Tex("$y_{1,1}^{[1]} = h_{1}^{[T]}w_{1}^{[1]}$",font_size=20) 
        tex3.shift( UP * 2.4  + LEFT * 5)
        
        self.play(Write(tex3))

        tex4 = Tex("$y_{1,2}^{[1]} = h_{1}^{[T]}w_{2}^{[1]}$",font_size=20) 
        tex4.shift( UP * 2.1  + LEFT * 5)
        
        self.play(Write(tex4))

        tex5 = Tex("$y_{1,n}^{[1]} = h_{1}^{[T]}w_{n}^{[1]}$",font_size=20) 
        tex5.shift( UP * 1.5  + LEFT * 5)
        
        self.play(Write(tex5))
        
        

        self.play(RoundedRectangle5.animate.shift(UP * 0.5).shift(LEFT * 5))
        tex6 = Tex("$y_{1,1}^{[2]} = h_{1}^{[T]}w_{1}^{[2]}$",font_size=20) 
        tex6.shift( UP * 1 + LEFT * 5)
        
        self.play(Write(tex6))

        tex7 = Tex("$y_{1,2}^{[2]} = h_{1}^{[T]}w_{2}^{[2]}$",font_size=20) 
        tex7.shift( UP * 0.7  + LEFT * 5)
        
        self.play(Write(tex7))

        tex8 = Tex("$y_{1,n}^{[2]} = h_{1}^{[T]}w_{n}^{[2]}$",font_size=20) 
        tex8.shift(  LEFT * 5)
        
        self.play(Write(tex8))
       

        self.play(RoundedRectangle6.animate.shift(DOWN * 1.843).shift(LEFT * 5))
        tex9 = Tex("$y_{1,1}^{[M]} = h_{1}^{[T]}w_{1}^{[M]}$",font_size=20) 
        tex9.shift( DOWN * 1.4 + LEFT * 5)
        
        self.play(Write(tex9))

        tex10 = Tex("$y_{1,2}^{[M]} = h_{1}^{[T]}w_{2}^{[M]}$",font_size=20) 
        tex10.shift( DOWN * 1.7  + LEFT * 5)
        
        self.play(Write(tex10))

        tex11 = Tex("$y_{1,n}^{[M]} = h_{1}^{[T]}w_{n}^{[M]}$",font_size=20) 
        tex11.shift( DOWN * 2.3 + LEFT * 5)
        
        self.play(Write(tex11))
        
        line2 = Arrow(start=[3, 3.5, 0], end=[5, 3.5, 0], buff=0, tip_length=0)
        arrow2 = Arrow(start=[5, 3.75, 0], end=[5, 2.75, 0])
        tex12 = Tex("$Q_{N}^{[i]}$",font_size=25)
        tex12.shift(UP * 3.7 + RIGHT * 3.5)

        tex13 = Tex("$I(Q_{N}^{[i]};i)=0$",font_size=25)
        tex13.shift(UP * 3.2 + RIGHT * 4)

        self.play(Create(line2),Write(tex12),Write(tex13))
        self.play(Create(arrow2))
        self.play(RoundedRectangle7.animate.shift(UP * 2).shift(RIGHT * 5))
        
        tex14 = Tex("$y_{N,1}^{[1]} = h_{1}^{[T]}w_{1}^{[1]}$",font_size=20)  
        tex14.shift( UP * 2.4  + RIGHT * 5)
        
        self.play(Write(tex14))

        
        tex15 = Tex("$y_{N,2}^{[1]} = h_{1}^{[T]}w_{2}^{[1]}$",font_size=20)  
        tex15.shift( UP * 2.1  + RIGHT * 5)
        
        self.play(Write(tex15))

        tex16 = Tex("$y_{N,n}^{[1]} = h_{1}^{[T]}w_{n}^{[1]}$",font_size=20)  
        tex16.shift( UP * 1.5  + RIGHT * 5)
        
        self.play(Write(tex16))
        
        
        self.play(RoundedRectangle8.animate.shift(UP * 0.5).shift(RIGHT * 5))
        
        tex17 = Tex("$y_{N,1}^{[2]} = h_{2}^{[T]}w_{1}^{[2]}$",font_size=20)  
        tex17.shift( UP * 1 + RIGHT * 5)
        
        self.play(Write(tex17))

        
        tex18 = Tex("$y_{N,2}^{[2]} = h_{2}^{[T]}w_{2}^{[2]}$",font_size=20) 
        tex18.shift( UP * 0.7  + RIGHT * 5)
        
        self.play(Write(tex18))

        
        tex19 = Tex("$y_{N,n}^{[2]} = h_{2}^{[T]}w_{n}^{[2]}$",font_size=20) 
        tex19.shift( RIGHT* 5)
        
        self.play(Write(tex19))
        
       
        self.play(RoundedRectangle9.animate.shift(DOWN * 1.843).shift(RIGHT * 5))
        
        tex20 = Tex("$y_{N,1}^{[M]} = h_{1}^{[T]}w_{1}^{[M]}$",font_size=20) 
        tex20.shift( DOWN * 1.4 + RIGHT * 5)
        
        self.play(Write(tex20))

        
        tex21 = Tex("$y_{N,2}^{[M]} = h_{1}^{[T]}w_{2}^{[M]}$",font_size=20) 
        tex21.shift( DOWN * 1.7  + RIGHT * 5)
        
        self.play(Write(tex21))

        
        tex22 = Tex("$y_{N,n}^{[M]} = h_{1}^{[T]}w_{n}^{[M]}$",font_size=20) 
        tex22.shift( DOWN * 2.3 + RIGHT * 5)
        
        self.play(Write(tex22))
        
        line3 = Arrow(start=[-3.5, 3.5, 0], end=[-1.5, 3.5, 0], buff=0, tip_length=0)
        arrow3 = Arrow(start=[-1.5, 3.75, 0], end=[-1.5, 2.75, 0])
        tex23 = Tex("$Q_{2}^{[i]}$",font_size=25)
        tex23.shift(UP * 3.7 + LEFT * 3)

        tex24 = Tex("$I(Q_{2}^{[i]};i)=0$",font_size=25)
        tex24.shift(UP * 3.2 + LEFT * 2.5)

        self.play(Create(line3),Write(tex23),Write(tex24))
        self.play(Create(arrow3))
        self.play(RoundedRectangle10.animate.shift(UP * 2).shift(LEFT * 1.5))
        tex25 = Tex("$y_{2,1}^{[1]} = h_{2}^{[T]}w_{1}^{[1]}$",font_size=20)
        tex25.shift( UP * 2.4  + LEFT * 1.5)
        
        self.play(Write(tex25))

        tex26 = Tex("$y_{2,2}^{[1]} = h_{2}^{[T]}w_{2}^{[1]}$",font_size=20)
        tex26.shift( UP * 2.1  + LEFT * 1.5)
        
        self.play(Write(tex26))

        
        tex27 = Tex("$y_{2,n}^{[1]} = h_{2}^{[T]}w_{n}^{[1]}$",font_size=20)
        tex27.shift( UP * 1.5  + LEFT * 1.5)
        
        self.play(Write(tex27))
        

        self.play(RoundedRectangle11.animate.shift(UP * 0.5).shift(LEFT * 1.5))
        
        tex28 = Tex("$y_{2,1}^{[2]} = h_{2}^{[T]}w_{1}^{[2]}$",font_size=20)
        tex28.shift( UP * 1 + LEFT * 1.5)
        
        self.play(Write(tex28))

        tex29 = Tex("$y_{2,2}^{[2]} = h_{2}^{[T]}w_{2}^{[2]}$",font_size=20) 
        tex29.shift( UP * 0.7  + LEFT * 1.5)
        
        self.play(Write(tex29))

        tex30 = Tex("$y_{2,n}^{[2]} = h_{2}^{[T]}w_{n}^{[2]}$",font_size=20) 
        tex30.shift(  LEFT * 1.5)
        
        self.play(Write(tex30))
    

        self.play(RoundedRectangle12.animate.shift(DOWN * 1.843).shift(LEFT * 1.5))
        tex31 = Tex("$y_{2,1}^{[M]} = h_{2}^{[T]}w_{1}^{[M]}$",font_size=20) 
        tex31.shift( DOWN * 1.4 + LEFT * 1.5)
        
        self.play(Write(tex31))

        tex32 = Tex("$y_{2,2}^{[M]} = h_{2}^{[T]}w_{2}^{[M]}$",font_size=20)
        tex32.shift( DOWN * 1.7  + LEFT * 1.5)
        
        self.play(Write(tex32))

        tex33 = Tex("$y_{2,n}^{[M]} = h_{2}^{[T]}w_{n}^{[M]}$",font_size=20) 
        tex33.shift( DOWN * 2.3 + LEFT * 1.5)
        
        self.play(Write(tex33))
       
        
        group = Group(line1,arrow1,line2,arrow2,line3,arrow3,RoundedRectangle1,RoundedRectangle2,RoundedRectangle3,RoundedRectangle4,RoundedRectangle5,RoundedRectangle6,RoundedRectangle7,RoundedRectangle8,RoundedRectangle9,RoundedRectangle10,RoundedRectangle11,RoundedRectangle12,tex1,tex2,tex3,tex4,tex5,tex6,tex7,tex8,tex9,tex10,tex11,tex12,tex13,tex14,tex15,tex16,tex17,tex18,tex19,tex20,tex21,tex22,tex23,tex24,tex25,tex26,tex27,tex28,tex29,tex30,tex31,tex32,tex33)
        self.play(Transform(group, group.copy().shift(UP * 1).scale(0.5)))
        
        arrow3 = Arrow(start=[-2.7, 0.0, 0], end=[-2.7, -0.8, 0])
        self.play(Create(arrow3))
        tex34 = Tex("$A_{1}^{[i]}$",font_size=23)
        tex34.shift(LEFT * 2.7 + DOWN * 0.8)
        self.play(Write(tex34))
        arrow4 = Arrow(start=[-0.9, 0.0, 0], end=[-0.9, -0.8, 0])
        self.play(Create(arrow4))
        tex35 = Tex("$A_{2}^{[i]}$",font_size=23)
        tex35.shift(LEFT * 0.9 + DOWN * 0.8)
        self.play(Write(tex35))
        arrow5 = Arrow(start=[2.4, 0, 0], end=[2.4, -0.8, 0])
        self.play(Create(arrow5))
        tex36 = Tex("$A_{N}^{[i]}$",font_size=23)
        tex36.shift(RIGHT * 2.4 + DOWN * 0.8)
        self.play(Write(tex36))

        rectangle1 = Rectangle(width=8,height=0.8)
        text1 = Text("combining answer strings at the user",font_size=21)
        text1.shift(DOWN * 1.5)
        self.play(rectangle1.animate.shift(DOWN * 1.5), Write(text1))
        arrow6 = Arrow(start=[0, -1.8, 0], end=[0, -2.7, 0])
        self.play(Create(arrow6))

        tex37 = Tex("$H(W_{i}|A_{1}^{[i]},A_{2}^{[i]},...,A_{n}^{[i]},Q_{1}^{[i]},Q_{2}^{[i]},..,Q_{N}^{[i]})$",font_size=26)
        tex37.shift(DOWN * 2.8)

        self.play(Write(tex37))
        self.wait(1)

#         self.wait(1)
        


# # # scene = ShiftBox()
# # # scene.render()
