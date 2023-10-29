from cmath import cos, sin, tan 
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *





class Concept11(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Types of pairs of angles formed when a transversal intersects two lines.", font ="Metal" ,font_size=32).set_color(GREEN, PINK)
            
        title.to_edge(UP, buff=0.5)
        title.to_edge(LEFT, buff=0.6)
        self.play(Write(title))
        self.wait(4)

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
        self.wait(7)


        txt4 = Text("Let t be the transversal" , color='BLUE' ,slant=ITALIC ,font_size=18)
        txt4.to_edge(RIGHT,buff=1)
        txt4.to_edge(DOWN,buff=0.5)
        self.play(FadeIn(txt4))
        lt = Line(start=np.array([-0.5,-1, 0]),end=np.array([1.25,2.5,0])).set_color(color=[PINK])
        txt5 = Tex(r"$t$"  , font_size=18 , color = PINK).move_to(np.array([-0.3,-1,0])).set_height(0.2)
        self.play(FadeIn(lt,txt5))
        self.wait(4)

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
        txt11 = Text("Corresponding angles are the angles which are formed in \n matching corners or corresponding corners with the transversal" , color='YELLOW' ,slant=ITALIC,font_size=18 )
        txt11.to_edge(LEFT,buff=0.5)
        txt11.to_edge(UP,buff=2.5)
        self.play(FadeIn(txt11))
        self.wait(4)
        txt12 = Text("Corresponding angles in this figure are : " , color='YELLOW' ,slant=ITALIC,font_size=18 )
        txt12.to_edge(LEFT,buff=0.5)
        txt12.to_edge(UP,buff=3.5)
        self.play(FadeIn(txt12))
        

        self.wait(8)

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
        self.play(FadeIn(angle1ufd,angle2ufd,angle3ufd,angle4ufd,angle5ufd,angle6ufd,angle7ufd,angle8ufd,txtangle1d,txtangle2d,txtangle3d,txtangle4d,txtangle5d,txtangle6d,txtangle7d,txtangle8d))
        self.play(angle1ufd.animate.to_edge(DOWN,buff=2),angle5ufd.animate.to_edge(DOWN,buff=2))
        self.play(angle1ufd.animate.to_edge(LEFT,buff=0.3),angle5ufd.animate.to_edge(LEFT,buff=2))
        # self.play(angle5ufd.animate.to_edge(DOWN,buff=2))
        # self.play(angle5ufd.animate.to_edge(LEFT,buff=2))
        
        txtand1 =  Text("and" , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=1.2)
        self.play(FadeIn(txtand1))

        txtcom1 =  Text("," , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=3)
        self.play(FadeIn(txtcom1))
        txtangle1d= Tex( r" $\angle$1"     , font_size=28 , color = GREEN).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=0.4)
        txtangle5d= Tex( r" $\angle$5"     , font_size=28 , color = PINK).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=2.2)
        self.play(FadeIn(txtangle1d,txtangle5d))

        txtbrac1 =  Text("(                  )" , color='YELLOW' ,slant=ITALIC,font_size=32 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=0.05)
        self.play(FadeIn(txtbrac1))
        self.play(angle2ufd.animate.to_edge(DOWN,buff=2),angle6ufd.animate.to_edge(DOWN,buff=2))        
        self.play(angle2ufd.animate.to_edge(LEFT,buff=3.5),angle6ufd.animate.to_edge(LEFT,buff=5.2))


        txtand2 =  Text("and" , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=4.4)
        self.play(FadeIn(txtand2))

        txtcom2 =  Text("," , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=6.2)
        self.play(FadeIn(txtcom2))
        txtbrac2 =  Text("(                  )" , color='YELLOW' ,slant=ITALIC,font_size=32 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=3.2)
        self.play(FadeIn(txtbrac2))

        txtangle2d= Tex( r" $\angle$2"     , font_size=28 , color = BLUE).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=3.6)
        txtangle6d= Tex( r" $\angle$6"     , font_size=28 , color = WHITE).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=5.4)
        self.play(FadeIn(txtangle2d,txtangle6d))

        self.play(angle4ufd.animate.to_edge(DOWN,buff=2),angle8ufd.animate.to_edge(DOWN,buff=2))
        self.play(angle4ufd.animate.to_edge(LEFT,buff=6.7),angle8ufd.animate.to_edge(LEFT,buff=8.4))
        
        
        
        txtand3 =  Text("and" , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=7.6)
        self.play(FadeIn(txtand3))
        
        txtcom3 =  Text("," , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=9.4)
        self.play(FadeIn(txtcom3))

        txtbrac3 =  Text("(                  )" , color='YELLOW' ,slant=ITALIC,font_size=32 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=6.4)
        self.play(FadeIn(txtbrac3))

        txtangle4d= Tex( r" $\angle$4"     , font_size=28 , color = YELLOW).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=6.8)
        txtangle8d= Tex( r" $\angle$8"     , font_size=28 , color = ORANGE).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=8.5)
        self.play(FadeIn(txtangle4d,txtangle8d))


        self.play(angle3ufd.animate.to_edge(DOWN,buff=2),angle7ufd.animate.to_edge(DOWN,buff=2))        
        self.play(angle3ufd.animate.to_edge(LEFT,buff=9.9),angle7ufd.animate.to_edge(LEFT,buff=11.6))
        # self.play(angle7ufd.animate.to_edge(DOWN,buff=2))
        # self.play(angle7ufd.animate.to_edge(LEFT,buff=11.6))

        txtand4 =  Text("and" , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=10.8)
        self.play(FadeIn(txtand4))
        txtbrac4 =  Text("(                  )" , color='YELLOW' ,slant=ITALIC,font_size=32 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=9.6)
        self.play(FadeIn(txtbrac4))

        txtangle3d= Tex( r" $\angle3$"     , font_size=28 , color = RED).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=10)
        txtangle7d= Tex( r" $\angle7$"     , font_size=28 , color = PURPLE).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=11.7)
        self.play(FadeIn(txtangle3d,txtangle7d))


        self.wait(10)

        self.remove(txtand1,txtand2,txtand3,txtand4,txtcom1,txtcom2,txtcom3,txt11,txt12,angle1ufd,angle2ufd,angle3ufd,angle4ufd,angle5ufd,angle6ufd,angle7ufd,angle8ufd,txtangle1d,txtangle2d,txtangle3d,txtangle4d,txtangle5d,txtangle6d,txtangle7d,txtangle8d,txtbrac1,txtbrac2,txtbrac3,txtbrac4,txtand3,txtand2,txtand1)

        txt13 = Text("Alternate interior angles lie on the inner side of the lines \n but on the opposite sides of the transversal" , color='YELLOW' ,slant=ITALIC,font_size=18 )
        txt13.to_edge(LEFT,buff=0.5)
        txt13.to_edge(UP,buff=2.5)
        self.play(FadeIn(txt13))
        self.wait(4)
        txt14 = Text("Alternate interior angles in this figure are : " , color='YELLOW' ,slant=ITALIC,font_size=18 )
        txt14.to_edge(LEFT,buff=0.5)
        txt14.to_edge(UP,buff=3.5)
        self.play(FadeIn(txt14))

        self.wait(8)

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
        self.play(FadeIn(angle1ufd,angle2ufd,angle3ufd,angle4ufd,angle5ufd,angle6ufd,angle7ufd,angle8ufd,txtangle1d,txtangle2d,txtangle3d,txtangle4d,txtangle5d,txtangle6d,txtangle7d,txtangle8d))
        self.play(angle4ufd.animate.to_edge(DOWN,buff=2),angle6ufd.animate.to_edge(DOWN,buff=2))
        self.play(angle4ufd.animate.to_edge(LEFT,buff=0.35),angle6ufd.animate.to_edge(LEFT,buff=2))
        
        
        txtand1 =  Text("and" , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=1.2)
        self.play(FadeIn(txtand1))

        txtcom1 =  Text("," , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=3)
        self.play(FadeIn(txtcom1))
        txtangle4d= Tex( r" $\angle$4"     , font_size=28 , color = YELLOW).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=0.4)
        txtangle6d= Tex( r" $\angle$6"     , font_size=28 , color = WHITE).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=2.2)
        self.play(FadeIn(txtangle4d,txtangle6d))

        txtbrac1 =  Text("(                  )" , color='YELLOW' ,slant=ITALIC,font_size=32 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=0.05)
        self.play(FadeIn(txtbrac1))    
        

#

        self.play(angle3ufd.animate.to_edge(DOWN,buff=2),angle5ufd.animate.to_edge(DOWN,buff=2))        
        self.play(angle3ufd.animate.to_edge(LEFT,buff=3.5),angle5ufd.animate.to_edge(LEFT,buff=5.2))


        txtand2 =  Text("and" , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=4.4)
        self.play(FadeIn(txtand2))

        # txtcom2 =  Text("," , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=6.2)
        # self.play(FadeIn(txtcom2))
        txtbrac2 =  Text("(                  )" , color='YELLOW' ,slant=ITALIC,font_size=32 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=3.2)
        self.play(FadeIn(txtbrac2))

        txtangle3d= Tex( r" $\angle3$"     , font_size=28 , color = RED).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=3.6)
        txtangle5d= Tex( r" $\angle5$"     , font_size=28 , color = PINK).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=5.4)
        self.play(FadeIn(txtangle3d,txtangle5d))
        
        self.wait(8)

        self.remove(txt13,txt14,txtangle3d,txtangle5d,txtbrac2,txtand2,txtbrac1,txtangle4d,txtangle6d,txtcom1,txtand1,angle1ufd,angle2ufd,angle3ufd,angle4ufd,angle5ufd,angle6ufd,angle7ufd,angle8ufd,txtangle1d,txtangle2d,txtangle3d,txtangle4d,txtangle5d,txtangle6d,txtangle7d,txtangle8d)

        txt13 = Text("Alternate exterior angles are the pair of angles that are formed on the \n outer side of the  lines but on the opposite side of the transversal" , color='YELLOW' ,slant=ITALIC,font_size=18 )
        txt13.to_edge(LEFT,buff=0.5)
        txt13.to_edge(UP,buff=2.5)
        self.play(FadeIn(txt13))
        self.wait(4)
        txt14 = Text("Alternate exterior angles in this figure are : " , color='YELLOW' ,slant=ITALIC,font_size=18 )
        txt14.to_edge(LEFT,buff=0.5)
        txt14.to_edge(UP,buff=3.5)
        self.play(FadeIn(txt14))

        self.wait(8)
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
        vg3 = VGroup(angle1ufd,angle2ufd,angle3ufd,angle4ufd,angle5ufd,angle6ufd,angle7ufd,angle8ufd,txtangle1d,txtangle2d,txtangle3d,txtangle4d,txtangle5d,txtangle6d,txtangle7d,txtangle8d)
        vg3.to_edge(RIGHT,buff=0.8)
        self.play(FadeIn(angle1ufd,angle2ufd,angle3ufd,angle4ufd,angle5ufd,angle6ufd,angle7ufd,angle8ufd,txtangle1d,txtangle2d,txtangle3d,txtangle4d,txtangle5d,txtangle6d,txtangle7d,txtangle8d))
        self.play(angle1ufd.animate.to_edge(DOWN,buff=2),angle7ufd.animate.to_edge(DOWN,buff=2))
        self.play(angle1ufd.animate.to_edge(LEFT,buff=0.35),angle7ufd.animate.to_edge(LEFT,buff=2))
        
        
        txtand1 =  Text("and" , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=1.2)
        self.play(FadeIn(txtand1))

        txtcom1 =  Text("," , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=3)
        self.play(FadeIn(txtcom1))
        txtangle1d= Tex( r" $\angle1$"     , font_size=28 , color = GREEN).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=0.4)
        txtangle7d= Tex( r" $\angle7$"     , font_size=28 , color = PURPLE).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=2.2)
        self.play(FadeIn(txtangle1d,txtangle7d))

        txtbrac1 =  Text("(                  )" , color='YELLOW' ,slant=ITALIC,font_size=32 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=0.05)
        self.play(FadeIn(txtbrac1))    
        

#

        self.play(angle2ufd.animate.to_edge(DOWN,buff=2),angle8ufd.animate.to_edge(DOWN,buff=2))        
        self.play(angle2ufd.animate.to_edge(LEFT,buff=3.5),angle8ufd.animate.to_edge(LEFT,buff=5.2))


        txtand2 =  Text("and" , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=4.4)
        self.play(FadeIn(txtand2))

        # txtcom2 =  Text("," , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=6.2)
        # self.play(FadeIn(txtcom2))
        txtbrac2 =  Text("(                  )" , color='YELLOW' ,slant=ITALIC,font_size=32 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=3.2)
        self.play(FadeIn(txtbrac2))

        txtangle2d= Tex( r" $\angle2$"     , font_size=28 , color = BLUE).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=3.6)
        txtangle8d= Tex( r" $\angle8$"     , font_size=28 , color = ORANGE).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=5.4)
        self.play(FadeIn(txtangle2d,txtangle8d))
        
        self.wait(8)

# ###############
        self.remove(txt13,txt14,txtangle1d,txtangle7d,txtbrac2,txtand2,txtbrac1,txtangle2d,txtangle8d,txtcom1,txtand1,angle1ufd,angle2ufd,angle3ufd,angle4ufd,angle5ufd,angle6ufd,angle7ufd,angle8ufd,txtangle1d,txtangle2d,txtangle3d,txtangle4d,txtangle5d,txtangle6d,txtangle7d,txtangle8d)

        txt13 = Text("Consecutive interior angles are the pair of Interior angles \n on the same side of the transversal" , color='YELLOW' ,slant=ITALIC,font_size=18 )
        txt13.to_edge(LEFT,buff=0.5)
        txt13.to_edge(UP,buff=2.5)
        self.play(FadeIn(txt13))
        self.wait(4)
        txt14 = Text("Consecutive interior angles in this figure are : " , color='YELLOW' ,slant=ITALIC,font_size=18 )
        txt14.to_edge(LEFT,buff=0.5)
        txt14.to_edge(UP,buff=3.5)
        self.play(FadeIn(txt14))

        self.wait(8)
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
        vg3 = VGroup(angle1ufd,angle2ufd,angle3ufd,angle4ufd,angle5ufd,angle6ufd,angle7ufd,angle8ufd,txtangle1d,txtangle2d,txtangle3d,txtangle4d,txtangle5d,txtangle6d,txtangle7d,txtangle8d)
        vg3.to_edge(RIGHT,buff=0.8)
        self.play(FadeIn(angle1ufd,angle2ufd,angle3ufd,angle4ufd,angle5ufd,angle6ufd,angle7ufd,angle8ufd,txtangle1d,txtangle2d,txtangle3d,txtangle4d,txtangle5d,txtangle6d,txtangle7d,txtangle8d))
        self.play(angle4ufd.animate.to_edge(DOWN,buff=2),angle5ufd.animate.to_edge(DOWN,buff=2))
        self.play(angle4ufd.animate.to_edge(LEFT,buff=0.35),angle5ufd.animate.to_edge(LEFT,buff=2))
        
        
        txtand1 =  Text("and" , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=1.2)
        self.play(FadeIn(txtand1))

        txtcom1 =  Text("," , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=3)
        self.play(FadeIn(txtcom1))
        txtangle4d= Tex( r" $\angle4$"     , font_size=28 , color = YELLOW).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=0.4)
        txtangle5d= Tex( r" $\angle5$"     , font_size=28 , color = PINK).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=2.2)
        self.play(FadeIn(txtangle4d,txtangle5d))

        txtbrac1 =  Text("(                  )" , color='YELLOW' ,slant=ITALIC,font_size=32 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=0.05)
        self.play(FadeIn(txtbrac1))    
        

#

        self.play(angle3ufd.animate.to_edge(DOWN,buff=2),angle6ufd.animate.to_edge(DOWN,buff=2))        
        self.play(angle3ufd.animate.to_edge(LEFT,buff=3.5),angle6ufd.animate.to_edge(LEFT,buff=5.2))


        txtand2 =  Text("and" , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=4.4)
        self.play(FadeIn(txtand2))

        # txtcom2 =  Text("," , color='YELLOW' ,slant=ITALIC,font_size=18 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=6.2)
        # self.play(FadeIn(txtcom2))
        txtbrac2 =  Text("(                  )" , color='YELLOW' ,slant=ITALIC,font_size=32 ).to_edge(DOWN,buff=2).to_edge(LEFT,buff=3.2)
        self.play(FadeIn(txtbrac2))

        txtangle3d= Tex( r" $\angle3$"     , font_size=28 , color = RED).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=3.6)
        txtangle6d= Tex( r" $\angle6$"     , font_size=28 , color = WHITE).to_edge(DOWN,buff=1.5).to_edge(LEFT,buff=5.4)
        self.play(FadeIn(txtangle3d,txtangle6d))
        
        self.wait(8)

        self.remove(txt13,txt14,txtangle3d,txtangle6d,txtbrac2,txtand2,txtbrac1,txtangle4d,txtangle5d,txtcom1,txtand1,angle1ufd,angle2ufd,angle3ufd,angle4ufd,angle5ufd,angle6ufd,angle7ufd,angle8ufd,txtangle1d,txtangle2d,txtangle3d,txtangle4d,txtangle5d,txtangle6d,txtangle7d,txtangle8d)

class Concept11_1(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Types of pairs of angles formed when a transversal intersects two lines.", font ="Metal" ,font_size=32).set_color(GREEN, PINK)
            
        title.to_edge(UP, buff=0.5)
        title.to_edge(LEFT, buff=0.6)
        self.add(title)

        txt1 = Tex( "Let " + r"$l1$" + " and " + r"$l2$" +" be two lines." , font_size=28 , color = YELLOW)
        txt1.to_edge(LEFT,buff=1)
        txt1.to_edge(DOWN,buff=0.5)
        l1 = Line(start=np.array([-1.5, 1.8, 0]),end=np.array([1.5,1.2,0])).set_color(color=[PINK])
        l2 = Line(start=np.array([-1.5, -0.3, 0]),end=np.array([1.5,0.3,0])).set_color(color=[PINK])
        txt2 = Tex(r"$l1$"  , font_size=18 , color = PINK).move_to(np.array([-1.7,1.75,0])).set_height(0.2)
        txt3 = Tex(r"$l2$"  , font_size=18 , color = PINK).move_to(np.array([-1.7,-0.15,0])).set_height(0.2)
        self.add(txt1)
        self.add(l1,l2)
        self.add(txt2,txt3)


        txt4 = Text("Let t be the transversal" , color='BLUE' ,slant=ITALIC ,font_size=18)
        txt4.to_edge(RIGHT,buff=1)
        txt4.to_edge(DOWN,buff=0.5)
        self.add(txt4)
        lt = Line(start=np.array([-0.5,-1, 0]),end=np.array([1.25,2.5,0])).set_color(color=[PINK])
        txt5 = Tex(r"$t$"  , font_size=18 , color = PINK).move_to(np.array([-0.3,-1,0])).set_height(0.2)
        self.add(lt,txt5)

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


        self.add(angle1uf,angle2uf,angle3uf,angle4uf,angle5uf,angle6uf,angle7uf,angle8uf,txtangle1,txtangle2,txtangle3,txtangle4,txtangle5,txtangle6,txtangle7,txtangle8)
        
        vg1 = VGroup(txt5,txt2,txt3,l1,l2,lt,angle1uf,angle2uf,angle3uf,angle4uf,angle5uf,angle6uf,angle7uf,angle8uf,txtangle1,txtangle2,txtangle3,txtangle4,txtangle5,txtangle6,txtangle7,txtangle8)
        vg1.to_edge(RIGHT,buff=0.8)
        txt4 = Text("Summary" , color='YELLOW' ,slant=ITALIC ,font_size=26)
        txt4.to_edge(UP, buff=1.5)
        txt4.to_edge(LEFT, buff=4)
        self.play(FadeIn(txt4))
        txt4 = Text("Corresponding angles" , color=BLUE_A ,slant=ITALIC ,font_size=18)
        txt4.to_edge(UP, buff=2)
        txt4.to_edge(LEFT, buff=1)
        self.play(FadeIn(txt4))
        txtangle= Tex( r" $\angle$1"     , font_size=28 , color = GREEN).to_edge(UP, buff=2.3).to_edge(LEFT, buff=1)
        self.play(FadeIn(txtangle))
        txtangle= Tex( " and "     , font_size=28 , color = WHITE).to_edge(UP, buff=2.3).to_edge(LEFT, buff=1.8)
        self.play(FadeIn(txtangle))
        txtangle= Tex( r" $\angle$5"     , font_size=28 , color = PINK).to_edge(UP, buff=2.3).to_edge(LEFT, buff=2.8)
        self.play(FadeIn(txtangle))
        txtangle= Tex( r" $\angle$2"     , font_size=28 , color = BLUE).to_edge(UP, buff=2.8).to_edge(LEFT, buff=1)
        self.play(FadeIn(txtangle))

        txtangle= Tex( " and "     , font_size=28 , color = WHITE).to_edge(UP, buff=2.8).to_edge(LEFT, buff=1.8)
        self.play(FadeIn(txtangle))

        txtangle= Tex( r" $\angle$6"     , font_size=28 , color = WHITE).to_edge(UP, buff=2.8).to_edge(LEFT, buff=2.8)
        self.play(FadeIn(txtangle))

        txtangle= Tex( r" $\angle$4"     , font_size=28 , color = YELLOW).to_edge(UP, buff=3.3).to_edge(LEFT, buff=1)
        self.play(FadeIn(txtangle))

        txtangle= Tex( " and "     , font_size=28 , color = WHITE).to_edge(UP, buff=3.3).to_edge(LEFT, buff=1.8)
        self.play(FadeIn(txtangle))

        txtangle= Tex( r" $\angle$8"     , font_size=28 , color = ORANGE).to_edge(UP, buff=3.3).to_edge(LEFT, buff=2.8)
        self.play(FadeIn(txtangle))

        txtangle= Tex( r" $\angle$3"     , font_size=28 , color = RED).to_edge(UP, buff=3.8).to_edge(LEFT, buff=1)
        self.play(FadeIn(txtangle))

        txtangle= Tex( " and "     , font_size=28 , color = WHITE).to_edge(UP, buff=3.8).to_edge(LEFT, buff=1.8)
        self.play(FadeIn(txtangle))

        txtangle= Tex( r" $\angle$7"     , font_size=28 , color = PURPLE).to_edge(UP, buff=3.8).to_edge(LEFT, buff=2.8)
        self.play(FadeIn(txtangle))



        txt4 = Text("Alternate interior angles" , color='GREEN' ,slant=ITALIC ,font_size=18)
        txt4.to_edge(UP, buff=2)
        txt4.to_edge(LEFT, buff=5)
        self.play(FadeIn(txt4))
        txtangle= Tex( r" $\angle$4"     , font_size=28 , color = YELLOW).to_edge(UP, buff=2.3).to_edge(LEFT, buff=6)
        self.play(FadeIn(txtangle))
        txtangle= Tex( " and "     , font_size=28 , color = WHITE).to_edge(UP, buff=2.3).to_edge(LEFT, buff=6.8)
        self.play(FadeIn(txtangle))
        txtangle= Tex( r" $\angle$6"     , font_size=28 , color = WHITE).to_edge(UP, buff=2.3).to_edge(LEFT, buff=7.8)
        self.play(FadeIn(txtangle))
        txtangle= Tex( r" $\angle$3"     , font_size=28 , color = RED).to_edge(UP, buff=2.8).to_edge(LEFT, buff=6)
        self.play(FadeIn(txtangle))

        txtangle= Tex( " and "     , font_size=28 , color = WHITE).to_edge(UP, buff=2.8).to_edge(LEFT, buff=6.8)
        self.play(FadeIn(txtangle))

        txtangle= Tex( r" $\angle$5"     , font_size=28 , color = PINK).to_edge(UP, buff=2.8).to_edge(LEFT, buff=7.8)
        self.play(FadeIn(txtangle))
        txt4 = Text("Alternate exterior angles" , color='RED' ,slant=ITALIC ,font_size=18)
        txt4.to_edge(UP, buff=5)
        txt4.to_edge(LEFT, buff=1)
        self.play(FadeIn(txt4))
        txtangle= Tex( r" $\angle$1"     , font_size=28 , color = GREEN).to_edge(UP, buff=5.3).to_edge(LEFT, buff=1)
        self.play(FadeIn(txtangle))
        txtangle= Tex( " and "     , font_size=28 , color = WHITE).to_edge(UP, buff=5.3).to_edge(LEFT, buff=1.8)
        self.play(FadeIn(txtangle))
        txtangle= Tex( r" $\angle$5"     , font_size=28 , color = PINK).to_edge(UP, buff=5.3).to_edge(LEFT, buff=2.8)
        self.play(FadeIn(txtangle))
        txtangle= Tex( r" $\angle$2"     , font_size=28 , color = BLUE).to_edge(UP, buff=5.8).to_edge(LEFT, buff=1)
        self.play(FadeIn(txtangle))

        txtangle= Tex( " and "     , font_size=28 , color = WHITE).to_edge(UP, buff=5.8).to_edge(LEFT, buff=1.8)
        self.play(FadeIn(txtangle))

        txtangle= Tex( r" $\angle$6"     , font_size=28 , color = WHITE).to_edge(UP, buff=5.8).to_edge(LEFT, buff=2.8)
        self.play(FadeIn(txtangle))
        
        txt4 = Text("Consecutive interior angles" , color='WHITE' ,slant=ITALIC ,font_size=18)
        txt4.to_edge(UP, buff=5)
        txt4.to_edge(LEFT, buff=5)
        self.play(FadeIn(txt4))
        txtangle= Tex( r" $\angle$4"     , font_size=28 , color = YELLOW).to_edge(UP, buff=5.3).to_edge(LEFT, buff=6)
        self.play(FadeIn(txtangle))
        txtangle= Tex( " and "     , font_size=28 , color = WHITE).to_edge(UP, buff=5.3).to_edge(LEFT, buff=6.8)
        self.play(FadeIn(txtangle))
        txtangle= Tex( r" $\angle$5"     , font_size=28 , color = PINK).to_edge(UP, buff=5.3).to_edge(LEFT, buff=7.8)
        self.play(FadeIn(txtangle))
        txtangle= Tex( r" $\angle$3"     , font_size=28 , color = RED).to_edge(UP, buff=5.8).to_edge(LEFT, buff=6)
        self.play(FadeIn(txtangle))

        txtangle= Tex( " and "     , font_size=28 , color = WHITE).to_edge(UP, buff=5.8).to_edge(LEFT, buff=6.8)
        self.play(FadeIn(txtangle))

        txtangle= Tex( r" $\angle$6"     , font_size=28 , color = WHITE).to_edge(UP, buff=5.8).to_edge(LEFT, buff=7.8)
        self.play(FadeIn(txtangle))
        self.wait(8)
animation1 = Concept11_1()
animation1.construct()