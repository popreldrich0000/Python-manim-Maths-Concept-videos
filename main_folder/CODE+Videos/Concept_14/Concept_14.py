from cmath import cos, sin 
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *





class Concept14_1(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Theorm: If a transversal intersects two parallel lines,\n then each pair of alternate interior angles is equal.", font ="Metal" ,font_size=32).set_color(GREEN, PINK)
            
        title.to_edge(UP, buff=0.5)
        title.to_edge(LEFT, buff=0.6)
        self.play(Write(title))
        self.wait(4)

        txt1 = Text("Let l1 and l2 be two parallel lines" , color='BLUE' ,slant=ITALIC,font_size=18 )
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
        lt = Line(start=np.array([-0.5,-1, 0]),end=np.array([1.25,2.5,0])).set_color(color=[PINK])
        txt5 = Tex(r"$t$"  , font_size=18 , color = PINK).move_to(np.array([-0.3,-1,0])).set_height(0.2)
        self.play(FadeIn(txt4,txt5,lt))


        angle1uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-PI, start_angle= 0, color = GREEN,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*(1.75/3.5),1.5,0]))
        angle3uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-PI, start_angle= 0, color = RED,fill_opacity=0.5, stroke_width=0)
        angle2uf = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -lt.get_angle()+PI, start_angle= lt.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0)

        self.wait(4)

        self.play(FadeIn(angle1uf,angle2uf,angle3uf))


        self.wait(4)
      
        txt19= Tex( " Let's focus on the angles " +r" $\angle$1 " + " , " + r" $\angle$2" + " and " +  r" $\angle$3"   , font_size=28 , color = RED)
        txt19.to_edge(LEFT,buff=1)
        txt19.to_edge(DOWN,buff=1)
        self.remove(txt4,txt1)
        txtangle1= Tex( r" $\angle$1 "    , font_size=28 , color = GREEN).shift(np.array([1.2*(1.2/3.5)+1,1.2,0]))
        txtangle3= Tex( r" $\angle$3 "    , font_size=28 , color = RED).shift(np.array([0.8,-0.7,0]))
        txtangle2= Tex( r" $\angle$2 "    , font_size=28 , color = BLUE).shift(np.array([-0.8,0.7,0]))

        self.play(FadeIn(txt19,txtangle1,txtangle2,txtangle3))


        self.wait(7)

        txtt1= Tex( "To prove" +r" $\angle$1 " + " = " + r" $\angle$2"     , font_size=28 , color = YELLOW)
        txtt1.to_edge(UP,0.8)
        txtt1.to_edge(RIGHT,1)
        txtt2= Tex( "Given = " + r"l1" + " and " + r"l2" + " are parallel"     , font_size=28 , color = BLUE)
        txtt2.to_edge(UP,2)
        txtt2.to_edge(RIGHT,0.5)
        
        self.play(FadeIn(txtt1,txtt2))
        self.wait(7)
        
        txt20 = Text("Using the following Axiom : \n If a transversal intersects two parallel lines, then each pair of corresponding angles is equal" , color='BLUE' ,slant=ITALIC ,font_size=18)
        txt20.to_edge(LEFT,buff=1)
        txt20.to_edge(DOWN,buff=1)
        self.remove(txt19)
        self.play(FadeIn(txt20))
        self.wait(7)

        txt22= Tex( "Here" +r" $\angle$1 " + " and " + r" $\angle$3"  + " are corresponding angles"   , font_size=28 , color = GREEN)
        txt22.to_edge(LEFT,buff=0.2)
        txt22.to_edge(UP,buff=4.5)
        self.play(FadeIn(txt22))

        self.wait(4)

        txt23= Tex( "And so according to the axiom "  + r"$\angle$1" + " = " + r"$\angle$3" , font_size=28 , color = GREEN)
        txt23.to_edge(LEFT,buff=0.2)
        txt23.to_edge(UP,buff=4.5)
        self.remove(txt22)
        self.play(FadeIn(txt23))
        angle1ufd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-PI, start_angle= 0, color = GREEN,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*(1.75/3.5),1.5,0]))
        angle3ufd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-PI, start_angle= 0, color = RED,fill_opacity=0.5, stroke_width=0)       
        self.play(FadeIn(angle1ufd,angle3ufd))
        self.play(angle1ufd.animate.to_edge(UP,buff = 2.8))
        self.play(angle1ufd.animate.to_edge(RIGHT,buff = 2))
        txtangle3d= Tex( r" $\angle$3 "    , font_size=28 , color = RED).to_edge(UP,buff = 3.6).to_edge(RIGHT,buff = 0.8)
        self.play(angle3ufd.animate.to_edge(UP,buff = 2.8))
        self.play(angle3ufd.animate.to_edge(RIGHT,buff = 0.5))
        txtequal= Tex( " = "   , font_size=28 , color = BLUE)
        txtequal.to_edge(RIGHT,buff=1.5)
        txtequal.to_edge(UP,buff=3)
        txtangle1d= Tex( r" $\angle$1 "    , font_size=28 , color = GREEN).to_edge(UP,buff = 3.6).to_edge(RIGHT,buff = 2.3)

        self.play(FadeIn(txtangle1d,txtangle3d))

        self.play(FadeIn(txtequal))
        self.wait(4)

        txt24= Tex( "Now using the following theorm :\n If two lines intersect each other, then the vertically opposite angles are equal." , font_size=28 , color = YELLOW)
        txt24.to_edge(LEFT,buff=1)
        txt24.to_edge(DOWN,buff=1)
        self.remove(txt20)
        self.play(FadeIn(txt24))
        self.wait(7)
    
        txt25= Tex( "Here" +r" $\angle$2 " + " and " + r" $\angle$3"  + " are Vertically Opposite angles"   , font_size=28 , color = BLUE)
        txt25.to_edge(LEFT,buff=0.2)
        txt25.to_edge(UP,buff=4.5)
        self.remove(txt23)
        self.play(FadeIn(txt25))

        self.wait(4)

        txt26= Tex( "And so according to the Theorm " + r"$\angle$2" + " = " + r"$\angle$3" , font_size=28 , color = RED)
        txt26.to_edge(LEFT,buff=0.2)
        txt26.to_edge(UP,buff=4.5)
        self.remove(txt25)
        self.play(FadeIn(txt26))

        self.wait(4)

        angle2ufdd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = -lt.get_angle()+PI, start_angle= lt.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0)
        angle3ufdd = AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()-PI, start_angle= 0, color = RED,fill_opacity=0.5, stroke_width=0)       
        self.play(FadeIn(angle2ufdd,angle3ufdd))
        self.play(angle2ufdd.animate.to_edge(UP,buff = 4.2))
        self.play(angle2ufdd.animate.to_edge(RIGHT,buff = 0.5))
        txtangle3dd = Tex( r" $\angle$3 "    , font_size=28 , color = RED).to_edge(UP,buff = 5).to_edge(RIGHT,buff = 2.3)


        self.play(angle3ufdd.animate.to_edge(UP,buff = 4.2))
        self.play(angle3ufdd.animate.to_edge(RIGHT,buff = 2))

        
        txtequal1= Tex( " = "   , font_size=28 , color = BLUE)
        txtequal1.to_edge(RIGHT,buff=1.5)
        txtequal1.to_edge(UP,buff=4.4)
        txtangle2dd= Tex( r" $\angle$2 "    , font_size=28 , color = BLUE).to_edge(UP,buff = 5).to_edge(RIGHT,buff = 0.8)

        self.play(FadeIn(txtangle2dd,txtangle3dd))

        self.play(FadeIn(txtequal1))
        self.wait(4)

        
        txt27= Tex( "Using simple manipulation the we get the following result." , font_size=28 , color = GREEN)
        txt27.to_edge(LEFT,buff=0.2)
        txt27.to_edge(UP,buff=5.5)
        self.remove(txt25,txt24,txt26)
        self.play(FadeIn(txt27))

        vg1 = VGroup(angle1ufd,angle3ufd,txtangle3d,txtequal,txtangle1d)
        self.play(vg1.animate.to_edge(RIGHT,buff = 2))
        self.play(vg1.animate.to_edge(UP,buff = 4.2))

        self.wait(4)

        self.remove(txtequal,txtangle3dd,txtangle3d,angle3ufd,angle3ufdd)

        vg2 = VGroup(angle1ufd,txtangle1d)
        self.play(vg2.animate.to_edge(RIGHT,buff = 2))

        self.wait(5)

        txt28= Tex( "And so we have concluded " + r"$\angle$1" + " = " + r"$\angle$2" , font_size=28 , color = GREEN)
        txt28.to_edge(LEFT,buff=0.2)
        txt28.to_edge(UP,buff=4.5)
        self.remove(txt27)
        self.play(FadeIn(txt28))
        self.wait(7)

        txt24= Tex( "Theorm used :\n If two lines intersect each other, then the vertically opposite angles are equal." , font_size=28 , color = YELLOW)
        txt24.to_edge(LEFT,buff=1)
        txt24.to_edge(DOWN,buff=1.5)
        self.play(FadeIn(txt24))
        txt20 = Tex("Axiom used : \n If a transversal intersects two parallel lines, then each pair of corresponding angles is equal" ,  font_size=28 , color = PINK)
        txt20.to_edge(LEFT,buff=1)
        txt20.to_edge(DOWN,buff=0.5)
        self.play(FadeIn(txt20))
        self.wait(7)
animation1 = Concept14_1()
animation1.construct()