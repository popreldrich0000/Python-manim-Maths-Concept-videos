from cmath import cos, sin 
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *

class Concept7_1(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        

        with register_font("/home/eldrich-rikaze/Downloads/Metal-Regular.ttf"):
            title = Text("Theorem : If two lines intersect each other,  \n then the vertically opposite angles are equal", font ="Metal" ).set_color(GREEN, PINK).set_height(0.8)
        title.to_edge(UP, buff=1)
        title.to_edge(LEFT, buff=0.6)
        self.play(Write(title))

        self.wait(4)
        
        txt1 = Text("Let AB and CD be 2 lines,  which intersect at a point O" , color='BLUE' ).set_height(0.3)
        txt1.to_edge(LEFT,buff=1)
        txt1.to_edge(DOWN,buff=0.5)
        self.play(FadeIn(txt1))

        self.wait(4)

        l1 =  Line(start=np.array([2, 1, 0]),end=np.array([-2,-1,0])).set_color(color=[GREEN]).shift(LEFT*4)
        l2 =  Line(start=np.array([-2, 1, 0]),end=np.array([2,-1,0])).set_color(color=[GREEN]).shift(LEFT*4)
        self.play(FadeIn(l1,l2))

        self.wait(2)
# A , B on l1
# C , D on l2
        A = Dot([1.4,0.7,0]).set_color(RED).shift(LEFT*4)
        B = Dot([-1.4,-0.7,0]).set_color(RED).shift(LEFT*4)
        C = Dot([-1.4,0.7,0]).set_color(RED).shift(LEFT*4)
        D = Dot([1.4,-0.7,0]).set_color(RED).shift(LEFT*4)
        O = Dot([0,0,0]).set_color(RED).shift(LEFT*4)

        tA = Tex(r"$A$"  , font_size=18 , color = PINK).move_to(np.array([A.get_center()[0]+0.5,A.get_center()[1]-0.3,0])).set_height(0.2)
        tB = Tex(r"$B$"  , font_size=18 , color = PINK).move_to(np.array([B.get_center()[0]-0.5,B.get_center()[1]+0.3,0])).set_height(0.2)
        tC = Tex(r"$C$"  , font_size=18 , color = PINK).move_to(np.array([C.get_center()[0]-0.5,C.get_center()[1]-0.3,0])).set_height(0.2)
        tD = Tex(r"$D$"  , font_size=18 , color = PINK).move_to(np.array([D.get_center()[0]+0.5,D.get_center()[1]+0.3,0])).set_height(0.2)
        tO = Tex(r"$O$"  , font_size=18 , color = PINK).move_to(np.array([O.get_center()[0],O.get_center()[1]-0.3,0])).set_height(0.2)
        self.play(FadeIn(A,B,C,D,tA,tB,tC,tD,tO))
        
        self.wait(5)
        
        angles1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle =  PI + l1.get_angle() - l2.get_angle() , start_angle=l2.get_angle(), color = YELLOW,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        angles2 = AnnularSector(inner_radius=0, outer_radius=0.5, angle =  PI + l1.get_angle() - l2.get_angle() , start_angle=PI +  l2.get_angle(), color = RED,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        angles3 = AnnularSector(inner_radius=0, outer_radius=0.5, angle =  -l1.get_angle() + l2.get_angle() , start_angle=PI + l1.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        self.play(FadeIn(angles1,angles2,angles3))
        
        self.wait(4)
        
       

        txt2 = Tex("To Proof : " + r" $\angle$AOD = $\angle$BOC"   , font_size=24 , color = WHITE)
        txt2.to_edge(RIGHT,buff=2.5)
        txt2.to_edge(UP,buff=1.3)
        self.play(FadeIn(txt2))

        self.wait(4)

        self.remove(txt1)

        txt3 = Tex(r" $\angle$AOD = "   , font_size=24 , color = YELLOW).shift([-1.2,-2.2,0])
        txt3.to_edge(LEFT,buff=1)
        txt3.to_edge(DOWN,buff=2.5)
        angles1d_1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle =  PI + l1.get_angle() - l2.get_angle() , start_angle=l2.get_angle(), color = YELLOW,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        angles1d_1.to_edge(LEFT,buff=2.5)
        angles1d_1.to_edge(DOWN,buff=2.5)
        self.play(FadeIn(txt3,angles1d_1))


        txt4 = Tex(r" $\angle$BOC = "   , font_size=24 , color = RED).shift([-1.2,-2.2,0])
        txt4.to_edge(LEFT,buff=1)
        txt4.to_edge(DOWN,buff=1.5)
        angles2d_1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle =  PI + l1.get_angle() - l2.get_angle() , start_angle=PI +  l2.get_angle(), color = RED,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        angles2d_1.to_edge(LEFT,buff=2.5)
        angles2d_1.to_edge(DOWN,buff=1.5)
        self.play(FadeIn(txt4,angles2d_1))

        txt5 = Tex(r" $\angle$AOC = "   , font_size=24 , color = BLUE).shift([-1.2,-2.2,0])
        txt5.to_edge(LEFT,buff=1)
        txt5.to_edge(DOWN,buff=0.5)
        angles3d_1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle =  -l1.get_angle() + l2.get_angle() , start_angle=PI + l1.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        angles3d_1.to_edge(LEFT,buff=2.5)
        angles3d_1.to_edge(DOWN,buff=0.5)
        self.play(FadeIn(txt5,angles3d_1))


        ldc1 =  Line(start=np.array([2, 1, 0]),end=np.array([-2,-1,0])).set_color(color=[GREEN]).shift(LEFT*4)
        ldc2 =  Line(start=np.array([-2, 1, 0]),end=np.array([0,0,0])).set_color(color=[GREEN]).shift(LEFT*4)
        anglesdc2 = AnnularSector(inner_radius=0, outer_radius=0.5, angle =  PI + l1.get_angle() - l2.get_angle() , start_angle=PI +  l2.get_angle(), color = RED,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        anglesdc3 = AnnularSector(inner_radius=0, outer_radius=0.5, angle =  -l1.get_angle() + l2.get_angle() , start_angle=PI + l1.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        Adc = Dot([1.4,0.7,0]).set_color(RED).shift(LEFT*4)
        Bdc = Dot([-1.4,-0.7,0]).set_color(RED).shift(LEFT*4)
        Cdc = Dot([-1.4,0.7,0]).set_color(RED).shift(LEFT*4)
        Odc = Dot([0,0,0]).set_color(RED).shift(LEFT*4)

        self.play(FadeIn(anglesdc2,anglesdc3,ldc1,ldc2 , Adc , Bdc ,Cdc , Odc),run_time = 0.2)
        dc1 = VGroup( anglesdc2 , anglesdc3 , ldc1 , ldc2 ,  Adc , Bdc ,Cdc , Odc )
        self.play(dc1.animate.shift(8*RIGHT))
        self.play(dc1.animate.rotate(PI - l1.get_angle()))
        self.wait(3)
        tdcA = Tex(r"$A$"  , font_size=18 , color = PINK).move_to(np.array([Adc.get_center()[0]+0.5,Adc.get_center()[1]-0.3,0])).set_height(0.2)
        tdcB = Tex(r"$B$"  , font_size=18 , color = PINK).move_to(np.array([Bdc.get_center()[0]-0.5,Bdc.get_center()[1]+0.3,0])).set_height(0.2)
        tdcC = Tex(r"$C$"  , font_size=18 , color = PINK).move_to(np.array([Cdc.get_center()[0]-0.5,Cdc.get_center()[1]-0.3,0])).set_height(0.2)
        tdcO = Tex(r"$O$"  , font_size=18 , color = PINK).move_to(np.array([Odc.get_center()[0],Odc.get_center()[1]-0.3,0])).set_height(0.2)

        self.play(FadeIn(tdcA,tdcB,tdcC,tdcO))
        
        txt6 = Text(" Axiom used : If a ray stands on a line, \n then the sum of two adjacent angles so formed is 180° "   , font_size=20 , color = PINK).shift([-1.2,-2.2,0])
        txt6.to_edge(LEFT,buff=5)
        txt6.to_edge(DOWN,buff=0.5)
        self.play(FadeIn(txt6))
        
        self.wait(8)
        
        txt7 = Text("Here AB is the line."   , font_size=17 , color = BLUE).shift([-1.2,-2.2,0])
        txt7.to_edge(RIGHT,buff=1.5)
        txt7.to_edge(DOWN,buff=3)
        self.play(FadeIn(txt7))
        txt8 = Text("OC is the ray \n standing on line AB"   , font_size=17 , color = BLUE).shift([-1.2,-2.2,0])
        txt8.to_edge(RIGHT,buff=0.5)
        txt8.to_edge(UP,buff=2.5)
        self.play(FadeIn(txt8))
        
        self.wait(10)


        self.remove(txt7,txt8,tdcA,tdcB,tdcC,tdcO,ldc1,ldc2 , Adc , Bdc ,Cdc , Odc)

        angroup2  = VGroup(anglesdc2,anglesdc3) 
        self.play(angroup2.animate.to_edge(UP ,buff=2.5))
        self.play(angroup2.animate.to_edge(RIGHT ,buff=3.65))

        txt9 = Text("="   , font_size=24 , color = BLUE).shift([-1.2,-2.2,0])
        txt9.to_edge(RIGHT,buff=3)
        txt9.to_edge(UP,buff=2.7)
        
        

        piangle =  AnnularSector(inner_radius=0, outer_radius=0.5, angle =  PI  , start_angle=0, color = PINK,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        piangle.to_edge(RIGHT,buff=1.5)
        piangle.to_edge(UP,buff=2.5)

        self.play(FadeIn(txt9, piangle))

        self.play(anglesdc2.animate.to_edge(RIGHT , buff = 5.3))

        self.wait(6)

        txt10 = Text("+"   , font_size=24 , color = GREEN).shift([-1.2,-2.2,0])
        txt10.to_edge(RIGHT,buff=4.7)
        txt10.to_edge(UP,buff=2.7)
        self.play(FadeIn(txt10))

        self.wait(2)

        txt11 = Text("+"   , font_size=24 , color = GREEN).shift([-1.2,-2.2,0])
        txt11.to_edge(RIGHT,buff=4.7)
        txt11.to_edge(UP,buff=3.3)

        txt12 = Tex(r" $\angle$AOC"   , font_size=24 , color = BLUE)
        txt12.to_edge(RIGHT,buff=3.65)
        txt12.to_edge(UP,buff=3.3)
        
        txt13 = Text("="   , font_size=24 , color = BLUE).shift([-1.2,-2.2,0])
        txt13.to_edge(RIGHT,buff=3)
        txt13.to_edge(UP,buff=3.3)

        txt14 = Tex(r"180$^{\circ}$"   , font_size=26 , color = PINK)
        txt14.to_edge(RIGHT,buff=1.8)
        txt14.to_edge(UP,buff=3.3)

        txt15 = Tex(r" $\angle$BOC"   , font_size=24 , color = RED)
        txt15.to_edge(RIGHT,buff=5.3)
        txt15.to_edge(UP,buff=3.3)

        
        self.play(FadeIn(txt11,txt12,txt13,txt14,txt15))
        totalgrp = VGroup(txt11,txt12,txt13,txt14,txt15,txt10,anglesdc2,anglesdc3,piangle,txt9)
        self.play(totalgrp.animate.to_edge(UP,buff=2.2))

        self.wait(3)


# second shift 


        lcd1 =  Line(start=np.array([2, 1, 0]),end=np.array([0,0,0])).set_color(color=[GREEN]).shift(LEFT*4)
        lcd2 =  Line(start=np.array([-2, 1, 0]),end=np.array([2,-1,0])).set_color(color=[GREEN]).shift(LEFT*4)
        anglescd1 = AnnularSector(inner_radius=0, outer_radius=0.5, angle =  PI + l1.get_angle() - l2.get_angle() , start_angle=l2.get_angle(), color = YELLOW,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        anglescd3 = AnnularSector(inner_radius=0, outer_radius=0.5, angle =  -l1.get_angle() + l2.get_angle() , start_angle=PI + l1.get_angle(), color = BLUE,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        Acd = Dot([1.4,0.7,0]).set_color(RED).shift(LEFT*4)
        Dcd = Dot([1.4,-0.7,0]).set_color(RED).shift(LEFT*4)
        Ccd = Dot([-1.4,0.7,0]).set_color(RED).shift(LEFT*4)
        Ocd = Dot([0,0,0]).set_color(RED).shift(LEFT*4)

        self.play(FadeIn(anglescd1,anglescd3,lcd1,lcd2 , Acd , Dcd ,Ccd , Ocd),run_time = 0.2)
        cd1 = VGroup( anglescd1 , anglescd3 , lcd1 , lcd2 ,  Acd , Dcd ,Ccd , Ocd )
        self.play(cd1.animate.shift(8*RIGHT+2.5*DOWN))
        self.play(cd1.animate.rotate( - l2.get_angle()))
        self.wait(3)
        tcdA = Tex(r"$A$"  , font_size=18 , color = PINK).move_to(np.array([Acd.get_center()[0]+0.5,Acd.get_center()[1]-0.3,0])).set_height(0.2)
        tcdB = Tex(r"$D$"  , font_size=18 , color = PINK).move_to(np.array([Dcd.get_center()[0]-0.5,Dcd.get_center()[1]+0.3,0])).set_height(0.2)
        tcdC = Tex(r"$C$"  , font_size=18 , color = PINK).move_to(np.array([Ccd.get_center()[0]-0.5,Ccd.get_center()[1]-0.3,0])).set_height(0.2)
        tcdO = Tex(r"$O$"  , font_size=18 , color = PINK).move_to(np.array([Ocd.get_center()[0],Ocd.get_center()[1]-0.3,0])).set_height(0.2)

        self.play(FadeIn(tcdA,tcdB,tcdC,tcdO))


        txt16 = Text("Here CD is the line."   , font_size=17 , color = BLUE).shift([-1.2,-2.2,0])
        txt16.to_edge(RIGHT,buff=3)
        txt16.to_edge(DOWN,buff=3)
        self.play(FadeIn(txt16))
        txt17 = Text("OA is the ray standing on line CD"   , font_size=17 , color = BLUE).shift([-1.2,-2.2,0])
        txt17.to_edge(RIGHT,buff=1.5)
        txt17.to_edge(UP,buff=4.3)
        self.play(FadeIn(txt17))
        self.wait(7)
        self.remove(lcd1,lcd2,Acd,Ccd,Dcd,Ocd,tcdA,tcdB,tcdC,tcdO,txt16,txt17)

        
        angroup3  = VGroup(anglescd1,anglescd3) 
        # self.play(angroup3.animate.move_to([0,0,0]))
        self.play(angroup3.animate.flip(UP),run_time =0.5)
        self.play(angroup3.animate.to_edge(RIGHT, buff = 3.65),run_time =0.5)
        self.play(angroup3.animate.to_edge(UP, buff = 4.2),run_time =0.5)


        txt = Text("="   , font_size=24 , color = BLUE).shift([-1.2,-2.2,0])
        txt.to_edge(RIGHT,buff=3)
        txt.to_edge(UP,buff=4.5)
        
        

        piangle2 =  AnnularSector(inner_radius=0, outer_radius=0.5, angle =  PI  , start_angle=0, color = PINK,fill_opacity=0.5, stroke_width=0).shift(LEFT*4)
        piangle2.to_edge(RIGHT,buff=1.5)
        piangle2.to_edge(UP,buff=4.2)

        self.play(FadeIn(txt, piangle2))

        self.play(anglescd1.animate.to_edge(RIGHT , buff = 5.3))


        txt19 = Text("+"   , font_size=24 , color = GREEN).shift([-1.2,-2.2,0])
        txt19.to_edge(RIGHT,buff=4.7)
        txt19.to_edge(UP,buff=4.5)
        self.play(FadeIn(txt19))
# 
        self.wait(2)
# 
        txt20 = Text("+"   , font_size=24 , color = GREEN).shift([-1.2,-2.2,0])
        txt20.to_edge(RIGHT,buff=4.7)
        txt20.to_edge(UP,buff=5)
# 
        txt21 = Tex(r" $\angle$AOC"   , font_size=24 , color = BLUE)
        txt21.to_edge(RIGHT,buff=3.65)
        txt21.to_edge(UP,buff=5)
        # 
        txt22 = Text("="   , font_size=24 , color = BLUE).shift([-1.2,-2.2,0])
        txt22.to_edge(RIGHT,buff=3)
        txt22.to_edge(UP,buff=5)
# 
        txt23 = Tex(r"180$^{\circ}$"   , font_size=26 , color = PINK)
        txt23.to_edge(RIGHT,buff=1.8)
        txt23.to_edge(UP,buff=5)
# 
        txt24 = Tex(r" $\angle$AOD"   , font_size=24 , color = YELLOW)
        txt24.to_edge(RIGHT,buff=5.3)
        txt24.to_edge(UP,buff=5)
# 
        # 
        self.play(FadeIn(txt20,txt21,txt22,txt23,txt24))

        self.play(totalgrp.animate.to_edge(DOWN,buff=1.7))
# 
        self.play(totalgrp.animate.to_edge(LEFT,buff=4))

        equalto = VGroup(txt,txt22)
        pi = VGroup(txt23,piangle2)
        anglegrp = VGroup(txt24,txt21,txt20,txt19,anglescd1,anglescd3)
        tot2 = VGroup(txt,txt22,txt23,piangle2,txt24,txt21,txt20,txt19,anglescd1,anglescd3)
        self.play(tot2.animate.to_edge(DOWN,buff=1.7))
        self.play(anglegrp.animate.to_edge(RIGHT,buff=0.3))
        self.play(equalto.animate.to_edge(RIGHT,buff=3))
        self.play(pi.animate.to_edge(RIGHT,buff=3.5))

        self.wait(8)
        self.remove(equalto,pi, piangle,txt14)
        self.wait(2)
        self.play(anglegrp.animate.to_edge(RIGHT,buff=4.45))
        rec1 =  Rectangle(fill_color = RED, width = 1 , height = 1.3,fill_opacity=0.5).to_edge(RIGHT, buff = 4.3).to_edge(DOWN , buff = 1.6)
        rec2 =  Rectangle(fill_color = RED, width = 1 , height = 1.3,fill_opacity=0.5).to_edge(LEFT, buff = 5.5).to_edge(DOWN , buff = 1.6)

        self.play(FadeIn(rec1,rec2))
        self.wait(8)
        self.remove(rec2,rec1,txt21,anglescd3,anglesdc3,txt12, txt10,txt11,txt19,txt20)

        self.wait(3)

        ad1 = VGroup(txt15,anglesdc2)
        self.play(ad1.animate.shift(RIGHT*1.6))

        self.wait(5)

        finalgrp = VGroup(txt24,txt15,anglescd1,anglesdc2,txt13,txt9)
        self.play(finalgrp.animate.to_edge(RIGHT,buff=2.3))
        self.play(finalgrp.animate.to_edge(UP,buff=2))

        self.wait(8)
        txt33 = Tex(r"Similarly we can prove $\angle$AOC = $\angle$BOD"   , font_size=24 , color = YELLOW)
        txt33.to_edge(RIGHT,buff=1)
        self.play(FadeIn(txt33))
        self.wait(5)
run1 = Concept7_1()
run1.construct()


        