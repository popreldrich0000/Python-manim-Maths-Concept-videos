from cmath import cos, sin 
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *


class DottedLine(Line):

    """A dotted :class:`Line`.
    Parameters
    ----------
    args : Any
        Arguments to be passed to :class:`Line`
    dot_spacing : Optional[:class:`float`]
        Minimal spacing of the dots. The spacing is scaled up to fit the start and end of the line.
    dot_kwargs : Any
        Arguments to be passed to ::class::`Dot`
    kwargs : Any
        Additional arguments to be passed to :class:`Line`
    Examples
    --------
    .. manim:: DottedLineExample
        :save_last_frame:
        class DottedLineExample(Scene):
            def construct(self):
                # default dotted line
                dotted_1 = DottedLine(LEFT, RIGHT))
                # reduced spacing
                dotted_2 = DottedLine(LEFT, RIGHT, dot_spacing=.3).shift(.5*DOWN))
                # smaller and colored dots
                dotted_3 = DottedLine(LEFT, RIGHT, dot_kwargs=dict(radius=.04, color=YELLOW)).shift(DOWN))
        
                self.add(dotted_1, dotted_2, dotted_3)

    """

    def __init__(
        self,
        *args,
        dot_spacing=0.4,
        dot_kwargs={},
        **kwargs
    ):
        Line.__init__(self, *args, **kwargs)
        n_dots = int(self.get_length() / dot_spacing) + 1
        dot_spacing = self.get_length() / (n_dots - 1)
        unit_vector = self.get_unit_vector()
        start = self.start

        self.dot_points = [start + unit_vector * dot_spacing * x for x in range(n_dots)]
        self.dots = [Dot(point, **dot_kwargs) for point in self.dot_points]

        self.clear_points()

        self.add(*self.dots)

        self.get_start = lambda: self.dot_points[0]
        self.get_end = lambda: self.dot_points[-1]

    def get_first_handle(self):
        return self.dot_points[-1]

    def get_last_handle(self):
        return self.dot_points[-2]



class Concept8_1(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("When 4 rays join, the angles sum up to 360°", font ="Metal" ,font_size=32).set_color(GREEN, PINK)
        title.to_edge(UP, buff=1)
        title.to_edge(LEFT, buff=0.6)
        self.play(Write(title))

        self.wait(4)
        
        txt1 = Text("Let   OP ," , color='BLUE',  t2c={'[6:11]': RED } ,slant=ITALIC ).set_height(0.3)
        txt1.to_edge(LEFT,buff=1)
        txt1.to_edge(DOWN,buff=0.5)
        OP = Vector(direction= [2.5,0,0]).set_color(color=[RED])
        O = Dot([0,0,0]).set_color(RED)
        tO = Tex(r"$O$"  , font_size=18 , color = WHITE).move_to(np.array([O.get_center()[0],O.get_center()[1]-0.8,0])).set_height(0.2)
        P = Dot([2.2,0,0]).set_color(RED)
        tP = Tex(r"$P$"  , font_size=18 , color = RED).move_to(np.array([P.get_center()[0],P.get_center()[1]-0.3,0])).set_height(0.2)

        self.play(FadeIn(txt1,OP,O,tO,tP,P))

        self.wait(2)

        txt2 = Text("OQ ," ,slant=ITALIC ).set_height(0.3).set_color(color=[GREEN])
        txt2.to_edge(LEFT,buff=2.7)
        txt2.to_edge(DOWN,buff=0.5)
        OQ=  Vector(direction= [-2.5*3/5,2.5*4/5,0]).set_color(color=[GREEN])
        Q= Dot([-2.2*3/5,2.2*4/5,0]).set_color(GREEN)
        tQ = Tex(r"$Q$"  , font_size=18 , color = GREEN).move_to(np.array([Q.get_center()[0],Q.get_center()[1]-0.3,0])).set_height(0.2)

        self.play(FadeIn(txt2,OQ,Q,tQ))

        self.wait(2)


        txt3 = Text("OR ," , color='YELLOW',slant=ITALIC ).set_height(0.3)
        txt3.to_edge(LEFT,buff=3.7)
        txt3.to_edge(DOWN,buff=0.5)
        OR = Vector(direction= [-2.5*4/5,-2.5*3/5,0]).set_color(color=[YELLOW])
        R= Dot([-2.2*4/5,-2.2*3/5,0]).set_color(YELLOW)
        tR = Tex(r"$R$"  , font_size=18 , color = YELLOW).move_to(np.array([R.get_center()[0],R.get_center()[1]-0.3,0])).set_height(0.2)

        self.play(FadeIn(txt3,OR,R,tR))
        
        self.wait(2)
        
        
        txt4 = Text("OS " ,slant=ITALIC ).set_height(0.3).set_color(color=[BLUE])
        txt4.to_edge(LEFT,buff=4.7)
        txt4.to_edge(DOWN,buff=0.5)
        OS = Vector(direction= [2.5/1.41,-2.5/1.41,0]).set_color(color=[BLUE])
        S= Dot([2.2/1.41,-2.2/1.41,0]).set_color(BLUE)
        tS = Tex(r"$S$"  , font_size=18 , color = BLUE).move_to(np.array([S.get_center()[0],S.get_center()[1]-0.3,0])).set_height(0.2)

        self.play(FadeIn(txt4,OS,S,tS))
        
        self.wait(2)

        txt5 = Text("be four rays at point O." , color='BLUE',slant=ITALIC ).set_height(0.3)
        txt5.to_edge(LEFT,buff=5.7)
        txt5.to_edge(DOWN,buff=0.5)
        
        self.play(FadeIn(txt5))

        angles1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = OQ.get_angle(), start_angle=0, color = RED,fill_opacity=0.5, stroke_width=0)
        angles2 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI  + PI+ OR.get_angle() - OQ.get_angle(), start_angle=OQ.get_angle(), color = GREEN,fill_opacity=0.5, stroke_width=0)
        angles3 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = OS.get_angle() - OR.get_angle(), start_angle=OR.get_angle(), color = YELLOW,fill_opacity=0.5, stroke_width=0)
        angles4 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -OS.get_angle(), start_angle=OS.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0)

        self.play(FadeIn(angles1,angles2,angles3,angles4))
        self.wait(4)

class Concept8_2(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("When 4 rays join, the angles sum up to 360°", font ="Metal" ,font_size=32).set_color(GREEN, PINK)
        title.to_edge(UP, buff=1)
        title.to_edge(LEFT, buff=0.6)
        self.add(title)

        
        txt1 = Text("Let   OP ," , color='BLUE',  t2c={'[6:11]': RED } ,slant=ITALIC ).set_height(0.3)
        txt1.to_edge(LEFT,buff=1)
        txt1.to_edge(DOWN,buff=0.5)
        OP = Vector(direction= [2.5,0,0]).set_color(color=[RED])
        O = Dot([0,0,0]).set_color(RED)
        tO = Tex(r"$O$"  , font_size=18 , color = WHITE).move_to(np.array([O.get_center()[0],O.get_center()[1]-0.8,0])).set_height(0.2)
        P = Dot([2.2,0,0]).set_color(RED)
        tP = Tex(r"$P$"  , font_size=18 , color = RED).move_to(np.array([P.get_center()[0],P.get_center()[1]-0.3,0])).set_height(0.2)

        self.add(txt1,OP,O,tO,tP,P)


        txt2 = Text("OQ ," ,slant=ITALIC ).set_height(0.3).set_color(color=[GREEN])
        txt2.to_edge(LEFT,buff=2.7)
        txt2.to_edge(DOWN,buff=0.5)
        OQ=  Vector(direction= [-2.5*3/5,2.5*4/5,0]).set_color(color=[GREEN])
        Q= Dot([-2.2*3/5,2.2*4/5,0]).set_color(GREEN)
        tQ = Tex(r"$Q$"  , font_size=18 , color = GREEN).move_to(np.array([Q.get_center()[0],Q.get_center()[1]-0.3,0])).set_height(0.2)

        self.add(txt2,OQ,Q,tQ)



        txt3 = Text("OR ," , color='YELLOW',slant=ITALIC ).set_height(0.3)
        txt3.to_edge(LEFT,buff=3.7)
        txt3.to_edge(DOWN,buff=0.5)
        OR = Vector(direction= [-2.5*4/5,-2.5*3/5,0]).set_color(color=[YELLOW])
        R= Dot([-2.2*4/5,-2.2*3/5,0]).set_color(YELLOW)
        tR = Tex(r"$R$"  , font_size=18 , color = YELLOW).move_to(np.array([R.get_center()[0],R.get_center()[1]-0.3,0])).set_height(0.2)

        self.add(txt3,OR,R,tR)
        
        
        
        txt4 = Text("OS " ,slant=ITALIC ).set_height(0.3).set_color(color=[BLUE])
        txt4.to_edge(LEFT,buff=4.7)
        txt4.to_edge(DOWN,buff=0.5)
        OS = Vector(direction= [2.5/1.41,-2.5/1.41,0]).set_color(color=[BLUE])
        S= Dot([2.2/1.41,-2.2/1.41,0]).set_color(BLUE)
        tS = Tex(r"$S$"  , font_size=18 , color = BLUE).move_to(np.array([S.get_center()[0],S.get_center()[1]-0.3,0])).set_height(0.2)

        self.add(txt4,OS,S,tS)
        

        txt5 = Text("be four rays at point O." , color='BLUE',slant=ITALIC ).set_height(0.3)
        txt5.to_edge(LEFT,buff=5.7)
        txt5.to_edge(DOWN,buff=0.5)
        
        self.add(txt5)

        angles1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = OQ.get_angle(), start_angle=0, color = RED,fill_opacity=0.5, stroke_width=0)
        angles2 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI  + PI+ OR.get_angle() - OQ.get_angle(), start_angle=OQ.get_angle(), color = GREEN,fill_opacity=0.5, stroke_width=0)
        angles3 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = OS.get_angle() - OR.get_angle(), start_angle=OR.get_angle(), color = YELLOW,fill_opacity=0.5, stroke_width=0)
        angles4 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -OS.get_angle(), start_angle=OS.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0)

        self.add(angles1,angles2,angles3,angles4)


        self.wait(4)

        txt6 = Tex("To Proof : " + r" $\angle$POQ + $\angle$QOR + $\angle$ROS + $\angle$SOP   \ \ = \ \  360°"   , font_size=24 , color = WHITE)
        txt6.to_edge(RIGHT,buff=0.5)
        txt6.to_edge(UP,buff=1.5)
        self.play(FadeIn(txt6))
        txt7 = Tex("="   , font_size=24 , color = WHITE)
        txt7.to_edge(RIGHT,buff=1.2)
        txt7.to_edge(UP,buff=2.5)

        angles1_1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = OQ.get_angle(), start_angle=0, color = RED,fill_opacity=0.5, stroke_width=0)
        angles2_1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI  + PI+ OR.get_angle() - OQ.get_angle(), start_angle=OQ.get_angle(), color = GREEN,fill_opacity=0.5, stroke_width=0)
        angles3_1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = OS.get_angle() - OR.get_angle(), start_angle=OR.get_angle(), color = YELLOW,fill_opacity=0.5, stroke_width=0)
        angles4_1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -OS.get_angle(), start_angle=OS.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0)
        fullangle =  AnnularSector(inner_radius=0, outer_radius=0.5, angle = 2*PI, start_angle=0, color = PINK,fill_opacity=0.5, stroke_width=0)
        fullangle.to_edge(RIGHT,0)
        fullangle.to_edge(UP,2)

        self.play(FadeIn(angles1_1,angles2_1,angles3_1,angles4_1))
        anglegrp = VGroup(angles1_1,angles2_1,angles3_1,angles4_1)
        self.play(anglegrp.animate.to_edge(RIGHT,buff=2.5))
        self.play(anglegrp.animate.to_edge(UP,buff=2))

        self.play(FadeIn(fullangle,txt7))
        self.wait(4)
        self.play(angles1_1.animate.to_edge(RIGHT,buff=4.8))
        self.play(angles1_1.animate.to_edge(UP,buff=2))
        self.play(angles2_1.animate.to_edge(UP,buff=2))
        self.play(angles2_1.animate.to_edge(RIGHT,buff=3.8))
        self.play(angles3_1.animate.to_edge(UP,buff=2))
        self.play(angles4_1.animate.to_edge(RIGHT,buff=1.8))
        self.play(angles4_1.animate.to_edge(UP,buff=2.2))

        self.wait(2)

        consray = DashedLine(start=np.array([0, 0, 0]),end=np.array([-2.5,0,0])).set_color(color=[PINK])
        self.play(FadeIn(consray))
        T= Dot([-2.5,0,0]).set_color(PINK)
        tT = Tex(r"$T$"  , font_size=18 , color = PINK).move_to(np.array([T.get_center()[0],T.get_center()[1]-0.3,0])).set_height(0.2)
        self.play(FadeIn(T,tT))
        self.wait(2)
        self.wait(3)
        self.remove(txt1,txt2,txt3,txt4,txt5)
        shiftgrp =  VGroup(OP,O,tO,tP,P,OQ,Q,tQ,OR,R,tR,OS,S,tS,angles1,angles2,angles3,angles4,consray,T,tT)
        self.play(shiftgrp.animate.shift(LEFT*4.5))
        self.wait(4)
        angles1_1_2 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI - OQ.get_angle(), start_angle=OQ.get_angle(), color = GREEN,fill_opacity=0.5, stroke_width=0).shift(LEFT*4.5)

        anglesPOQ = AnnularSector(inner_radius=0, outer_radius=0.5, angle = OQ.get_angle(), start_angle=0, color = RED,fill_opacity=0.5, stroke_width=0).shift(LEFT*4.5)
        self.play(FadeIn(angles1_1_2,anglesPOQ))
        
        angrp = VGroup(anglesPOQ,angles1_1_2)
        self.play(angrp.animate.shift(RIGHT*6))
        txt8 = Tex( r" $\angle$QOT + $\angle$POQ  \ \ = \ \  180°"   , font_size=24 , color = WHITE)
        txt8.to_edge(RIGHT,buff = 3.8)
        txt8.to_edge(UP,buff = 4.5)
        self.play(FadeIn(txt8))
        txt81 = Tex( " (Linear pair axiom)"   , font_size=24 , color = WHITE)
        txt81.to_edge(RIGHT,buff = 1.5)
        txt81.to_edge(UP,buff = 4.5)
        self.play(FadeIn(txt81))

        anglesstrai = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI, start_angle=0, color = PINK,fill_opacity=0.5, stroke_width=0).shift(RIGHT*3.5)
        txt9 = Tex( r" = "   , font_size=24 , color = WHITE).shift(2.6*RIGHT+UP*0.25)
        self.play(FadeIn(anglesstrai,txt9))
        self.play(angles1_1_2.animate.shift(LEFT*1))
        txt10 = Tex( r" + "   , font_size=24 , color = WHITE).shift(0.9*RIGHT+UP*0.25)

        self.play(FadeIn(txt10))

        txt11 = Tex( r" $\angle$TOR + $\angle$ROP  \ \ = \ \  180°"    , font_size=24 , color = WHITE)
        txt11.to_edge(RIGHT,buff = 3.8)
        txt11.to_edge(UP,buff = 6.5)
        self.play(FadeIn(txt11))
        txt111 = Tex( " (Linear pair axiom)"   , font_size=24 , color = WHITE)
        txt111.to_edge(RIGHT,buff = 1.5)
        txt111.to_edge(UP,buff = 6.5)
        self.play(FadeIn(txt111))
        angles1tor = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI + OR.get_angle(), start_angle=PI, color = GREEN,fill_opacity=0.5, stroke_width=0).shift(LEFT*4.5)
        angles3ROS = AnnularSector(inner_radius=0, outer_radius=0.5, angle = OS.get_angle() - OR.get_angle(), start_angle=OR.get_angle(), color = YELLOW,fill_opacity=0.5, stroke_width=0).shift(LEFT*4.5)
        angles4SOP = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -OS.get_angle(), start_angle=OS.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0).shift(LEFT*4.5)
        self.play(FadeIn(angles1tor,angles3ROS,angles4SOP))
        angrp1 = VGroup(angles1tor,angles3ROS,angles4SOP)
        self.play(angrp1.animate.shift(RIGHT*6+DOWN*1.5))
        self.wait(3)
        anglesstrai1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI, start_angle=PI, color = PINK,fill_opacity=0.5, stroke_width=0).shift(RIGHT*3.5 + DOWN*1.5)
        txt121 = Tex( r" = "   , font_size=24 , color = WHITE).shift(2.6*RIGHT+DOWN*1.75)
        self.play(FadeIn(anglesstrai1,txt121))
        self.wait(3)
        self.play(angles1tor.animate.shift(LEFT*1.7))
        self.wait(4)
        self.play(angles3ROS.animate.shift(LEFT*0.8))
        self.wait(4)
        txt12 = Tex( r" $\angle$TOR + $\angle$ROS + $\angle$SOP \ \ = \ \  180°"    , font_size=24 , color = WHITE)

        txt12.to_edge(RIGHT,buff = 3.8)
        txt12.to_edge(UP,buff = 6.5)
        self.remove(txt11)

        self.play(FadeIn(txt12))
        txt13 = Tex( r"+"    , font_size=24 , color = WHITE).shift(1.35*RIGHT+DOWN*1.75)
        txt14 = Tex( r"+"    , font_size=24 , color = WHITE).shift(DOWN*1.75)

        self.play(FadeIn(txt13,txt14))
        self.wait(4)
        self.remove(txt111,txt81)
        self.play(txt8.animate.shift(DOWN*2+LEFT*6))
        self.wait(4)

        txt15 = Tex( r"  $\angle$POQ + $\angle$QOT + $\angle$TOR + $\angle$ROS + $\angle$SOP \ \ = \ \  360°"    , font_size=24 , color = WHITE)
        txt15.to_edge(RIGHT,buff = 3.8)
        txt15.to_edge(UP,buff = 6.5)
        self.remove(txt12,txt8)

        self.play(FadeIn(txt15))
        self.wait(5)
        self.play(anglesstrai1.animate.shift(UP*1.5))
        self.wait(2)
        strgrp = VGroup(anglesstrai1,anglesstrai)
        self.play(strgrp.animate.shift(RIGHT*2))
        self.remove(txt121)
        self.play(txt9.animate.shift(RIGHT*2+DOWN*0.25))
        self.remove(txt13,txt14,txt10)

        self.play(angles4SOP.animate.shift(UP*1.75+RIGHT*2))
        self.play(angles3ROS.animate.shift(UP*1.75+RIGHT*2))

        self.play(angles1tor.animate.shift(UP*1.5+RIGHT*0.7))
        
        self.play(anglesPOQ.animate.shift(LEFT*1))
        grengrp = VGroup(angles1tor,angles1_1_2)
        self.play(grengrp.animate.shift(RIGHT*1.5))
        self.wait(2)
        rec1 =  Rectangle(fill_color = RED, width = 2 , height = 1,fill_opacity=0.5).to_edge(UP,buff = 6.2).to_edge(LEFT,buff = 5.25)
        self.play(FadeIn(rec1))
        self.wait(3)
        txt16 = Tex( r"  $\angle$QOR"    , font_size=24 , color = WHITE)
        txt16.to_edge(LEFT,buff = 6)
        txt16.to_edge(DOWN,buff = 0.5)
        self.play(FadeIn(txt16))
        self.wait(3)
        txt17 = Tex( r"  $\angle$POQ + $\angle$QOR + $\angle$ROS + $\angle$SOP \ \ = \ \  360°"    , font_size=24 , color = WHITE)
        txt17.to_edge(RIGHT,buff = 3.8)
        txt17.to_edge(UP,buff = 6.5)
        self.remove(txt16,txt15,rec1)
        self.play(FadeIn(txt17))
        self.wait(3)
Animation1 = Concept8_2()
Animation1.construct()