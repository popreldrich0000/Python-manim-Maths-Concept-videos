from cmath import cos, sin 
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *





class Concept15_1(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Theorem: If a transversal intersects two lines such that a pair of \n alternate interior angles is equal, then the two lines are parallel.", font ="Metal" ,font_size=32).set_color(GREEN, PINK)
            
        title.to_edge(UP, buff=0.5)
        title.to_edge(LEFT, buff=0.6)
        self.play(Write(title))
        self.wait(4)

        txt1 = Tex( "Let " + r"$l1$" + " and " + r"$l2$" +" be two lines." , font_size=28 , color = YELLOW)
        txt1.to_edge(LEFT,buff=1)
        txt1.to_edge(DOWN,buff=0.5)
        l1 = Line(start=np.array([-1.5, 1.5, 0]),end=np.array([1.5,1.5,0])).set_color(color=[PINK])
        l2 = Line(start=np.array([-1.5, 0.0, 0]),end=np.array([1.5,0,0])).set_color(color=[PINK])
        txt2 = Tex(r"$l1$"  , font_size=18 , color = PINK).move_to(np.array([-1.7,1.5,0])).set_height(0.2)
        txt3 = Tex(r"$l2$"  , font_size=18 , color = PINK).move_to(np.array([-1.7,0,0])).set_height(0.2)
        self.play(FadeIn(txt1))
        self.play(FadeIn(l1,l2))
        self.play(FadeIn(txt2,txt3))
        self.wait(7)
        txt4 = Text("Let t be the transversal" , color='BLUE' ,slant=ITALIC ,font_size=18)
        txt4.to_edge(RIGHT,buff=1)
        txt4.to_edge(DOWN,buff=0.5)
        self.play(FadeIn(txt4))
        lt = Line(start=np.array([-0.5,-1, 0]),end=np.array([1.25,2.5,0])).set_color(color=[PINK])
        txt5 = Tex(r"$t$"  , font_size=18 , color = PINK).move_to(np.array([-0.3,-1,0])).set_height(0.2)
        self.play(FadeIn(lt,txt5))
        self.wait(4)
        angle1uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-PI, start_angle= 0, color = GREEN,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*(1.75/3.5),1.5,0]))
        angle3uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-PI, start_angle= 0, color = RED,fill_opacity=0.5, stroke_width=0)
        angle2uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -lt.get_angle()+PI, start_angle= lt.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0)
        self.play(FadeIn(angle1uf,angle2uf,angle3uf))
        self.wait(2)
        txt191= Tex( " Let's focus on the angles " +r" $\angle$1 " + " , " + r" $\angle$2" + " and " +  r" $\angle$3"   , font_size=28 , color = RED)
        txt191.to_edge(LEFT,buff=1)
        txt191.to_edge(DOWN,buff=1)
        self.remove(txt4,txt1)
        txtangle1= Tex( r" $\angle$1 "    , font_size=28 , color = GREEN).shift(np.array([1.2*(1.2/3.5)+1,1.2,0]))
        txtangle3= Tex( r" $\angle$3 "    , font_size=28 , color = RED).shift(np.array([0.8,-0.7,0]))
        txtangle2= Tex( r" $\angle$2 "    , font_size=28 , color = BLUE).shift(np.array([-0.8,0.7,0]))

        self.play(FadeIn(txt191,txtangle1,txtangle2,txtangle3))

        self.wait(3)

        txtt1= Tex( "Given" +r" $\angle$1 " + " = " + r" $\angle$2"     , font_size=28 , color = RED)
        txtt1.to_edge(UP,2.5)
        txtt1.to_edge(RIGHT,1)
        txtt2= Tex( "To prove = " + r"$l1$" + " and " + r"$l2$" +  " are parallel"     , font_size=28 , color = YELLOW)
        txtt2.to_edge(UP,1.7)
        txtt2.to_edge(RIGHT,1)
        self.play(FadeIn(txtt1))
        self.play(FadeIn(txtt2))

        self.wait(7)
        
        self.remove(txt191)


        txt24= Tex( "Now using the following theorm :\n If two lines intersect each other, then the vertically opposite angles are equal." , font_size=28 , color = GREEN)
        txt24.to_edge(LEFT,buff=1)
        txt24.to_edge(DOWN,buff=1)
        self.play(FadeIn(txt24))
        self.wait(5)

        txt251= Tex( "Here" +r" $\angle$2 " + " and " + r" $\angle$3"  + " are Vertically Opposite angles"   , font_size=28 , color = YELLOW)
        txt251.to_edge(LEFT,buff=0.2)
        txt251.to_edge(UP,buff=4.5)
        self.play(FadeIn(txt251))
        self.wait(4)
        txt26= Tex( "And so according to the Theorm " + r"$\angle$2" + " = " + r"$\angle$3" , font_size=28 , color = PINK)
        txt26.to_edge(LEFT,buff=0.2)
        txt26.to_edge(UP,buff=4.5)
        self.remove(txt251)
        self.play(FadeIn(txt26))

        self.wait(4)

        angle2ufdd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -lt.get_angle()+PI, start_angle= lt.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0)
        angle3ufdd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-PI, start_angle= 0, color = RED,fill_opacity=0.5, stroke_width=0)       
        self.play(FadeIn(angle2ufdd,angle3ufdd))
        self.play(angle3ufdd.animate.to_edge(UP,buff = 5))
        self.play(angle3ufdd.animate.to_edge(RIGHT,buff = 0.5))
        txtangle3dd = Tex( r" $\angle$3 "    , font_size=28 , color = RED).to_edge(UP,buff = 5.8).to_edge(RIGHT,buff = 0.8)


        self.play(angle2ufdd.animate.to_edge(UP,buff = 5))
        self.play(angle2ufdd.animate.to_edge(RIGHT,buff = 2))

        
        txtequal1= Tex( " = "   , font_size=28 , color = BLUE)
        txtequal1.to_edge(RIGHT,buff=1.5)
        txtequal1.to_edge(UP,buff=5.2)
        txtangle2d= Tex( r" $\angle$2 "    , font_size=28 , color = BLUE).to_edge(UP,buff = 5.8).to_edge(RIGHT,buff = 2.3)

        self.play(FadeIn(txtangle2d,txtangle3dd))

        self.play(FadeIn(txtequal1))

        self.wait(4)
        txt252= Tex( "Here  " +r" $\angle$1 " + " and " + r" $\angle$2"  + " are Alternate interior angles"   , font_size=28 , color = GREEN)
        txt252.to_edge(LEFT,buff=1)
        txt252.to_edge(DOWN,buff=1)
        self.remove(txt24,txt26)
        self.play(FadeIn(txt252))
        
        self.wait(5)
       


        txt223= Tex( "Here it is given to us that \n " +r" $\angle$1 " + " = " + r" $\angle$2"     , font_size=28 , color = YELLOW)
        txt223.to_edge(LEFT,buff=0.2)
        txt223.to_edge(UP,buff=4.5)
        self.play(FadeIn(txt223))

        self.wait(3)
            

        angleu1fdd2 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-PI, start_angle= 0, color = GREEN,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*(1.75/3.5),1.5,0]))
        angleu2fdd2 = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -lt.get_angle()+PI, start_angle= lt.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0)       
        self.play(FadeIn(angleu1fdd2,angleu2fdd2))
        self.play(angleu2fdd2.animate.to_edge(UP,buff = 3.3))
        self.play(angleu2fdd2.animate.to_edge(RIGHT,buff = 0.5))
        txtangle1dd = Tex( r" $\angle$1 "    , font_size=28 , color = GREEN).to_edge(UP,buff = 4.1).to_edge(RIGHT,buff = 2.3)




        self.play(angleu1fdd2.animate.to_edge(UP,buff = 3.3))
        self.play(angleu1fdd2.animate.to_edge(RIGHT,buff = 2))
        
        txtequal= Tex( " = "   , font_size=28 , color = BLUE)
        txtequal.to_edge(RIGHT,buff=1.5)
        txtequal.to_edge(UP,buff=3.7)
        txtangle2dd= Tex( r" $\angle$2 "    , font_size=28 , color = BLUE).to_edge(UP,buff = 4.1).to_edge(RIGHT,buff = 0.8)

        self.play(FadeIn(txtangle2dd,txtangle1dd,))

        self.play(FadeIn(txtequal))

        self.wait(4)
    

        vg1 = VGroup(angleu1fdd2,angleu2fdd2,txtequal,txtangle2dd,txtangle1dd)

        self.play(vg1.animate.to_edge(RIGHT,buff=2))
        self.play(vg1.animate.to_edge(UP,buff=5))
        self.wait(4)


        self.remove(angle2ufdd,txtequal,txtangle2dd,angleu2fdd2,txtangle2d)

        self.wait(1)
        
        vg2 = VGroup(angleu1fdd2,txtangle1dd)
        self.play(vg2.animate.to_edge(RIGHT,buff=2))
        self.wait(4)
        txt28= Tex( "Using simple manipulation we get the following result." , font_size=28 , color = WHITE)

        txt28.to_edge(LEFT,buff=0.2)
        txt28.to_edge(UP,buff=5.5)
        self.remove(txt223,txt252)
        self.play(FadeIn(txt28))

       

        txt30= Tex( r" $\angle$1 " + " = " + r" $\angle$3"     , font_size=28 , color = PINK)
        txt30.to_edge(LEFT,buff=0.2)
        txt30.to_edge(DOWN,buff=1)
        self.play(FadeIn(txt30))
       
        self.wait(5)
        # txt282= Tex( "Here " +r" $\angle$1 " + " and " + r" $\angle$3"  + " are corresponding angles"   , font_size=28 , color = GREEN)
        # txt282.to_edge(LEFT,buff=0.2)
        # txt282.to_edge(UP,buff=5.2)
        self.remove(txt28)
        # self.play(FadeIn(txt282))
        self.wait(4)
        self.play(txt30.animate.shift(UP*3))

        txt201 = Text("According to the following Axiom : If a transversal intersects two lines such that a pair of \n corresponding angles is equal, then the two lines are parallel to each other." , color='RED' ,slant=ITALIC ,font_size=18)
        txt201.to_edge(LEFT,buff=0.2)
        txt201.to_edge(DOWN,buff=1)
        self.play(FadeIn(txt201))

        txt20 = Tex("Here the corresponding angles " + r"\\"  + r" $\angle$1 " + " and " + r" $\angle$3 " + " are equal.", color=RED,font_size=28)
        txt20.to_edge(LEFT,buff=0.2)
        txt20.to_edge(DOWN ,buff=5)
        self.play(FadeIn(txt20))


        txt23= Tex( "And so according to the axiom " + r"$l1$" + " and " + r"$l2$" +" are parallel" , font_size=28 , color = YELLOW)
        txt23.to_edge(LEFT,buff=0.2)
        txt23.to_edge(UP,buff=5.2)
        self.play(FadeIn(txt23)) 
        self.wait(5)
        vg3 =  VGroup(angleu1fdd2,txtangle1dd,txtangle3dd,angle3ufdd,txtequal1)
        self.play(vg3.animate.shift(UP*1))
        self.remove(txt201)
        self.wait(2)

        txt24= Tex( "Theorm used :\n If two lines intersect each other, then the vertically opposite angles are equal." , font_size=28 , color = GREEN)
        txt24.to_edge(LEFT,buff=1)
        txt24.to_edge(DOWN,buff=1.5)
        self.play(FadeIn(txt24))
        txt20 = Tex("Axiom used: If a transversal intersects two lines such that a pair of \n corresponding angles is equal, then the two lines are parallel to each other." , font_size=28 , color = YELLOW)
        txt20.to_edge(LEFT,buff=1)
        txt20.to_edge(DOWN,buff=0.5)
        self.play(FadeIn(txt20))
        self.wait(5)


animation1 = Concept15_1()
animation1.construct()