from cmath import cos, sin 
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *

class Concept6_1(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Axiom : If the sum of two adjacent angles is 180°, \n then the non-common arms of the angles forms a line", font ="Metal" ).set_color(GREEN, PINK).set_height(1)
        title.to_edge(UP, buff=1)
        title.to_edge(LEFT, buff=3)
        self.play(Write(title))
        self.wait(4)
        txt1 = Text("Let's draw Adjacent angles of different measures ", ).set_color(ORANGE).set_height(0.3)
        txt1.to_edge(DOWN,  buff = 0.5)
        txt1.to_edge(LEFT,  buff = 2)
        self.play(FadeIn(txt1))
        self.wait(4)


        line1_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[RED])
        line1_1.shift(LEFT*5.5)
        line1_2 = Vector(direction= [1,1,0]).set_color(color=[RED])
        line1_2.shift(LEFT*5.5)
        line1_3 = Vector(direction= [-1,1,0]).set_color(color=[RED])
        line1_3.shift(LEFT*5.5)
        angle11 = Arc(radius=0.4, start_angle=0, angle=line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)
        angle12 = Arc(radius=0.5, start_angle=0, angle=line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)
        angle1_2 = Arc(radius=0.8, start_angle=line1_2.get_angle(), angle=line1_3.get_angle()-line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)

       
# 
        self.play(Create(line1_1), run_time = 0.5)
        self.play(Create(line1_2), run_time = 0.5)
        self.play(Create(line1_3), run_time = 0.5)
        self.play(Create(angle11), run_time = 0.5)
        self.play(Create(angle12), run_time = 0.5)
        self.play(Create(angle1_2), run_time = 0.5)

        self.wait(2)

        line2_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[GREEN])
        line2_1.shift(RIGHT*5.5)
        line2_2 = Vector(direction= [-1,1,0]).set_color(color=[GREEN])
        line2_2.shift(RIGHT*5.5)
        line2_3 = Vector(direction= [-1,-1,0]).set_color(color=[GREEN])
        line2_3.shift(RIGHT*5.5)
        angle21 = Arc(radius=0.4, start_angle=0, angle=line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
        angle22 = Arc(radius=0.5, start_angle=0, angle=line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
        angle2_2 = Arc(radius=0.8, start_angle=line2_2.get_angle(), angle=2*PI+line2_3.get_angle()-line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
# 
        # 
        self.play(Create(line2_1), run_time = 0.5)
        self.play(Create(line2_2), run_time = 0.5)
        self.play(Create(line2_3), run_time = 0.5)
# 
        self.play(Create(angle21), run_time = 0.5)
        self.play(Create(angle22), run_time = 0.5)
        self.play(Create(angle2_2), run_time = 0.5)

        self.wait(2)


        line3_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[BLUE])
        line3_2 = Vector(direction= [-1,1,0]).set_color(color=[BLUE])
        line3_3 = Vector(direction= [1,-1,0]).set_color(color=[BLUE])
        angle31 = Arc(radius=0.4, start_angle=0, angle=line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
        angle32 = Arc(radius=0.5, start_angle=0, angle=line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
        angle3_2 = Arc(radius=0.8, start_angle=line3_2.get_angle(), angle=2*PI+line3_3.get_angle()-line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
# 
# 
# 
        self.play(Create(line3_1), run_time = 0.5)
        self.play(Create(line3_2), run_time = 0.5)
        self.play(Create(line3_3), run_time = 0.5)
        self.play(Create(angle31), run_time = 0.5)
        self.play(Create(angle32), run_time = 0.5)
        self.play(Create(angle3_2), run_time = 0.5)

        self.wait(4)


class Concept6_2(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Axiom : If the sum of two adjacent angles is 180°, \n then the non-common arms of the angles forms a line", font ="Metal" ).set_color(GREEN, PINK).set_height(1)
        title.to_edge(UP, buff=1)
        title.to_edge(LEFT, buff=3)
        self.add(title)        
        txt1 = Text("Let's draw Adjacent angles of different measures ", ).set_color(ORANGE).set_height(0.3)
        txt1.to_edge(DOWN,  buff = 0.5)
        txt1.to_edge(LEFT,  buff = 2)
        self.add(txt1)


        line1_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[RED])
        line1_1.shift(LEFT*5.5)
        line1_2 = Vector(direction= [1,1,0]).set_color(color=[RED])
        line1_2.shift(LEFT*5.5)
        line1_3 = Vector(direction= [-1,1,0]).set_color(color=[RED])
        line1_3.shift(LEFT*5.5)
        angle11 = Arc(radius=0.4, start_angle=0, angle=line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)
        angle12 = Arc(radius=0.5, start_angle=0, angle=line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)
        angle1_2 = Arc(radius=0.8, start_angle=line1_2.get_angle(), angle=line1_3.get_angle()-line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)

       
# 
        self.add(line1_1)
        self.add(line1_2)
        self.add(line1_3)
        self.add(angle11)
        self.add(angle12)
        self.add(angle1_2)


        line2_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[GREEN])
        line2_1.shift(RIGHT*5.5)
        line2_2 = Vector(direction= [-1,1,0]).set_color(color=[GREEN])
        line2_2.shift(RIGHT*5.5)
        line2_3 = Vector(direction= [-1,-1,0]).set_color(color=[GREEN])
        line2_3.shift(RIGHT*5.5)
        angle21 = Arc(radius=0.4, start_angle=0, angle=line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
        angle22 = Arc(radius=0.5, start_angle=0, angle=line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
        angle2_2 = Arc(radius=0.8, start_angle=line2_2.get_angle(), angle=2*PI+line2_3.get_angle()-line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
# 
        # 
        self.add(line2_1)
        self.add(line2_2)
        self.add(line2_3)
        self.add(angle21)
        self.add(angle22)
        self.add(angle2_2)



        line3_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[BLUE])
        line3_2 = Vector(direction= [-1,1,0]).set_color(color=[BLUE])
        line3_3 = Vector(direction= [1,-1,0]).set_color(color=[BLUE])
        angle31 = Arc(radius=0.4, start_angle=0, angle=line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
        angle32 = Arc(radius=0.5, start_angle=0, angle=line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
        angle3_2 = Arc(radius=0.8, start_angle=line3_2.get_angle(), angle=2*PI+line3_3.get_angle()-line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
# 
# 
# 
        self.add(line3_1)
        self.add(line3_2)
        self.add(line3_3)
        self.add(angle31)
        self.add(angle32)
        self.add(angle3_2)

        self.wait(5)           
        self.remove(txt1)                     
        txt3 = Text("Let's start by changing the angle and observing the total sum of the adjacent \n angles in the examples.  ", font_size=22).set_color(ORANGE)
        txt3.to_edge(DOWN,  buff = 0.5)
        txt3.to_edge(LEFT,  buff = 0.5)
        self.play(FadeIn(txt3))

        theta = ValueTracker(PI/4)
        line1_3v = always_redraw(lambda : Vector(direction= [-1.41*cos(theta.get_value()).real,1.41*sin(theta.get_value()).real,0]).set_color(color=[RED]).shift(LEFT*5.5))
        angle1_2v = always_redraw(lambda : Arc(radius=0.8, start_angle=line1_2.get_angle(), angle=PI-theta.get_value()-line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5))
        

        self.play(FadeIn(line1_3v,angle1_2v))
        self.remove(line1_3,angle1_2)

        thetatxt = Tex(r" $\theta$ "   , font_size=22 , color = WHITE).to_edge(LEFT,buff=1.7)
        thetatxt.to_edge(UP,buff=2.8)
        self.play(FadeIn(thetatxt))
        phitxt = Tex(r" $\phi$ "   , font_size=22 , color = WHITE).to_edge(LEFT,buff=2.5)
        phitxt.to_edge(UP,buff=3.5)
        self.play(FadeIn(phitxt))

        txt2 = always_redraw(lambda : Tex(" " + r" $\theta$ \ + \ $\phi$ \ = \ "  + str((round((PI - theta.get_value() )*180/PI,2))) + r" $^{\circ}$ "   , font_size=22 , color = WHITE).to_edge(LEFT,buff=0.5).to_edge(DOWN,buff=2))

        self.play(FadeIn(txt2))
        
        txt6 = always_redraw(lambda : Tex(r" $\theta$=" + str((round((PI - theta.get_value() - line1_2.get_angle() )*180/PI,2))) + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(LEFT,buff=0.5).to_edge(DOWN,buff=1.5))
        
        txt7 = always_redraw(lambda : Tex(r" $\phi$=" + "45.0" + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(LEFT,buff=2).to_edge(DOWN,buff=1.5))

        self.play(FadeIn(txt6,txt7))



        self.play(theta.animate.set_value((0)) , run_time = 5)
        
        self.wait(4)

        # txt4 = Text("We see that when the total sum of Adjacent angles becomes 180° then the two non-commom arms become straight and forms a line.", ).set_color(ORANGE).set_height(0.3)
        # txt4.to_edge(DOWN,  buff = 0.5)
        # txt4.to_edge(LEFT,  buff = 2)
        # self.play(FadeIn(txt4))

        # txt5 = Text("Hence we have verified the axiom using above examples. ", ).set_color(ORANGE).set_height(0.3)
        # txt5.to_edge(DOWN,  buff = 0.5)
        # txt5.to_edge(LEFT,  buff = 2)
        # self.play(FadeIn(txt5))
class Concept6_3(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Axiom : If the sum of two adjacent angles is 180°, \n then the non-common arms of the angles forms a line", font ="Metal" ).set_color(GREEN, PINK).set_height(1)
        title.to_edge(UP, buff=1)
        title.to_edge(LEFT, buff=3)
        self.add(title)        


        line1_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[RED])
        line1_1.shift(LEFT*5.5)
        line1_2 = Vector(direction= [1,1,0]).set_color(color=[RED])
        line1_2.shift(LEFT*5.5)
        line1_3 = Vector(direction= [-1*1.41,0,0]).set_color(color=[RED])
        line1_3.shift(LEFT*5.5)
        angle11 = Arc(radius=0.4, start_angle=0, angle=line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)
        angle12 = Arc(radius=0.5, start_angle=0, angle=line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)
        angle1_2 = Arc(radius=0.8, start_angle=line1_2.get_angle(), angle=line1_3.get_angle()-line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)

       
# 
        self.add(line1_1)
        self.add(line1_2)
        self.add(line1_3)
        self.add(angle11)
        self.add(angle12)
        self.add(angle1_2)


        line2_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[GREEN])
        line2_1.shift(RIGHT*5.5)
        line2_2 = Vector(direction= [-1,1,0]).set_color(color=[GREEN])
        line2_2.shift(RIGHT*5.5)
        line2_3 = Vector(direction= [-1,-1,0]).set_color(color=[GREEN])
        line2_3.shift(RIGHT*5.5)
        angle21 = Arc(radius=0.4, start_angle=0, angle=line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
        angle22 = Arc(radius=0.5, start_angle=0, angle=line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
        angle2_2 = Arc(radius=0.8, start_angle=line2_2.get_angle(), angle=2*PI+line2_3.get_angle()-line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
# 
        # 
        self.add(line2_1)
        self.add(line2_2)
        self.add(line2_3)
        self.add(angle21)
        self.add(angle22)
        self.add(angle2_2)



        line3_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[BLUE])
        line3_2 = Vector(direction= [-1,1,0]).set_color(color=[BLUE])
        line3_3 = Vector(direction= [1,-1,0]).set_color(color=[BLUE])
        angle31 = Arc(radius=0.4, start_angle=0, angle=line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
        angle32 = Arc(radius=0.5, start_angle=0, angle=line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
        angle3_2 = Arc(radius=0.8, start_angle=line3_2.get_angle(), angle=2*PI+line3_3.get_angle()-line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
# 
# 
# 
        self.add(line3_1)
        self.add(line3_2)
        self.add(line3_3)
        self.add(angle31)
        self.add(angle32)
        self.add(angle3_2)
        phitxt = Tex(r" $\phi$ "   , font_size=22 , color = WHITE).to_edge(LEFT,buff=2.5)
        phitxt.to_edge(UP,buff=3.5)
        self.add(phitxt)
        thetatxt = Tex(r" $\theta$ "   , font_size=22 , color = WHITE).to_edge(LEFT,buff=1.7)
        thetatxt.to_edge(UP,buff=2.8)
        self.add(thetatxt)
        txt3 = Text("Let's start by changing the angle and observing the total sum of the adjacent \n angles in the examples.  ", font_size=22).set_color(ORANGE)
        txt3.to_edge(DOWN,  buff = 0.5)
        txt3.to_edge(LEFT,  buff = 0.5)
        self.add(txt3)
        txt2 = Tex(" " + r" $\theta$ \ + \ $\phi$ \ = \ "  + "180.0"+ r" $^{\circ}$ "   , font_size=22 , color = WHITE).to_edge(LEFT,buff=0.5).to_edge(DOWN,buff=2)
        
        
        self.add(txt2)
        txt6 = Tex(r" $\theta$=" + "135.0" + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(LEFT,buff=0.5).to_edge(DOWN,buff=1.5)

        
        txt7 = Tex(r" $\phi$=" + "45.0" + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(LEFT,buff=2).to_edge(DOWN,buff=1.5)
        self.add(txt6,txt7)
        self.wait(5)           



        theta = ValueTracker(PI/4)
        line2_3v = always_redraw(lambda : Vector(direction= [-1.41*cos(theta.get_value()).real,-1.41*sin(theta.get_value()).real,0]).set_color(color=[GREEN]).shift(RIGHT*5.5))
        angle2_2v = always_redraw(lambda : Arc(radius=0.8, start_angle=line2_2.get_angle(), angle=PI+theta.get_value()-line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5))
        

        self.play(FadeIn(line2_3v,angle2_2v))
        self.remove(line2_3,angle2_2)

        thetatxt = Tex(r" $\theta$ "   , font_size=22 , color = WHITE).to_edge(RIGHT,buff=1.7)
        thetatxt.to_edge(UP,buff=2.8)
        self.play(FadeIn(thetatxt))
        phitxt = Tex(r" $\phi$ "   , font_size=22 , color = WHITE).to_edge(RIGHT,buff=2.5)
        phitxt.to_edge(UP,buff=3.5)
        self.play(FadeIn(phitxt))

        txt2v = always_redraw(lambda : Tex(" " + r" $\theta$ \ + \ $\phi$ \ = \ "  + str((round((PI + theta.get_value() )*180/PI,2))) + r" $^{\circ}$ "   , font_size=22 , color = WHITE).to_edge(LEFT,buff=11.5).to_edge(DOWN,buff=2))

        self.play(FadeIn(txt2v))
        
        txt6 = always_redraw(lambda : Tex(r" $\phi$=" + str((round((PI/4 + theta.get_value()  )*180/PI,2))) + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(LEFT,buff=13).to_edge(DOWN,buff=1.5))
        
        txt7 = always_redraw(lambda : Tex(r" $\theta$=" + "135.0" + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(RIGHT,buff=2).to_edge(DOWN,buff=1.5))

        self.play(FadeIn(txt6,txt7))



        self.play(theta.animate.set_value((0)) , run_time = 5)
        
        self.wait(7)

        
        # theta = ValueTracker(3*PI/4)
        # line2_3v = always_redraw(lambda : Vector(direction= [1.41*cos(theta.get_value()).real,-1.41*sin(theta.get_value()).real,0]).set_color(color=[RED]).shift(LEFT*5.5))
        # self.play(FadeIn(line2_3v))
        # self.remove(line2_3)



        
        
        




        # self.play(theta.animate.set_value((PI)) , run_time = 5)

class Concept6_4(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Axiom : If the sum of two adjacent angles is 180°, \n then the non-common arms of the angles forms a line", font ="Metal" ).set_color(GREEN, PINK).set_height(1)
        title.to_edge(UP, buff=1)
        title.to_edge(LEFT, buff=3)
        self.add(title)        


        line1_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[RED])
        line1_1.shift(LEFT*5.5)
        line1_2 = Vector(direction= [1,1,0]).set_color(color=[RED])
        line1_2.shift(LEFT*5.5)
        line1_3 = Vector(direction= [-1*1.41,0,0]).set_color(color=[RED])
        line1_3.shift(LEFT*5.5)
        angle11 = Arc(radius=0.4, start_angle=0, angle=line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)
        angle12 = Arc(radius=0.5, start_angle=0, angle=line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)
        angle1_2 = Arc(radius=0.8, start_angle=line1_2.get_angle(), angle=line1_3.get_angle()-line1_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(LEFT*5.5)

       
# 
        self.add(line1_1)
        self.add(line1_2)
        self.add(line1_3)
        self.add(angle11)
        self.add(angle12)
        self.add(angle1_2)


        line2_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[GREEN])
        line2_1.shift(RIGHT*5.5)
        line2_2 = Vector(direction= [-1,1,0]).set_color(color=[GREEN])
        line2_2.shift(RIGHT*5.5)
        line2_3 = Vector(direction= [-1*1.41,0,0]).set_color(color=[GREEN])
        line2_3.shift(RIGHT*5.5)
        angle21 = Arc(radius=0.4, start_angle=0, angle=line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
        angle22 = Arc(radius=0.5, start_angle=0, angle=line2_2.get_angle(), num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
        angle2_2 = Arc(radius=0.8, start_angle=line2_2.get_angle(), angle=PI/4, num_components=9, arc_center=np.array([0,0,0])).shift(RIGHT*5.5)
# 
        # 
        self.add(line2_1)
        self.add(line2_2)
        self.add(line2_3)
        self.add(angle21)
        self.add(angle22)
        self.add(angle2_2)



        line3_1 = Vector(direction= [1*1.41,0,0]).set_color(color=[BLUE])
        line3_2 = Vector(direction= [-1,1,0]).set_color(color=[BLUE])
        line3_3 = Vector(direction= [1,-1,0]).set_color(color=[BLUE])
        angle31 = Arc(radius=0.4, start_angle=0, angle=line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
        angle32 = Arc(radius=0.5, start_angle=0, angle=line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
        angle3_2 = Arc(radius=0.8, start_angle=line3_2.get_angle(), angle=2*PI+line3_3.get_angle()-line3_2.get_angle(), num_components=9, arc_center=np.array([0,0,0]))
# 
# 
# 
        self.add(line3_1)
        self.add(line3_2)
        self.add(line3_3)
        self.add(angle31)
        self.add(angle32)
        self.add(angle3_2)
        phitxt = Tex(r" $\phi$ "   , font_size=22 , color = WHITE).to_edge(LEFT,buff=2.5)
        phitxt.to_edge(UP,buff=3.5)
        self.add(phitxt)
        thetatxt = Tex(r" $\theta$ "   , font_size=22 , color = WHITE).to_edge(LEFT,buff=1.7)
        thetatxt.to_edge(UP,buff=2.8)
        self.add(thetatxt)
        txt3 = Text("Let's start by changing the angle and observing the total sum of the adjacent \n angles in the examples.  ", font_size=22).set_color(ORANGE)
        txt3.to_edge(DOWN,  buff = 0.5)
        txt3.to_edge(LEFT,  buff = 0.5)
        self.add(txt3)
        txt2 = Tex(" " + r" $\theta$ \ + \ $\phi$ \ = \ "  + "180.0"+ r" $^{\circ}$ "   , font_size=22 , color = WHITE).to_edge(LEFT,buff=0.5).to_edge(DOWN,buff=2)
        
        
        self.add(txt2)
        txt6 = Tex(r" $\theta$=" + "135.0" + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(LEFT,buff=0.5).to_edge(DOWN,buff=1.5)

        
        txt7 = Tex(r" $\phi$=" + "45.0" + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(LEFT,buff=2).to_edge(DOWN,buff=1.5)
        self.add(txt6,txt7)



        


        thetatxt = Tex(r" $\theta$ "   , font_size=22 , color = WHITE).to_edge(RIGHT,buff=1.7)
        thetatxt.to_edge(UP,buff=2.8)
        phitxt = Tex(r" $\phi$ "   , font_size=22 , color = WHITE).to_edge(RIGHT,buff=2.5)
        phitxt.to_edge(UP,buff=3.5)
        self.add(phitxt,thetatxt)

        txt2v = Tex(" " + r" $\theta$ \ + \ $\phi$ \ = \ "  + "180.0" + r" $^{\circ}$ "   , font_size=22 , color = WHITE).to_edge(LEFT,buff=11.5).to_edge(DOWN,buff=2)

        self.add(txt2v)
        
        txt6 = Tex(r" $\phi$=" + "45.0" + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(LEFT,buff=13).to_edge(DOWN,buff=1.5)
        
        txt7 = Tex(r" $\theta$=" + "135.0" + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(RIGHT,buff=2).to_edge(DOWN,buff=1.5)

        self.add(txt6,txt7)
        
        self.wait(4)

        theta = ValueTracker(3*PI/4)
        line3_3v = always_redraw(lambda : Vector(direction= [-1.41*cos(theta.get_value()).real,-1.41*sin(theta.get_value()).real,0]).set_color(color=[BLUE]))
        angle3_2v = always_redraw(lambda : Arc(radius=0.8, start_angle=line3_2.get_angle(), angle=PI/4+theta.get_value(), num_components=9, arc_center=np.array([0,0,0])))
        

        self.play(FadeIn(line3_3v,angle3_2v))
        self.remove(line3_3,angle3_2)

        thetatxt = Tex(r" $\theta$ "   , font_size=22 , color = WHITE).to_edge(RIGHT,buff=6.7).shift(DOWN*0.3)
        thetatxt.to_edge(UP,buff=2.8)
        self.play(FadeIn(thetatxt))
        phitxt = Tex(r" $\phi$ "   , font_size=22 , color = WHITE).shift(LEFT*1.5)
        phitxt.to_edge(UP,buff=3.5)
        self.play(FadeIn(phitxt))

        txt2v = always_redraw(lambda : Tex(" " + r" $\theta$ \ + \ $\phi$ \ = \ "  + str((round((PI + theta.get_value() )*180/PI,2))) + r" $^{\circ}$ "   , font_size=22 , color = WHITE).to_edge(DOWN,buff=2))

        self.play(FadeIn(txt2v))
        
        txt6 = always_redraw(lambda : Tex(r" $\phi$=" + str((round((PI/4 + theta.get_value()  )*180/PI,2))) + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(DOWN,buff=1.5).shift(LEFT*1.5))
        
        txt7 = always_redraw(lambda : Tex(r" $\theta$=" + "135.0" + r" $^{\circ}$"  , font_size=22 , color = WHITE).to_edge(DOWN,buff=1.5))

        self.play(FadeIn(txt6,txt7))



        self.play(theta.animate.set_value((0)) , run_time = 5)
        
        self.wait(7)
        self.remove(txt3)
        txt12 = Text("From the above examples we see that as the sum of the adjacent angles \n approaches 180° the non-commom arm forms a line.   ", font_size=22).set_color(ORANGE)
        txt12.to_edge(DOWN,  buff = 0.5)
        txt12.to_edge(LEFT,  buff = 0.5)
        self.play(FadeIn(txt12))
        self.wait(6)
        self.remove(txt12)
        txt13 = Text("And so from the above examples we can conclude the above axiom as verified.", font_size=22).set_color(ORANGE)
        txt13.to_edge(DOWN,  buff = 0.5)
        txt13.to_edge(LEFT,  buff = 0.5)
        self.play(FadeIn(txt13))
        self.wait(4)
run1 = Concept6_4()
run1.construct()
