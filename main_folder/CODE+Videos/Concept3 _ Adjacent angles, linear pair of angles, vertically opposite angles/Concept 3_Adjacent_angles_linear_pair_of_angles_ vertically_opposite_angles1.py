from cmath import cos, sin 
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *
class Concept3_1(Scene):
    def construct(self):
        title = MathTex("Adjacent \ angles").set_color_by_gradient(GREEN, PINK).set_height(0.8)
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        title.to_edge(UP, buff=1)
        self.add(logo)        
        self.play(FadeIn(title))
        self.wait(5)
        defination = Text("Two angles are adjacent, if they have a common vertex, a common arm and \n their non-common arms are on different sides of the common arm." , line_spacing=1 , t2c={'[15:23]': BLUE } ,  slant=ITALIC , font_size=18 , color = WHITE)

        defination.to_edge( UP , buff = 3)
        defination.to_edge( LEFT , buff = 0.5)
        self.play(FadeIn(defination))
        self.wait(10)
        self.remove(title)
        self.play(defination.animate.shift(+UP*2.5),run_time =2)
        self.wait(5)
class Concept3_2(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        
        self.add(logo)        
        
        defination = Text("Two angles are adjacent, if they have a common vertex, a common arm and \n their non-common arms are on different sides of the common arm." , line_spacing=1 , t2c={'[15:23]': BLUE } ,  slant=ITALIC , font_size=18 , color = WHITE)

        defination.to_edge( UP , buff = 0.5)
        defination.to_edge( LEFT , buff = 0.5)
        self.add(defination)
        self.wait(2)
        a1 = Vector( direction=[-2,2,0]).set_color(color=[GREEN]).shift([-2.5,-1,0])
        a2 = Vector( direction=[2,2,0]).set_color(color=[YELLOW]).shift([-2.5,-1,0])
        a3 = Vector( direction=[2*(1.41),0,0]).set_color(color=[BLUE]).shift([-2.5,-1,0])
        vertex = Dot([-2.5,-1,0]).set_color(RED).scale(1)
        txt1 = Text("This is the commom vertex of the two Angles" , line_spacing=1 ,  slant=ITALIC , font_size=18 , color = WHITE).shift([-3,-3,0])
        txt2 = Text("This is the commom arm between the two Angles" , line_spacing=1 ,  slant=ITALIC , font_size=18 , color = WHITE).shift(3.7*RIGHT)
        angle1_1 = Arc(radius=0.4, start_angle=0, angle=a2.get_angle(), num_components=9, arc_center=np.array([-2.5,-1,0]))
        angle1_2 = Arc(radius=0.5, start_angle=0, angle=a2.get_angle(), num_components=9, arc_center=np.array([-2.5,-1,0]))

        angle2 = Arc(radius=0.8, start_angle=a2.get_angle(), angle=a1.get_angle()-a2.get_angle(), num_components=9, arc_center=np.array([-2.5,-1,0]))
        vertexarrow = Arrow(start = [-3.5,-2.8,0], end = [-2.6,-1.1,0]).set_color(color=[RED])
        commmonarmarrow = Arrow(start = [-1.5,0,0], end = [0.6,0,0]).set_color(color=[YELLOW])
        self.play(FadeIn(a1,a2,a3,angle1_1,angle1_2,angle2))
        self.wait(5)
        self.play(FadeIn(vertex,txt1,vertexarrow))
        self.wait(8)
        self.play(FadeIn(txt2,commmonarmarrow))
        self.wait(8)
class Concept3_3(Scene):
    def construct(self):
        title = MathTex("Linear \ Pair \ Of \ Angles").set_color_by_gradient(GREEN, PINK).set_height(0.8)
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        title.to_edge(UP, buff=1)
        self.add(logo)        
        self.play(FadeIn(title))
        self.wait(5)
        txt1 = Text("Linear Pair Of Angles are a special case of Adjacent Angles" , line_spacing=1 , t2c={'[0:21]': BLUE } , slant=ITALIC , font_size=18 , color = WHITE)
        txt1.to_edge(UP , buff = 3)
        txt1.to_edge(LEFT , buff = 0.5)
        self.play(FadeIn(txt1))
        self.wait(6)
        self.remove(title)
        self.play(txt1.animate.shift(+UP*2.5),run_time =2)
        txt2 = Tex(r"Lets $\angle$ABC and $\angle$ABD be two adjacent angles with AB as the commom arm").set_color(RED).set_height(0.2)

        txt2.to_edge(DOWN , buff = 1)
        txt2.to_edge(LEFT , buff = 0.5)
        a1 = Vector( direction=[-2,2,0]).set_color(color=[GREEN]).shift([-2.5,-2,0])
        a2 = Vector( direction=[2,2,0]).set_color(color=[YELLOW]).shift([-2.5,-2,0])
        a3 = Vector( direction=[2*(1.41),0,0]).set_color(color=[BLUE]).shift([-2.5,-2,0])

        # veca1 = 
        # veca2 = 
        thetac = ValueTracker(a2.get_angle()-a3.get_angle())
        thetas = ValueTracker(a1.get_angle()-a3.get_angle())

        commomarm = always_redraw(lambda : Vector(direction=np.array([2*1.41*cos(thetac.get_value()).real,2*1.41*sin(thetac.get_value()).real,0])).set_color(color=[RED]).shift([-2.5,-2,0]))
        sidearm = always_redraw(lambda : Vector(direction=np.array([2*1.41*cos(thetas.get_value()).real,2*1.41*sin(thetas.get_value()).real,0])).set_color(color=[RED]).shift([-2.5,-2,0]))
        A = Dot(point=np.array([-0.85, -0.35, 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=WHITE)
        C = always_redraw(lambda : Dot(point=np.array([2.35*cos(thetas.get_value()).real-2.5,2.35*sin(thetas.get_value()).real -2, 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=WHITE))
        B = Dot(point=np.array([-2.5,-2,0]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=WHITE)
        D = Dot(point=np.array([-0.15, -2.0, 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=WHITE)
        xA = A.get_center()
        tA = Tex(r"$A$"  , font_size=18 , color = WHITE).move_to(np.array([xA[0]+0.4,xA[1]-0.4,0]))
        xB = B.get_center()
        tB = Tex(r"$B$"  , font_size=18 , color = WHITE).move_to(np.array([xB[0],xB[1]-0.4,0]))
        xD = D.get_center()
        tD = Tex(r"$D$"  , font_size=18 , color = WHITE).move_to(np.array([xD[0],xD[1]-0.4,0]))
        tC = Tex(r"$C$"  , font_size=18 , color = WHITE)
        tC.add_updater(lambda x : x.move_to(np.array([C.get_center()[0],C.get_center()[1]-0.4,0])))
        self.play(FadeIn(commomarm,sidearm,a3,txt2,B,A,C,D,tA,tB,tC,tD))
        self.wait(8)
        txt3 = Text("If the non-common arms BC and BD as shown in the figure forms a line.\n Then the two adjacent angles are called Linear Pair Of Angles " , line_spacing=1 ,  slant=ITALIC , font_size=18 , color = WHITE).shift(UP+RIGHT)
        txt3.to_edge(LEFT , buff=0.5)
        txt3.to_edge(UP , buff=1.5)
#
        self.play(FadeIn(txt3))
        self.play(thetas.animate.set_value(PI) , run_time = 2)

        txt4 = Text("Here Lines BC and BD forms a stright line CD" , line_spacing=1 ,  slant=ITALIC , font_size=18 , color = WHITE).shift(UP+RIGHT)
        txt4.to_edge(RIGHT,buff=0.5)
        txt4.to_edge(DOWN,buff=2)
        self.wait(8)
        self.play(FadeIn(txt4))
        self.wait(6)
class Concept3_4(Scene):
    def construct(self):
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)        
        
        txt1 = Text("Linear Pair Of Angles are a special case of Adjacent Angles" , line_spacing=1 , t2c={'[0:21]': BLUE } , slant=ITALIC , font_size=18 , color = WHITE)
        txt1.to_edge(UP , buff = 0.5)
        txt1.to_edge(LEFT , buff = 0.5)
        self.add(txt1)
        txt2 = Tex(r"Lets $\angle$ABC and $\angle$ABD be two adjacent angles with AB as the commom arm").set_color(RED).set_height(0.2)

        txt2.to_edge(DOWN , buff = 1)
        txt2.to_edge(LEFT , buff = 0.5)
        a1 = Vector( direction=[-2*(1.41),0,0]).set_color(color=[GREEN]).shift([-2.5,-2,0])
        a2 = Vector( direction=[2,2,0]).set_color(color=[YELLOW]).shift([-2.5,-2,0])
        a3 = Vector( direction=[2*(1.41),0,0]).set_color(color=[BLUE]).shift([-2.5,-2,0])

        # veca1 = 
        # veca2 = 
        thetac = ValueTracker(a2.get_angle()-a3.get_angle())
        thetas = ValueTracker(a1.get_angle()-a3.get_angle())

        commomarm = always_redraw(lambda : Vector(direction=np.array([2*1.41*cos(thetac.get_value()).real,2*1.41*sin(thetac.get_value()).real,0])).set_color(color=[RED]).shift([-2.5,-2,0]))
        sidearm = always_redraw(lambda : Vector(direction=np.array([2*1.41*cos(thetas.get_value()).real,2*1.41*sin(thetas.get_value()).real,0])).set_color(color=[RED]).shift([-2.5,-2,0]))
        C = Dot(point=np.array([-4.85, -2, 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=WHITE)
        A = always_redraw(lambda : Dot(point=np.array([2.35*cos(thetac.get_value()).real-2.5,2.35*sin(thetac.get_value()).real -2, 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=WHITE))
        B = Dot(point=np.array([-2.5,-2,0]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=WHITE)
        D = Dot(point=np.array([-0.15, -2.0, 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=WHITE)
        xC = C.get_center()
        tC = Tex(r"$C$"  , font_size=18 , color = WHITE).move_to(np.array([xC[0],xC[1]-0.4,0]))
        xB = B.get_center()
        tB = Tex(r"$B$"  , font_size=18 , color = WHITE).move_to(np.array([xB[0],xB[1]-0.4,0]))
        xD = D.get_center()
        tD = Tex(r"$D$"  , font_size=18 , color = WHITE).move_to(np.array([xD[0],xD[1]-0.4,0]))
        tA = Tex(r"$A$"  , font_size=18 , color = WHITE).move_to(np.array([A.get_center()[0]+0.4,A.get_center()[1]-0.4,0]))
        tA.add_updater(lambda x : x.move_to(np.array([A.get_center()[0]+0.4,A.get_center()[1]-0.4,0])))
        self.add(commomarm,sidearm,a3,txt2,B,A,C,D,tA,tB,tC,tD)
        txt3 = Text("If the non-common arms BC and BD as shown in the figure forms a line.\n Then the two adjacent angles are called Linear Pair Of Angles " , line_spacing=1 ,t2c={'[111:132]': BLUE } ,  slant=ITALIC , font_size=18 , color = WHITE).shift(UP+RIGHT)
        txt3.to_edge(LEFT , buff=0.5)
        txt3.to_edge(UP , buff=1.5)
        self.add(txt3)
        txt4 = Text("Here Lines BC and BD forms a stright line CD" , line_spacing=1 ,  slant=ITALIC , font_size=18 , color = WHITE).shift(UP+RIGHT)
        txt4.to_edge(RIGHT,buff=0.5)
        txt4.to_edge(DOWN,buff=2)
        self.add(txt4)
        self.wait(2)
        txt5 = Tex(r"Hence $\angle$CBD = 180$^{\circ}$"  , font_size=18 , color = WHITE).shift(UP+RIGHT)
        self.play(FadeIn(txt5))
        txt6 = Tex(r"  $\angle$ABC + $\angle$ABD = 180$^{\circ}$"   , font_size=18 , color = WHITE).shift(UP+RIGHT)
        txt6.to_edge(LEFT,buff=0.5)
        txt6.to_edge(DOWN,buff=3.3)

        self.play(FadeIn(txt6))
        angle1_1 = always_redraw(lambda : Arc(radius=0.4, start_angle=thetac.get_value(), angle=thetas.get_value()-thetac.get_value(), num_components=9, arc_center=np.array([-2.5,-2,0])))
        angle1_2 = always_redraw(lambda : Arc(radius=0.5,start_angle = thetac.get_value(), angle=thetas.get_value()-thetac.get_value(), num_components=9, arc_center=np.array([-2.5,-2,0])))
        angle2 = always_redraw(lambda : Arc(radius=0.8, start_angle=0, angle=thetac.get_value(), num_components=9, arc_center=np.array([-2.5,-2,0])))
        self.play(FadeIn(angle1_1,angle1_2,angle2))
        txt7 = Tex(r" $\angle$ABC"   , font_size=18 , color = WHITE).shift([-3.3,-1.8,0])
        txt8 = Tex(r"$\angle$ABD"   , font_size=18 , color = WHITE).shift([-1.3,-1.8,0])
        
        self.play(FadeIn(txt7,txt8))
        txt11 = always_redraw(lambda : Tex(" " + str((round((thetas.get_value()-thetac.get_value())*180/PI,2)))+ r"$^{\circ}$ " + r" \  + \  " + str(round((thetac.get_value())*180/PI,2)) + r"$^{\circ}$ " + r"\  = \ " + r"  180$^{\circ}$ "   , font_size=19 , color = WHITE).to_edge(LEFT,buff=0.5).to_edge(LEFT,buff=0.5))
        
        self.play(FadeIn(txt7,txt8,txt11))
        self.wait(6)
        self.play(thetac.animate.set_value((3*PI/4)-0.12) , run_time = 3)
        self.play(thetac.animate.set_value(0.35) , run_time = 3)
        self.wait(5)
        # txt11 = always_redraw(lambda : Tex(r ""   , font_size=18 , color = WHITE).shift(UP+RIGHT))
        # txt12 = always_redraw(lambda : Tex(r""   , font_size=18 , color = WHITE).shift(UP+RIGHT))

        txt12 = always_redraw(lambda : Vector(direction=np.array([2*1.41*cos(thetac.get_value()).real,2*1.41*sin(thetac.get_value()).real,0])).set_color(color=[RED]))

        
class Concept3_5(Scene):
    def construct(self):        
        title = MathTex("Vertically \ Opposite \ Angles").set_color_by_gradient(GREEN, PINK).set_height(0.8)
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        title.to_edge(UP, buff=1)
        self.add(logo)        
        self.play(FadeIn(title))
        
        txt1 = Text("Vertically Opposite Angles are formed when two lines intersect each other." , line_spacing=1 ,t2c={'[0:27]': GREEN } ,  slant=ITALIC , font_size=18 , color = WHITE).shift(UP+RIGHT)
        txt1.to_edge(LEFT,buff = 0.5)
        self.play(FadeIn(txt1))
        self.wait(5)
        self.remove(title)
        self.play(txt1.animate.shift(+UP*2.5),run_time =2)
        a1 = Vector(direction=np.array([1.5,1.5,0])).set_color(color=[RED])
        a2 = Vector(direction=np.array([-1.5,-1.5,0])).set_color(color=[RED])
        b1 = Vector(direction=np.array([-1.5,1.5,0])).set_color(color=[RED])
        b2 = Vector(direction=np.array([1.5,-1.5,0])).set_color(color=[RED])
        # print(a2.get_angle())
        thetaa1 = ValueTracker(a1.get_angle())
       
        am1 = always_redraw(lambda : Vector(direction=np.array([1.5*1.41*cos(thetaa1.get_value()).real,1.5*1.41*sin(thetaa1.get_value()).real,0])).set_color(color=[RED]))
        am2 = always_redraw(lambda : Vector(direction=np.array([1.5*1.41*cos((PI +thetaa1.get_value())).real,1.5*1.41*sin((PI +thetaa1.get_value())).real,0])).set_color(color=[RED]))
        bm1 = always_redraw(lambda : Vector(direction=np.array([1.5*1.41*cos((PI - thetaa1.get_value())).real,1.5*1.41*sin((PI - thetaa1.get_value())).real,0])).set_color(color=[RED]))
        bm2 = always_redraw(lambda : Vector(direction=np.array([1.5*1.41*cos((-thetaa1.get_value())).real,1.5*1.41*sin((-thetaa1.get_value())).real,0])).set_color(color=[RED]))
        txt2 = Text("Let's say two lines AB and CD intersect at a point O then " , line_spacing=1  ,  slant=ITALIC , font_size=18 , color = WHITE).shift(UP+RIGHT)
        txt2.to_edge(UP, buff=1.2)
        txt2.to_edge(LEFT, buff=0.5)
# 
        A = always_redraw(lambda : Dot(point=np.array([1.5*cos(thetaa1.get_value()).real,1.5*sin(thetaa1.get_value()).real , 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=PINK))
        B = always_redraw(lambda : Dot(point=np.array([1.5*cos((PI +thetaa1.get_value())).real,1.5*sin((PI +thetaa1.get_value())).real , 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=PINK))
        C = always_redraw(lambda : Dot(point=np.array([1.5*cos((PI - thetaa1.get_value())).real,1.5*sin((PI - thetaa1.get_value())).real , 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=PINK))
        D = always_redraw(lambda : Dot(point=np.array([1.5*cos((-thetaa1.get_value())).real,1.5*sin((-thetaa1.get_value())).real , 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=PINK))
        O = Dot(point=np.array([0,0 , 0.]), radius=0.08, stroke_width=0, fill_opacity=1.0, color=PINK)
# 
        tA = Tex(r"$A$"  , font_size=18 , color = PINK).move_to(np.array([A.get_center()[0]+0.3,A.get_center()[1]-0.3,0]))
        # 
        tA.add_updater(lambda x : x.move_to(np.array([A.get_center()[0]+0.3,A.get_center()[1]-0.3,0])))
        # 
        tB = Tex(r"$B$"  , font_size=18 , color = PINK).move_to(np.array([B.get_center()[0]-0.3,B.get_center()[1]+0.3,0]))
        # 
        tB.add_updater(lambda x : x.move_to(np.array([B.get_center()[0]-0.3,B.get_center()[1]+0.3,0])))
        # 
        tC = Tex(r"$C$"  , font_size=18 , color = PINK).move_to(np.array([C.get_center()[0]+0.3,C.get_center()[1]+0.3,0]))
        # 
        tC.add_updater(lambda x : x.move_to(np.array([C.get_center()[0]+0.3,C.get_center()[1]+0.3,0])))
        # 
        tD = Tex(r"$D$"  , font_size=18 , color = PINK).move_to(np.array([D.get_center()[0]-0.3,D.get_center()[1]-0.3,0]))
        # 
        tD.add_updater(lambda x : x.move_to(np.array([D.get_center()[0]-0.3,D.get_center()[1]-0.3,0])))
        # 
        tO = Tex(r"$O$"  , font_size=18 , color = PINK).move_to(np.array([O.get_center()[0]-0.8,O.get_center()[1],0]))
        angle1_1 = always_redraw(lambda :Arc(radius=0.4, start_angle=thetaa1.get_value(), angle=-2*thetaa1.get_value(), num_components=9, arc_center=np.array([0,0,0])))
        angle1_2 = always_redraw(lambda :Arc(radius=0.5, start_angle=thetaa1.get_value(), angle=-2*thetaa1.get_value(), num_components=9, arc_center=np.array([0,0,0])))
# 
        angle2 = always_redraw(lambda :Arc(radius=0.8, start_angle=thetaa1.get_value(), angle=(PI - 2*thetaa1.get_value()), num_components=9, arc_center=np.array([0,0,0])))
# 
        angle3_1 = always_redraw(lambda :Arc(radius=0.4, start_angle=(PI - thetaa1.get_value()), angle=2*thetaa1.get_value(), num_components=9, arc_center=np.array([0,0,0])))
        angle3_2 = always_redraw(lambda :Arc(radius=0.5, start_angle=(PI - thetaa1.get_value()), angle=2*thetaa1.get_value(), num_components=9, arc_center=np.array([0,0,0])))
# 
        angle4 = always_redraw(lambda :Arc(radius=0.8, start_angle=PI + thetaa1.get_value(), angle= (PI - 2*thetaa1.get_value()) , num_components=9, arc_center=np.array([0,0,0])))
        self.play(FadeIn(am1,am2,bm1,bm2,txt2,A,B,C,D,tA,tB,tC,tD,O,tO,angle2,angle1_1,angle1_2,angle3_1,angle3_2,angle4))
        self.wait(8)
        txt3 = Text("Then two pairs of Vertically Opposite angles are formed." , line_spacing=1 ,t2c={'[18:55]': GREEN } ,  slant=ITALIC , font_size=18 , color = WHITE).shift(UP+RIGHT)
        txt3.to_edge(DOWN,buff=0.5)
        txt3.to_edge(LEFT,buff=0.5)
        self.play(FadeIn(txt3))
        self.wait(4)
        txt4 = Tex(r"One such pair is $\angle$AOC and $\angle$BOD "  , font_size=18 , color = RED)
        txt4.to_edge(LEFT,buff=0.5)
        txt4_1 = always_redraw(lambda : Tex(r"$\angle$AOC"+" = " +  str(round(((PI - thetaa1.get_value()) - thetaa1.get_value())*180/PI,2)) , font_size=18 , color = RED).shift(2.2*UP))
        txt4_2 = always_redraw(lambda : Tex(r"$\angle$BOD"+" = " +  str(round(((PI - thetaa1.get_value()) - thetaa1.get_value())*180/PI,2)) , font_size=18 , color = RED).shift(2.2*DOWN))
        self.play(FadeIn(txt4_1,txt4_2,txt4))
        self.wait(3)
        txt5 = Tex(r"The other pair is $\angle$AOD and $\angle$BOC "  , font_size=18 , color = BLUE)
        txt5.to_edge(RIGHT,buff=0.5)
        txt5_1 = always_redraw(lambda : Tex(r"$\angle$AOD"+" = " +  str(round(((thetaa1.get_value())+thetaa1.get_value())*180/PI,2)) , font_size=18 , color = BLUE).shift(2.8*RIGHT))
        txt5_2 = always_redraw(lambda : Tex(r"$\angle$BOC"+" = " +  str(round(((thetaa1.get_value())+thetaa1.get_value())*180/PI,2))  , font_size=18 , color = BLUE).shift(2.8*LEFT))
        self.play(FadeIn(txt5_1,txt5_2,txt5))
        self.wait(3)

        txt6 = Tex(r"The pair $\angle$AOC and $\angle$BOD are equal."  , font_size=18 , color = YELLOW).shift(UP+RIGHT)
        txt6.to_edge(LEFT,buff=1)
        txt6.to_edge(DOWN,buff=2.5)
        
        self.play(FadeIn(txt6))
        self.wait(5)
        self.play(thetaa1.animate.set_value(1.2) , run_time = 3)
        # self.play(thetaa1.animate.set_value(PI) ,thetaa2.animate.set_value(PI),thetab1.animate.set_value(PI),thetab2.animate.set_value(), run_time = 2)

        txt7 = Tex(r"Similarly angles $\angle$AOD and $\angle$BOC are also equal"  , font_size=18 , color = YELLOW).shift(UP+RIGHT)
        txt7.to_edge(RIGHT,buff=1)
        txt7.to_edge(DOWN,buff=2.5)
        self.play(FadeIn(txt7))
        self.play(thetaa1.animate.set_value(0.35) , run_time = 3)

        self.wait(5)
        


run1 =  Concept3_5()
run1.construct()     