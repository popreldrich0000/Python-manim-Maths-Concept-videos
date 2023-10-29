from cmath import cos, sin 
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *

class Concept5_1(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Axiom: If a ray stands on a line, \n then the sum of two adjacent angles so formed is 180°.", font ="Metal" ).set_color(GREEN, PINK).set_height(0.8)
        theta = ValueTracker(PI/4)

        self.add(logo)        
        title.to_edge(UP, buff=1)
        title.to_edge(LEFT, buff=0.6)

        self.play(Write(title))
        self.wait(2)
        line1_R = Vector(direction= [4,0,0]).set_color(color=[RED])
        line1_R.shift(DOWN*2.5)
        # line1_R.to_edge(LEFT,buff = 5)

        line1_L = Vector(direction= [-4,0,0]).set_color(color=[RED])
        line1_L.shift(DOWN * 2.5)
        # line1_L.to_edge(LEFT,buff = 5)

        A = Dot(point=np.array([-3.2, 0, 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=YELLOW).shift(DOWN * 2.5)
        B = Dot(point=np.array([3.2,0,0]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=YELLOW).shift(DOWN * 2.5)
        xA = A.get_center()

        tA = Tex(r"$A$"  , font_size=18 , color = YELLOW).move_to(np.array([xA[0],xA[1]+0.4,0]))
        xB = B.get_center()
        tB = Tex(r"$B$"  , font_size=18 , color = YELLOW).move_to(np.array([xB[0],xB[1]+0.4,0]))
        
        ray = Vector(direction=np.array([4*cos(theta.get_value()).real,4*sin(theta.get_value()).real,0])).set_color(color=[BLUE])
        self.play(FadeIn(line1_R,line1_L, A , B , tA,tB))
        self.wait(2)
        txt1 = Text("Let AB be a line segment ", ).set_color(ORANGE).set_height(0.3)
        txt1.to_edge(UP , buff = 2.5)
        txt1.to_edge(LEFT , buff = 0.5)

        self.play(FadeIn(txt1))

        self.wait(3)
        txt2 = Text("And OP be a ray", ).set_color(BLUE).set_height(0.3)
        txt2.to_edge(UP , buff = 2.5)
        txt2.to_edge(RIGHT , buff = 0.5)

        self.play(FadeIn(txt2))       
        
        self.wait(3)
        self.play(FadeIn(ray))
        O = Dot(point=np.array([0, 0, 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=PURPLE)
        P = Dot(point=np.array([3.5*cos(theta.get_value()).real,3.5*sin(theta.get_value()).real,0]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=PURPLE)
        xO = O.get_center()

        tO = Tex(r"$O$"  , font_size=18 , color = PURPLE).move_to(np.array([xO[0],xO[1]-0.4,0]))
        xP = P.get_center()
        tP = Tex(r"$P$"  , font_size=18 , color = PURPLE).move_to(np.array([xP[0],xP[1]+0.4,0]))
        self.play(FadeIn(O,P,tO,tP))
        self.wait(3)
        grpray = VGroup(O,P,tO,tP,ray) 
        self.play(grpray.animate.shift(+DOWN*2.5),run_time =2)
        self.wait(4)
class Concept5_2(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Axiom: If a ray stands on a line, \n then the sum of two adjacent angles so formed is 180°.", font ="Metal" ).set_color(GREEN, PINK).set_height(0.8)
        theta = ValueTracker(PI/4)

        self.add(logo)        
        title.to_edge(UP, buff=1)
        title.to_edge(LEFT, buff=0.6)

        self.add(title)
        
        line1_R = Vector(direction= [4,0,0]).set_color(color=[RED])
        line1_R.shift(DOWN*2.5)
        # line1_R.to_edge(LEFT,buff = 5)

        line1_L = Vector(direction= [-4,0,0]).set_color(color=[RED])
        line1_L.shift(DOWN * 2.5)
        # line1_L.to_edge(LEFT,buff = 5)

        A = Dot(point=np.array([-3.2, 0, 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=YELLOW).shift(DOWN * 2.5)
        B = Dot(point=np.array([3.2,0,0]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=YELLOW).shift(DOWN * 2.5)
        xA = A.get_center()

        tA = Tex(r"$A$"  , font_size=18 , color = YELLOW).move_to(np.array([xA[0],xA[1]+0.4,0]))
        xB = B.get_center()
        tB = Tex(r"$B$"  , font_size=18 , color = YELLOW).move_to(np.array([xB[0],xB[1]+0.4,0]))
        
        ray = always_redraw(lambda : Vector(direction=np.array([4*cos(theta.get_value()).real,4*sin(theta.get_value()).real,0])).set_color(color=[BLUE]).shift(DOWN * 2.5))
        self.add(line1_R,line1_L, A , B , tA,tB)
        txt1 = Text("Let AB be a line segment ", ).set_color(ORANGE).set_height(0.3)
        txt1.to_edge(UP , buff = 2.5)
        txt1.to_edge(LEFT , buff = 0.5)

        self.add(txt1)

        txt2 = Text("And OP be a ray", ).set_color(BLUE).set_height(0.3)
        txt2.to_edge(UP , buff = 2.5)
        txt2.to_edge(RIGHT , buff = 0.5)

        self.add(txt2)
        self.add(ray)
        O = Dot(point=np.array([0, 0, 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=PURPLE).shift(+DOWN*2.5)

        P = always_redraw(lambda : Dot(point=np.array([3.5*cos(theta.get_value()).real,3.5*sin(theta.get_value()).real,0]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=PURPLE).shift(+DOWN*2.5))

        xO = O.get_center()

        tO =  Tex(r"$O$"  , font_size=18 , color = PURPLE).move_to(np.array([xO[0],xO[1]-0.4,0]))

        tP = always_redraw(lambda : Tex(r"$P$"  , font_size=18 , color = PURPLE).move_to(np.array([3.5*cos(theta.get_value()).real,3.5*sin(theta.get_value()).real+0.4,0])).shift(+DOWN*2.5))

        self.add(O,P,tO,tP)
        self.wait(2)
        angle1_1 = always_redraw(lambda :Arc(radius=0.4, start_angle=0, angle=theta.get_value(), num_components=9, arc_center=np.array([0,0,0])).shift(+DOWN*2.5))
        angle1_2 = always_redraw(lambda :Arc(radius=0.5, start_angle=0, angle=theta.get_value(), num_components=9, arc_center=np.array([0,0,0])).shift(+DOWN*2.5))

        angle2 = always_redraw(lambda :Arc(radius=0.8, start_angle=theta.get_value(), angle=PI - theta.get_value(), num_components=9, arc_center=np.array([0,0,0])).shift(+DOWN*2.5))
        self.play(FadeIn(angle1_1,angle1_2,angle2))
        txt2_1 = Tex(r"  $\angle$AOP + $\angle$BOP = 180$^{\circ}$"   , font_size=18 , color = WHITE).shift(UP+RIGHT)
        txt2_1.to_edge(LEFT,buff=0.5)
        txt2_1.to_edge(DOWN,buff=3.3)

        self.play(FadeIn(txt2_1))

        txt3 = Tex(r" $\angle$AOP"   , font_size=18 , color = WHITE).shift([-1.2,-2.2,0])
        txt4 = Tex(r"$\angle$BOP"   , font_size=18 , color = WHITE).shift([1.2,-2.2,0])
        
        txt5 = always_redraw(lambda : Tex(" " + str((round((PI-theta.get_value())*180/PI,2)))+ r"$^{\circ}$ " + r" \  + \  " + str(round((theta.get_value())*180/PI,2)) + r"$^{\circ}$ " + r"\  = \ " + r"  180$^{\circ}$ "   , font_size=19 , color = WHITE).to_edge(LEFT,buff=0.5).to_edge(LEFT,buff=0.5))
        
        self.play(FadeIn(txt3,txt4,txt5))
        self.wait(6)
        self.play(theta.animate.set_value((3*PI/4)-0.12) , run_time = 3)
        self.wait(3)
        self.play(theta.animate.set_value((PI/4)-0.12) , run_time = 3)
        self.remove(txt1,txt2)
        txt6 = Text("As we can see from the above diagram that no matter how we vary the angle of ray OP, \n sum of the adjacent angles is always 180°", ).set_color(ORANGE).set_height(0.5)
        txt6.to_edge(UP , buff = 2.5)
        txt6.to_edge(LEFT , buff = 0.5)
        self.play(FadeIn(txt6))
        self.wait(7)

run5_1 = Concept5_2()
run5_1.construct()