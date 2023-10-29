from cmath import cos, sin , tan
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *





class Concept13_1(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Axiom: If a transversal intersects two lines such that a pair of  \n corresponding angles is equal, then the two lines are parallel to each other.", font ="Metal" ,font_size=32).set_color(GREEN, PINK)
        title.to_edge(UP, buff=0.5)
        title.to_edge(LEFT, buff=0.6)
        self.play(Write(title))
        self.wait(4)

        txt1 = Text("Let l1 and l2 be two lines" , color='BLUE' ,slant=ITALIC,font_size=18 )
        txt1.to_edge(LEFT,buff=1)
        txt1.to_edge(DOWN,buff=0.5)
        l1 = Line(start=np.array([-1.5, 1.8, 0]),end=np.array([1.5,1.2,0])).set_color(color=[PINK])
        l2 = Line(start=np.array([-1.5, -0.3, 0]),end=np.array([1.5,0.3,0])).set_color(color=[PINK])
        txt2 = Tex(r"$l1$"  , font_size=18 , color = PINK).move_to(np.array([-1.7,1.75,0])).set_height(0.2)
        txt3 = Tex(r"$l2$"  , font_size=18 , color = PINK).move_to(np.array([-1.7,-0.15,0])).set_height(0.2)
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
        
        

        txt19= Tex( " Let's focus on the angles " +r" $\angle$1 " + " and " + r" $\angle$2"     , font_size=28 , color = GREEN)
        txt19.to_edge(RIGHT,buff=1)
        txt19.to_edge(UP,buff=3)
        self.remove(txt4,txt1)
        self.play(FadeIn(txt19))
        self.wait(4)
        theta  =  ValueTracker(l1.get_angle())

        txtangle1= Tex( r" $\angle$1"     , font_size=28 , color = GREEN).shift([1.8,1.8,0])
        txtangle2= Tex( r" $\angle$2"     , font_size=28 , color = GREEN).shift([1.8,-0.4,0])
        lvar1var_1 = always_redraw(lambda : Tex( r" $\angle$1"  + " = " + str(round(((lt.get_angle() - theta.get_value())*180/PI),2)) + "°" , font_size=28 , color = GREEN).to_edge(RIGHT,buff = 0.5).to_edge(UP,buff = 4))
        lvar1var_2 = always_redraw(lambda : Tex( r" $\angle$2"  + " = " + str(round(((lt.get_angle() + theta.get_value())*180/PI),2)) + "°", font_size=28 , color = GREEN).to_edge(RIGHT,buff = 0.5).to_edge(UP,buff = 5))
        lvar1_1 = always_redraw(lambda : Line(start=np.array([0,1.5,0]),end=np.array([1.53*cos(theta.get_value()).real,1.5+1.53*sin(theta.get_value()).real,0])).set_color(color=[PINK]))
        lvar1_2 = always_redraw(lambda : Line(start=np.array([0,1.5,0]),end=np.array([-1.53*cos(theta.get_value()).real,1.5-1.53*sin(theta.get_value()).real,0])).set_color(color=[PINK]))
        lvar2_1 = always_redraw(lambda : Line(start=np.array([0,0,0]),end=np.array([1.53*cos(PI-theta.get_value()).real,1.53*sin(PI-theta.get_value()).real,0])).set_color(color=[PINK]))
        lvar2_2 = always_redraw(lambda : Line(start=np.array([0,0,0]),end=np.array([-1.53*cos(PI-theta.get_value()).real,-1.53*sin(PI-theta.get_value()).real,0])).set_color(color=[PINK]))

        self.play(FadeIn(lvar1_1,lvar1_2,lvar2_1,lvar2_2))

        self.remove(l1,l2)
        angle1uf = always_redraw(lambda : AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle() - theta.get_value(), start_angle= theta.get_value(), color = GREEN,fill_opacity=0.5, stroke_width=0).shift(np.array([1.5*1.75/(3.5-1.75*tan(theta.get_value()).real),1.5*3.5/(3.5-1.75*tan(theta.get_value()).real),0])))
        angle2uf = always_redraw(lambda : AnnularSector(inner_radius=0, outer_radius=0.5, angle = lt.get_angle()+theta.get_value(), start_angle= -theta.get_value(), color = GREEN,fill_opacity=0.5, stroke_width=0).shift(np.array([0,0,0])))

        self.play(FadeIn(angle1uf,angle2uf))
        
        self.play(FadeIn(lvar1var_1,lvar1var_2,txtangle1,txtangle2))
        self.wait(5)

        txt21 = Text("Let's draw two parallel \n lines for reference." , color='YELLOW' ,slant=ITALIC ,font_size=18)
        txt21.to_edge(LEFT,buff=0.5)
        txt21.to_edge(UP,buff=2)
        self.play(FadeIn(txt21))
        pl1 = DashedLine(start=np.array([-2.5, 1.5, 0]),end=np.array([2.5,1.5,0])).set_color(color=[YELLOW])
        pl2 = DashedLine(start=np.array([-2.5, 0, 0]),end=np.array([2.5,0,0])).set_color(color=[YELLOW])
        self.play(FadeIn(pl1,pl2))
        self.wait(7)
        self.remove(txt21)
        txt20 = Text("Let's change the angles of the lines l1 and l2, and observe the change in above angles " , color='BLUE' ,slant=ITALIC ,font_size=18)
        txt20.to_edge(LEFT,buff=0.5)
        txt20.to_edge(DOWN,buff=0.5)
        self.remove(txt19)
        self.play(FadeIn(txt20))
        self.wait(4)
        self.play(theta.animate.set_value(0),run_time = 5)
        self.wait(5)
        txtt3 = Text("We observe that as the two lines approaches to parallelism ,\n the two angles approaches the same value and finally becomes equal when the two lines are parallel." , color='BLUE' ,slant=ITALIC ,font_size=18).to_edge(LEFT,buff=0.1).to_edge(UP,buff=3)
        self.remove(txt20)
        txtt3.to_edge(LEFT,buff=0.5)
        txtt3.to_edge(DOWN,buff=0.5)       
        self.play(FadeIn(txtt3))
        self.wait(6)
        self.play(theta.animate.set_value(-0.79),run_time = 5)
        self.wait(5)
        self.play(theta.animate.set_value(0),run_time = 5)
        self.wait(5) 
        # txt21.to_edge(DOWN,buff=0.5)
        # self.remove(txt20)
        # self.play(FadeIn(txt21))
        # self.wait(5)
        # # txt22 = always_redraw(lambda : Tex(r" $\angle$1 " + " = " +  str(theta.get_value()*180/PI)  , font_size=24 , color = GREEN).to_edge(RIGHT,buff=0.5).to_edge(UP,buff=3))
        # # txt23 = always_redraw(lambda : Tex(r" $\angle$5 " + " = " +  str(theta.get_value()*180/PI)  , font_size=24 , color = GREEN).to_edge(RIGHT,buff=0.5))

        # # angle1uf = always_redraw(lambda : AnnularSector(inner_radius=0, outer_radius=0.5, angle = theta.get_value(), start_angle=0, color = GREEN,fill_opacity=0.5, stroke_width=0).shift(np.array([0.75,1.5,0])))
        # # angle5uf = always_redraw(lambda : AnnularSector(inner_radius=0, outer_radius=0.5, angle = theta.get_value(), start_angle=0, color = GREEN,fill_opacity=0.5, stroke_width=0))
        

        # line1uf = always_redraw(lambda : Line(start=np.array([0.875+1.95*cos(theta.get_value()).real,1.75+1.95*sin(theta.get_value()).real, 0]),end=np.array([1.25,2.5,0])).set_color(color=[PINK]))
        # line2uf = always_redraw(lambda : Line(start=np.array([0.875-1.95*cos(theta.get_value()).real,1.75-1.95*sin(theta.get_value()).real, 0]),end=np.array([1.25,2.5,0])).set_color(color=[PINK]))
        # self.play(FadeIn(line1uf,line2uf))
        # self.remove(angle1,angle5,lt)

        # self.wait(4)
        # self.play(theta.animate.set_value((3*PI/4)))
        # self.wait(4)
        # self.play(theta.animate.set_value((PI/4)))
        # self.wait(2)
class Concept13_2(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Axiom: If a transversal intersects two lines such that a pair of  \n corresponding angles is equal, then the two lines are parallel to each other.", font ="Metal" ,font_size=32).set_color(GREEN, PINK)
        title.to_edge(UP, buff=0.5)
        title.to_edge(LEFT, buff=0.6)
        self.add(title)
        txtfinal = Tex("We can say that the above axiom is the converse of the following axiom:" , font_size=32 , color = RED).to_edge(LEFT,buff=0.1).to_edge(UP,buff=3)
        txtfinal.to_edge(LEFT,buff=1)
        txtfinal.to_edge(UP,buff=2.5)
        self.play(FadeIn(txtfinal))
        txtfinal2 = Tex("If a transversal intersects two parallel lines, \n then each pair of corresponding angles is equal" , font_size=32 , color = GREEN).to_edge(LEFT,buff=0.1).to_edge(UP,buff=3)
        txtfinal2.to_edge(LEFT,buff=1)
        txtfinal2.to_edge(UP,buff=3)
        self.play(FadeIn(txtfinal2))

        self.wait(8)
        txtfinal3 = Tex("And hence one implies the other: " , font_size=32 , color = RED).to_edge(LEFT,buff=0.1).to_edge(UP,buff=3)
        txtfinal3.to_edge(LEFT,buff=1)
        txtfinal3.to_edge(UP,buff=2.2)
        self.remove(txtfinal)
        self.play(FadeIn(txtfinal3))

        implies = ImageMobject("assets/img/imp.png").scale(1)
        implies.to_edge(LEFT,buff=5.5)
        implies.to_edge(UP,buff=3.9)
        self.play(FadeIn(implies))
        txtfinal4 = Tex("If a transversal intersects two lines such that a pair of  \n corresponding angles is equal, then the two lines are parallel to each other."  , font_size=32 , color = RED).to_edge(LEFT,buff=0.1).to_edge(UP,buff=3)
        txtfinal4.to_edge(LEFT,buff=1)
        txtfinal4.to_edge(DOWN,buff=1.5)
        self.play(FadeIn(txtfinal4))

        self.wait(8)

animation1 = Concept13_2()
animation1.construct()