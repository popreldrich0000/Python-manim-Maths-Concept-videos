from cmath import cos, sin, tan 
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *





class Concept_10(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Exterior and Interior angles", font ="Metal" ,font_size=32).set_color(GREEN, PINK)
            
        title.to_edge(UP, buff=0.5)
        title.to_edge(LEFT, buff=0.6)
        self.play(Write(title))

        txt1 = Tex( "Let " + r"$l1$" + " and " + r"$l2$" +" be two lines." , font_size=28 , color = YELLOW)
        txt1.to_edge(LEFT,buff=1)
        txt1.to_edge(DOWN,buff=0.5)
        l1 = Line(start=np.array([-1.5, 1.8, 0]),end=np.array([1.5,1.2,0])).set_color(color=[PINK])
        l2 = Line(start=np.array([-1.5, -0.3, 0]),end=np.array([1.5,0.3,0])).set_color(color=[PINK])
        txt2 = Tex(r"$l1$"  , font_size=18 , color = PINK).move_to(np.array([-1.7,1.75,0])).set_height(0.2)
        txt3 = Tex(r"$l2$"  , font_size=18 , color = PINK).move_to(np.array([-1.7,-0.15,0])).set_height(0.2)
        self.play(FadeIn(txt1))
        self.play(FadeIn(l1,l2))
        self.play(FadeIn(txt2,txt3))

        self.wait(2)

        txt4 = Text("Let t be the transversal" , color='BLUE' ,slant=ITALIC ,font_size=18)
        txt4.to_edge(RIGHT,buff=1)
        txt4.to_edge(DOWN,buff=0.5)
        self.play(FadeIn(txt4))
        lt = Line(start=np.array([-0.5,-1, 0]),end=np.array([1.25,2.5,0])).set_color(color=[PINK])
        txt5 = Tex(r"$t$"  , font_size=18 , color = PINK).move_to(np.array([-0.3,-1,0])).set_height(0.2)
        self.play(FadeIn(lt,txt5))
        self.wait(2)

        theta  =  ValueTracker(l1.get_angle())

        angle1uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -lt.get_angle()+PI+l1.get_angle() , start_angle= lt.get_angle(), color = GREEN,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real),1.5*3.5/(3.5-1.75*tan(theta.get_value()).real),0]))
        angle2uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -l1.get_angle()+lt.get_angle(), start_angle= l1.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real),1.5*3.5/(3.5-1.75*tan(theta.get_value()).real),0]))
        angle3uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -(PI-lt.get_angle()+l1.get_angle()), start_angle= l1.get_angle() , color = RED,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real),1.5*3.5/(3.5-1.75*tan(theta.get_value()).real),0]))
        angle4uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-l1.get_angle(), start_angle= PI+l1.get_angle(), color = YELLOW,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real),1.5*3.5/(3.5-1.75*tan(theta.get_value()).real),0]))
        angle5uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = l2.get_angle()+PI-lt.get_angle(), start_angle= lt.get_angle(), color = PINK,fill_opacity=0.5, stroke_width=0)
        angle6uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-l2.get_angle(), start_angle= l2.get_angle(), color = WHITE,fill_opacity=0.5, stroke_width=0)
        angle7uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -(-lt.get_angle()+PI+l2.get_angle()), start_angle=l2.get_angle() , color = PURPLE,fill_opacity=0.5, stroke_width=0)
        angle8uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -(lt.get_angle()-l2.get_angle()), start_angle= lt.get_angle()-PI, color = ORANGE,fill_opacity=0.5, stroke_width=0)

        txtangle1= Tex( r" $\angle$1"     , font_size=28 , color = GREEN).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real) - 0.4,1.5*3.5/(3.5-1.75*tan(theta.get_value()).real) + 0.7 ,0]))
        txtangle2= Tex( r" $\angle$2"     , font_size=28 , color = BLUE).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real) + 0.7,1.5*3.5/(3.5-1.75*tan(theta.get_value()).real) +  0.4,0]))
        txtangle3= Tex( r" $\angle$3"     , font_size=28 , color = RED).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real) + 0.6,1.5*3.5/(3.5-1.75*tan(theta.get_value()).real) - 0.5,0]))
        txtangle4= Tex( r" $\angle$4"     , font_size=28 , color = YELLOW).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real) - 0.8,1.5*3.5/(3.5-1.75*tan(theta.get_value()).real) - 0.3,0]))
        txtangle5= Tex( r" $\angle$5"     , font_size=28 , color = PINK).shift(np.array([-0.7,0.4,0]))
        txtangle6= Tex( r" $\angle$6"     , font_size=28 , color = WHITE).shift(np.array([0.6,0.6,0]))
        txtangle7= Tex( r" $\angle$7"     , font_size=28 , color = PURPLE).shift(np.array([0.4,-0.6,0]))
        txtangle8= Tex( r" $\angle$8"     , font_size=28 , color = ORANGE).shift(np.array([-0.6,-0.6,0]))


        self.play(FadeIn(angle1uf,angle2uf,angle3uf,angle4uf,angle5uf,angle6uf,angle7uf,angle8uf,txtangle1,txtangle2,txtangle3,txtangle4,txtangle5,txtangle6,txtangle7,txtangle8))
        self.wait(4)
        vg1 = VGroup(txt5,txt2,txt3,l1,l2,lt,angle1uf,angle2uf,angle3uf,angle4uf,angle5uf,angle6uf,angle7uf,angle8uf,txtangle1,txtangle2,txtangle3,txtangle4,txtangle5,txtangle6,txtangle7,txtangle8)
        self.play(vg1.animate.to_edge(RIGHT,buff=0.8))

        self.wait(4)
        
       
        angle1ufd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -lt.get_angle()+PI+l1.get_angle() , start_angle= lt.get_angle(), color = GREEN,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real),1.5*3.5/(3.5-1.75*tan(theta.get_value()).real),0]))
        angle2ufd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -l1.get_angle()+lt.get_angle(), start_angle= l1.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real),1.5*3.5/(3.5-1.75*tan(theta.get_value()).real),0]))
        angle3ufd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -(PI-lt.get_angle()+l1.get_angle()), start_angle= l1.get_angle() , color = RED,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real),1.5*3.5/(3.5-1.75*tan(theta.get_value()).real),0]))
        angle4ufd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-l1.get_angle(), start_angle= PI+l1.get_angle(), color = YELLOW,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real),1.5*3.5/(3.5-1.75*tan(theta.get_value()).real),0]))
        angle5ufd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = l2.get_angle()+PI-lt.get_angle(), start_angle= lt.get_angle(), color = PINK,fill_opacity=0.5, stroke_width=0)
        angle6ufd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-l2.get_angle(), start_angle= l2.get_angle(), color = WHITE,fill_opacity=0.5, stroke_width=0)
        angle7ufd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -(-lt.get_angle()+PI+l2.get_angle()), start_angle=l2.get_angle() , color = PURPLE,fill_opacity=0.5, stroke_width=0)
        angle8ufd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -(lt.get_angle()-l2.get_angle()), start_angle= lt.get_angle()-PI, color = ORANGE,fill_opacity=0.5, stroke_width=0)

        txtangle1d= Tex( r" $\angle$1"     , font_size=28 , color = GREEN).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real) - 0.4,1.5*3.5/(3.5-1.75*tan(theta.get_value()).real) + 0.7 ,0]))
        txtangle2d= Tex( r" $\angle$2"     , font_size=28 , color = BLUE).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real) + 0.7,1.5*3.5/(3.5-1.75*tan(theta.get_value()).real) +  0.4,0]))
        txtangle3d= Tex( r" $\angle$3"     , font_size=28 , color = RED).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real) + 0.6,1.5*3.5/(3.5-1.75*tan(theta.get_value()).real) - 0.5,0]))
        txtangle4d= Tex( r" $\angle$4"     , font_size=28 , color = YELLOW).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real) - 0.8,1.5*3.5/(3.5-1.75*tan(theta.get_value()).real) - 0.3,0]))
        txtangle5d= Tex( r" $\angle$5"     , font_size=28 , color = PINK).shift(np.array([-0.7,0.4,0]))
        txtangle6d= Tex( r" $\angle$6"     , font_size=28 , color = WHITE).shift(np.array([0.6,0.6,0]))
        txtangle7d= Tex( r" $\angle$7"     , font_size=28 , color = PURPLE).shift(np.array([0.4,-0.6,0]))
        txtangle8d= Tex( r" $\angle$8"     , font_size=28 , color = ORANGE).shift(np.array([-0.6,-0.6,0]))


        vg2 = VGroup(angle1ufd,angle2ufd,angle3ufd,angle4ufd,angle5ufd,angle6ufd,angle7ufd,angle8ufd,txtangle1d,txtangle2d,txtangle3d,txtangle4d,txtangle5d,txtangle6d,txtangle7d,txtangle8d)
        vg2.to_edge(RIGHT,buff=0.8)
        self.play(FadeIn(vg2))

        txt4 = Text("Exterior angles" , color=YELLOW ,slant=ITALIC ,font_size=18)
        txt4.to_edge(UP, buff=2)
        txt4.to_edge(LEFT, buff=1)
        self.play(FadeIn(txt4))
        txt4 = Text("Angles that are in the area between \n the lines are called interior angles" , color=YELLOW ,slant=ITALIC ,font_size=18)
        txt4.to_edge(UP, buff=2.5)
        txt4.to_edge(LEFT, buff=0.1)
        self.play(FadeIn(txt4))
        self.wait(2)
        
        # self.play(FadeIn(angle1uf,angle2uf,angle3uf,angle4uf,angle5uf,angle6uf,angle7uf,angle8uf,txtangle1,txtangle2,txtangle3,txtangle4,txtangle5,txtangle6,txtangle7,txtangle8))

        self.play(angle1uf.animate.to_edge(UP,buff=3.4).to_edge(LEFT,buff=1),angle2uf.animate.to_edge(UP,buff=4.2).to_edge(LEFT,buff=1),angle7uf.animate.to_edge(UP,buff=5).to_edge(LEFT,buff=1),angle8uf.animate.to_edge(UP,buff=5.8).to_edge(LEFT,buff=1),txtangle1d.animate.to_edge(UP,buff=3.4).to_edge(LEFT,buff=1.8),txtangle2d.animate.to_edge(UP,buff=4.2).to_edge(LEFT,buff=1.8),txtangle7d.animate.to_edge(UP,buff=5).to_edge(LEFT,buff=1.8),txtangle8d.animate.to_edge(UP,buff=5.8).to_edge(LEFT,buff=1.8))
        self.wait(8)

        txt4 = Text("Interior angles" , color=WHITE ,slant=ITALIC ,font_size=18)
        txt4.to_edge(UP, buff=2)
        txt4.to_edge(LEFT, buff=5)
        self.play(FadeIn(txt4))
        txt4 = Text("Angles that are outside the lines \n  are called interior angles" , color=WHITE ,slant=ITALIC ,font_size=18)
        txt4.to_edge(UP, buff=2.5)
        txt4.to_edge(LEFT, buff=5)
        self.play(FadeIn(txt4))
        self.play(angle3uf.animate.to_edge(UP,buff=3.4).to_edge(LEFT,buff=5.2),angle4uf.animate.to_edge(UP,buff=4.2).to_edge(LEFT,buff=5.2),angle5uf.animate.to_edge(UP,buff=5).to_edge(LEFT,buff=5.2),angle6uf.animate.to_edge(UP,buff=5.8).to_edge(LEFT,buff=5.2),txtangle3d.animate.to_edge(UP,buff=3.4).to_edge(LEFT,buff=6),txtangle4d.animate.to_edge(UP,buff=4.2).to_edge(LEFT,buff=6),txtangle5d.animate.to_edge(UP,buff=5).to_edge(LEFT,buff=6),txtangle6d.animate.to_edge(UP,buff=5.8).to_edge(LEFT,buff=6))
        self.wait(8)

animation1 = Concept_10()
animation1.construct()