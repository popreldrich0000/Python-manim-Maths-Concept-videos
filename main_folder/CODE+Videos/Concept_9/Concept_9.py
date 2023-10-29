from cmath import cos, sin, tan 
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *





class Concept_9(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Transversal", font ="Metal" ,font_size=32).set_color(GREEN, PINK)
            
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

        self.wait(4)

        
        lt = Line(start=np.array([-0.5,-1, 0]),end=np.array([1.25,2.5,0])).set_color(color=[PINK])
        txt5 = Tex(r"$t$"  , font_size=18 , color = PINK).move_to(np.array([-0.3,-1,0])).set_height(0.2)
        self.play(FadeIn(lt,txt5))
        self.wait(2)

        txt4 = Text("Here t is the transversal" , color='BLUE' ,slant=ITALIC ,font_size=18)
        txt4.to_edge(RIGHT,buff=5)
        txt4.to_edge(DOWN,buff=2.2)
        self.play(FadeIn(txt4))
        vg1 = VGroup(txt5,txt3,txt2,l1,l2,lt,txt4)
        self.play(vg1.animate.scale(0.7))
        txt5 = Text("A line which intersects two or more lines \n  at distinct points is called a transversal" , color='YELLOW' ,slant=ITALIC ,font_size=18)
        txt5.to_edge(LEFT,buff=1)
        txt5.to_edge(UP,buff=1.3)
        self.play(FadeIn(txt5))
        self.play(vg1.animate.to_edge(RIGHT,buff=0.8).to_edge(UP,buff=1))
        self.wait(4)

        # 
        # 
        l1 = Line(start=np.array([-1, 0.5, 0]),end=np.array([1,0.5,0])).set_color(color=[PINK])
        l2 = Line(start=np.array([-1, -0.8, 0]),end=np.array([1,-0.8,0])).set_color(color=[PINK])
        txt2 = Tex(r"$l1$"  , font_size=18 , color = PINK).next_to(l1).set_height(0.2).scale(0.7)
        txt3 = Tex(r"$l2$"  , font_size=18 , color = PINK).next_to(l2).set_height(0.2).scale(0.7)
        lt = Line(start=np.array([-0.5,-1.2, 0]),end=np.array([0.5,1.2,0])).set_color(color=[PINK])
        txt5 = Tex(r"$t$"  , font_size=18 , color = PINK).next_to(lt).set_height(0.2)
        self.play(FadeIn(lt,txt5))
        txt4 = Text("Here t is the transversal" , color='BLUE' ,slant=ITALIC ,font_size=18).scale(0.7)
        txt4.to_edge(RIGHT,buff=5)
        txt4.to_edge(DOWN,buff=2.2)
        self.play(FadeIn(l1,l2))
        self.play(FadeIn(txt2,txt3))
        self.play(FadeIn(txt4))
        self.wait(4)
        

        vg2 = VGroup(txt5,txt3,txt2,l1,l2,lt,txt4)
        self.play(vg2.animate.to_edge(RIGHT,buff=0.8).to_edge(DOWN,buff=0.5))
        self.wait(2)

# 


        l1 = Line(start=np.array([-0.9, 0.9, 0]),end=np.array([0.9,-0.9,0])).set_color(color=[PINK])
        l2 = Line(start=np.array([-0.9, -0.9, 0]),end=np.array([0.9,0.9,0])).set_color(color=[PINK])
        txt2 = Tex(r"$l1$"  , font_size=18 , color = PINK).shift(np.array([-1.2,1.2,0])).set_height(0.2).scale(0.7)
        txt3 = Tex(r"$l2$"  , font_size=18 , color = PINK).shift(np.array([-1.2,-1.2,0])).set_height(0.2).scale(0.7)
        lt = Line(start=np.array([-0.8,-0.2, 0]),end=np.array([0.8,0.2,0])).set_color(color=[PINK])
        txt5 = Tex(r"$t$"  , font_size=18 , color = PINK).next_to(lt).set_height(0.2).scale(0.7)
        self.play(FadeIn(lt,txt5))
        txt4 = Text("Here t is not the transversal as it does not \n intersects at two DISTINCT points" , color='BLUE' ,slant=ITALIC ,font_size=18).scale(0.7)
        txt4.to_edge(RIGHT,buff=5)
        txt4.to_edge(DOWN,buff=2.2)
        self.play(FadeIn(l1,l2))
        self.play(FadeIn(txt2,txt3))
        self.play(FadeIn(txt4))
        self.wait(4)
        

        vg2 = VGroup(txt5,txt3,txt2,l1,l2,lt,txt4)
        self.play(vg2.animate.to_edge(LEFT,buff=1.4))
        self.wait(2)

        # 
        # 


        l1 = Line(start=np.array([-0.9, 0.9, 0]),end=np.array([0.9,0.0,0])).set_color(color=[PINK])
        l2 = Line(start=np.array([-0.9, -0.9, 0]),end=np.array([0.9,0.9,0])).set_color(color=[PINK])
        txt2 = Tex(r"$l1$"  , font_size=18 , color = PINK).shift(np.array([-1.2,1.2,0])).set_height(0.2).scale(0.7)
        txt3 = Tex(r"$l2$"  , font_size=18 , color = PINK).shift(np.array([-1.2,-1.2,0])).set_height(0.2).scale(0.7)
        lt = Line(start=np.array([-0.8,-0.2, 0]),end=np.array([0.8,0.2,0])).set_color(color=[PINK])
        txt5 = Tex(r"$t$"  , font_size=18 , color = PINK).next_to(lt).set_height(0.2).scale(0.7)
        self.play(FadeIn(lt,txt5))
        txt4 = Text("Here t is the transversal" , color='BLUE' ,slant=ITALIC ,font_size=18).scale(0.7)
        txt4.to_edge(RIGHT,buff=5)
        txt4.to_edge(DOWN,buff=2.2)
        self.play(FadeIn(l1,l2))
        self.play(FadeIn(txt2,txt3))
        self.play(FadeIn(txt4))
        self.wait(4)
        

        # vg2 = VGroup(txt5,txt3,txt2,l1,l2,lt,txt4)
        # self.play(vg2.animate.to_edge(LEFT,buff=1.4))
animation1 = Concept_9()
animation1.construct()