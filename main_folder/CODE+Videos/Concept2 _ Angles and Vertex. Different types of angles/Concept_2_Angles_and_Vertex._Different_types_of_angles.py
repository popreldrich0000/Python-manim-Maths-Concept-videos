from cmath import cos, sin
from math import fabs 
import numpy as np
import random
from curses.textpad import rectangle
from tkinter import CENTER, Y
from turtle import circle, right
from manim import *

# class Tute4(Scene):
#     def construct(self):

#         title = MathTex("Angles \ and \ Vertex").set_color_by_gradient(GREEN, PINK).set_height(0.8)
#         logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
#         title.to_edge(UP, buff=1)
   
class Concept2_1(ThreeDScene):
    def construct(self):
        title = MathTex("Angles \ and \ Vertex").set_color_by_gradient(GREEN, PINK).set_height(0.8)
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        title.to_edge(UP, buff=1)
        self.add(logo)        
        self.play(FadeIn(title))
        self.wait(5)
        defination = Text("An Angle is a figure that is formed when two rays share a commom endpoint. \n The common end point is called the Vertex of the Angle" , line_spacing=1 , t2c={'[3:8]': BLUE , '[111:118]':RED} ,  slant=ITALIC , font_size=18 , color = WHITE)

        defination.to_edge( UP , buff = 3)
        defination.to_edge( LEFT , buff = 0.5)
        self.play(FadeIn(defination))
        self.wait(10)
        self.remove(title)
        self.play(defination.animate.shift(+UP*2.5),run_time =2)
        self.wait(5)
class Concept2_2(ThreeDScene):
    def construct(self):
        def get_points(v2):
            r = 0.5
            v1 = np.array([-1,1,1])
            v3 = np.cross(np.cross(v1,v2),v1)
            v1r = v1*r / np.sqrt(np.sum(v1**2))
            v2r = v2*r / np.sqrt(np.sum(v2**2))
            v3r = v3*r / np.sqrt(np.sum(v3**2))
            theta = np.arccos(np.dot(v1,v2)/(np.sqrt(np.sum(v2**2))*np.sqrt(np.sum(v1**2))))
            thetas = theta/32
          
            q1 = np.zeros([33,3]) 
            
            for i in range(33):
                q1[i] = v1r*cos(thetas*i) + v3r*sin(thetas*i)
            
            
            
          
            return q1 
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add_fixed_in_frame_mobjects(logo)
        self.add(logo)        
        defination = Text("An Angle is a figure that is formed when two rays share a commom endpoint. \n The common end point is called the Vertex of the Angle" , line_spacing=1 , t2c={'[3:8]': BLUE , '[111:118]':RED} ,  slant=ITALIC , font_size=18 , color = WHITE)
        defination.to_edge( UP , buff = 0.5)
        defination.to_edge( LEFT , buff = 0.5)
        # self.add(defination)
        self.add_fixed_in_frame_mobjects(defination)
        axes = ThreeDAxes(
            x_range=[-6,6,1],
            y_range=[-6,6,1],
            z_range=[-6,6,1],
            x_length=8,
            y_length=6,
            z_length=6
        )
        self.set_camera_orientation(phi = 60*DEGREES, theta=30*DEGREES,distance = 5 )
        self.play(FadeIn(axes))
        
        self.wait(5)
        a2 = Arrow3D(start=[0,0,0], end=[2,-2,2]).set_color(color=[GREEN])
        a1 = Arrow3D(start=[0,0,0], end=[-2,2,2] ).set_color(color=[RED])
        l2 =  Line(start=[0,0,0], end=[2,-2,2], path_arc=None )
        self.play(FadeIn(a1,a2))
        q1 = get_points(l2.get_unit_vector())
        self.wait(10)
        q3 = np.zeros([33,3])
        pnts = np.concatenate([q1, q3, q1[0].reshape(1, 3)])
        # mfill = 
        # x = lambda a : 2*PI + a if a<0  else a 
        # angle = always_redraw(lambda : VMobject().set_points_as_corners(pnts).set_fill(GREEN, opacity=0.5))
        angle = VMobject().set_color(BLUE)
        angle.set_points_as_corners(pnts).set_fill(GREEN, opacity=0.5)
        vertex = Sphere(center=np.array([0., 0., 0.]), radius=0.1)
        vertex.set_color(RED)


        at1 = Arrow3D(start=[0.9,-0.9,0.4], end=[0.1,-0.1,0.07]).set_color(color=[RED])
        at2 = Arrow3D(start=[-1.5,1.5,1.0], end=[-0.2,0.2,0.5] ).set_color(color=[BLUE])
        txt1 = Text("This is an Angle" , line_spacing=1 , t2c={'[11:16]': BLUE } ,  slant=ITALIC , font_size=18 , color = WHITE)
        self.add_fixed_in_frame_mobjects(txt1)
        
        txt1.to_edge(DOWN*10)
        txt1.to_edge(RIGHT*5)
        self.play(FadeIn(txt1,angle,at2))
        self.wait(10)
        txt2 = Text("This is the Vertex formed by the two rays.", line_spacing=1 , t2c={'[12:18]': RED } ,  slant=ITALIC , font_size=18 , color = WHITE)
        self.add_fixed_in_frame_mobjects(txt2)

        txt2.to_edge(DOWN*8)
        txt2.to_edge(LEFT*0.5)
        self.play(FadeIn(txt2,vertex,at1))
        self.wait(10)
        self.remove(txt1,txt2,at1,at2)
        self.begin_ambient_camera_rotation(rate=0.9)
        self.wait(6.891)
        
        # txt3 = Text("As we can see the value of the Angle changes as we rotate the rays" , line_spacing=1 , t2c={'[32:37]': BLUE } ,  slant=ITALIC , font_size=18 , color = WHITE)
        
        # txt4 = Text("The Angle gets smaller as the two rays gets closer and bigger as they get further" , line_spacing=1 , t2c={'[11:16]': BLUE } ,  slant=ITALIC , font_size=18 , color = WHITE)
        # txt5 = Text("The two rays lie in a plane " , line_spacing=1 , t2c={'[11:16]': BLUE } ,  slant=ITALIC , font_size=18 , color = WHITE)
        # txt6 = Text("We catogorise Angles between two rays  based on the orentation of the rays" , line_spacing=1 , t2c={'[11:16]': BLUE } ,  slant=ITALIC , font_size=18 , color = WHITE)
        
        # Angle.from_three_points(UP, ORIGIN, LEFT)
        
                
        
        
        
        # self.play(Rotate(l2  ,  
        #               angle=PI*2,
        #               about_point=ORIGIN,
        #               rate_func=linear,
        # ),FadeIn(angle))
        
        
        # self.begin_ambient_camera_rotation(rate=0.9)
        # self.wait(2)
        # self.play(FadeIn(l1),run_timr=2)
        # self.wait(3)
        # self.stop_ambient_camera_rotation()
        # self.wait(4)
        # self.move_camera(phi=-48*DEGREES, theta=48*DEGREES,distance = 5 )
        # self.line_1_color =ORANGE
        # self.line_2_color =PINK
        # self.lines_size = 3.5
        # self.theta =PI/2
        # self.increment_theta =PI/2
        # self.final_theta =PI
        # self.radius =0.7
        # self.radius_color = YELLOW
        # theta  = ValueTracker(0)
        # line_2 =  always_redraw(lambda :  Line(ORIGIN,RIGHT*self.lines_size,color=self.line_1_color)).rotate(0.001,about_point=ORIGIN)
        # line_1 = Line(ORIGIN,RIGHT*self.lines_size,color=self.line_2_color)
        # self.add(line_1)
        
        # x = lambda a : 2*PI + a if a<0  else a 
        # # angle = always_redraw(lambda : Arc(
        # #         radius=0.7,
        # #         start_angle=line_1.get_angle(),
        # #         angle = x(line_2.get_angle()) ,
        # #         color= YELLOW,
        # #         fill_color=YELLOW, fill_opacity=0.6
                
        # # ))
        # angle = always_redraw(lambda : AnnularSector(inner_radius=0, outer_radius=0.5,
        #  angle=x(line_2.get_angle()),
        #  start_angle=line_1.get_angle(),
        #  fill_opacity=0.5,
        #  color=GREEN)
                
        # )
        # self.add(angle)
        # self.play(LaggedStart(Rotate(l2  ,  
        #               angle=PI*2,
        #               axis = np.cross(np.array([2,-2,2]) ,np.array([-2,2,2]) ),
        #               about_point=ORIGIN,
        #               rate_func=linear,
        #               runtime = 5
        # ))
        
        # )

class Concept2_3(ThreeDScene):
    def construct(self):

        def get_points(v2):
            r = 0.5
            v1 = np.array([-1,1,1])
            v3 = np.cross(np.cross(v1,v2),v1)
            v1r = v1*r / np.sqrt(np.sum(v1**2))
            v2r = v2*r / np.sqrt(np.sum(v2**2))
            v3r = v3*r / np.sqrt(np.sum(v3**2))
            theta = np.arccos(np.dot(v1,v2)/(np.sqrt(np.sum(v2**2))*np.sqrt(np.sum(v1**2))))
            thetas = theta/32
          
            q1 = np.zeros([33,3]) 
            
            for i in range(33):
                q1[i] = v1r*cos(thetas*i) + v3r*sin(thetas*i)
            
            
            
          
            return q1 
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add_fixed_in_frame_mobjects(logo)
        self.add(logo)        

        self.add(logo)        
        axes = ThreeDAxes(
            x_range=[-6,6,1],
            y_range=[-6,6,1],
            z_range=[-6,6,1],
            x_length=8,
            y_length=6,
            z_length=6
        )
        self.set_camera_orientation(phi = 60*DEGREES, theta=30*DEGREES,distance = 5 )
        self.add(axes)
        
        a2 = Arrow3D(start=[0,0,0], end=[2,-2,2]).set_color(color=[GREEN])
        a1 = Arrow3D(start=[0,0,0], end=[-2,2,2] ).set_color(color=[RED])
        l2 =  Line(start=[0,0,0], end=[2,-2,2], path_arc=None )
        l3 = np.cross(np.cross(l2.get_unit_vector(), [-1,1,1]),l2.get_unit_vector())
        self.add(a1,a2)
        # txt3 = Text("As we can see the value of the Angle changes as we rotate the rays" ,  slant=ITALIC , font_size=18 , color = WHITE)
        # txt3.to_edge(buff=LEFT*4)

        # txt3.to_edge(buff=UP*2)
        
        q1 = get_points(l3)
        q3 = np.zeros([33,3])
        pnts = np.concatenate([q1, q3, q1[0].reshape(1, 3)])
        # mfill = 
        # x = lambda a : 2*PI + a if a<0  else a 
        # angle = always_redraw(lambda : VMobject().set_points_as_corners(pnts).set_fill(GREEN, opacity=0.5))
        angle_s = VMobject().set_color(BLUE)
        angle_s.set_points_as_corners(pnts).set_fill(GREEN, opacity=0.5)
        
        txt3 = Text("The Angle gets smaller as the two rays gets closer and Large as they get further" , line_spacing=1 ,  slant=ITALIC , font_size=18 , color = WHITE)
        self.add_fixed_in_frame_mobjects(txt3)

        txt3.to_edge(LEFT , buff = 2)

        txt3.to_edge(UP , buff = 0.7)
        self.play(FadeIn(txt3))
        self.wait(1)
        self.play(Rotate(a2,  
                      angle=PI/2,
                      about_point=ORIGIN,
                      rate_func=linear,
                      axis = np.cross(l2.get_unit_vector(),np.array([-1,1,1]))
        ))
        
        
        self.wait(2)
        stxt = Text("Small Angle" , line_spacing=1 ,  slant=ITALIC , font_size=18 , color = WHITE).shift(LEFT*2)
        self.add_fixed_in_frame_mobjects(stxt)

        self.play(FadeIn(angle_s,stxt ))
        self.wait(8)
        self.remove(angle_s,stxt)
        q1 = get_points(l2.get_unit_vector())
        q3 = np.zeros([33,3])
        pntb = np.concatenate([q1, q3, q1[0].reshape(1, 3)])
        angle_b = VMobject().set_color(BLUE)
        

        angle_b.set_points_as_corners(pntb).set_fill(GREEN, opacity=0.5)
        self.play(Rotate(a2,  
                      angle=-PI/2,
                      about_point=ORIGIN,
                      rate_func=linear,
                      axis = np.cross(l2.get_unit_vector(),np.array([-1,1,1]))
        ))
        
        
        self.wait(2)
        btxt = Text("Large Angle" , line_spacing=1 ,  slant=ITALIC , font_size=18 , color = WHITE).shift(LEFT*2)
        self.add_fixed_in_frame_mobjects(btxt)
        self.play(FadeIn(angle_b),FadeIn(btxt))
        self.wait(8)
        self.remove(angle_b, btxt)

        
        # txt5 = Text("The two rays lie in a plane " , line_spacing=1 , t2c={'[11:16]': BLUE } ,  slant=ITALIC , font_size=18 , color = WHITE)
        # txt6 = Text("We catogorise Angles between two rays  based on the orentation of the rays" , line_spacing=1 , t2c={'[11:16]': BLUE } ,  slant=ITALIC , font_size=18 , color = WHITE)
        
        
class Concept2_4(Scene):
    def construct(self):
        theta = ValueTracker(3*PI/4)
        title = MathTex("Different  \ Types \ of \ Angles").set_color_by_gradient(GREEN, PINK).set_height(0.8)
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        title.to_edge(UP, buff=1)
        self.add(logo)        
        self.play(FadeIn(title))
        self.wait(5)
        txt1 = Text("We catogorise Angles between two rays based on the orentation of the rays" , line_spacing=1   ,  slant=ITALIC , font_size=18 , color = WHITE)

        txt1.to_edge( UP , buff = 3)
        txt1.to_edge( LEFT , buff = 0.5)
        self.play(FadeIn(txt1))
        self.wait(5)
        self.remove(title)
        self.play(txt1.animate.shift(+UP*2.5),run_time =2)
        self.wait(2)        
        a1 = always_redraw(lambda : Vector(direction=np.array([1.5*1.41*cos(theta.get_value()).real,1.5*1.41*sin(theta.get_value()).real,0])).set_color(color=[RED]))
        a2 = Vector(direction=[1.41*1.5,0,0]).set_color(color=[RED])
        angle = always_redraw(lambda : AnnularSector(inner_radius=0, outer_radius=0.5, angle = theta.get_value()  , start_angle=0, fill_opacity=0.5, color = RED,stroke_width=0))
        # self.play(FadeIn(angle),FadeIn(a2),FadeIn(a1))
          
        angval = always_redraw(lambda :  Text(str(abs(round((180*(theta.get_value()))/PI,2)))+'°').set_height(0.3).shift(RIGHT*3))
        self.play(LaggedStart(FadeIn(a1) ,FadeIn(angle) ,FadeIn(a2)),FadeIn(angval))
        self.play(theta.animate.set_value(-PI/4) , run_time = 3)
        self.wait(2)
        self.play(theta.animate.set_value(PI/2) , run_time = 3)
        self.wait(2)
        self.remove(txt1)
        txt2 = Text("We can classify Angles based on the range in which they lie" , line_spacing=1   ,  slant=ITALIC , font_size=18 , color = WHITE)
        txt2.to_edge( UP , buff = 0.5   )
        txt2.to_edge( LEFT , buff = 0.5)
        self.play(FadeIn(txt2))
        self.wait(3)
class Concept2_5(Scene):
    def construct(self):
        # ACUTE ANGLE 
        logo = ImageMobject("assets/img/Vizlogo.png").scale(0.08).shift(RIGHT*6.5+UP*3.5)
        self.add(logo)
        txt1 = Text("We can classify Angles based on the range in which they lie" , line_spacing=1   ,  slant=ITALIC , font_size=18 , color = WHITE)
        txt1.to_edge( UP , buff = 0.5   )
        txt1.to_edge( LEFT , buff = 0.5)
        acup1 = Vector(direction=np.array([1.5*1.41*cos(PI/2).real,1.5*1.41*sin(PI/2).real,0])).set_color(color=[RED])
        acup2 = Vector(direction=[1.41*1.5,0,0]).set_color(color=[RED])
        angval_acup = Text(str(abs(round((180*(PI/2))/PI,2)))+'°').set_height(0.3).shift(RIGHT*3)
        angleacup = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI/2  , start_angle=0, color = RED,fill_opacity=0.5, stroke_width=0)
        self.add(acup1,acup2,angval_acup,angleacup,txt1)
        self.wait(2)

        thetacu = ValueTracker(PI/2)
        
        acu1 = always_redraw(lambda : Vector(direction=np.array([1.5*1.41*cos(thetacu.get_value()).real,1.5*1.41*sin(thetacu.get_value()).real,0])).set_color(color=[RED]))
        acu2 = Vector(direction=[1.41*1.5,0,0]).set_color(color=[RED])
        angleacu = always_redraw(lambda : AnnularSector(inner_radius=0, outer_radius=0.5, angle = thetacu.get_value()  , start_angle=0, color = RED,fill_opacity=0.5, stroke_width=0))
        
        angval_acu = always_redraw(lambda :  Text(str(abs(round((180*(thetacu.get_value()))/PI,2)))+'°').set_height(0.3).shift(RIGHT*3))
        self.add(angleacu)
        self.play(LaggedStart(FadeIn(acu2)  ,FadeIn(acu1)),FadeIn(angval_acu))
        self.remove(acup1,acup2,angval_acup,angleacup)
        self.wait(2)
    
        ###############
        self.play(thetacu.animate.set_value(0) , run_time = 3)
        txt4 = Text("Acute angle Lies between 0° & 90°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = RED).shift(DOWN*0.75 + RIGHT*2)
        self.play(FadeIn(txt4))
        self.wait(5)

        self.play(thetacu.animate.set_value(PI/2) , run_time = 3)
        self.wait(3)
        self.play(thetacu.animate.set_value(PI/4) , run_time = 3)
        self.wait(3)
        self.remove(angval_acu)
        txt_theta = Tex(r"$\Theta$").set_color(RED).set_height(0.2).shift(RIGHT*0.8+UP*0.3)
        txt3 = Tex(r"$0^{\circ}$ < $\Theta$ < 90$^{\circ}$ ").set_color(RED).set_height(0.2).shift(DOWN*1.3 + RIGHT*2)
        self.play(FadeIn(txt_theta))
        list_acute  = Group(acu1,acu2,angleacu,txt4,txt_theta,txt3)

        # self.play(list_acute.set_color(RED))
        # self.play(list_acute.animate.set_color(RED))

        self.play(list_acute.animate.shift(LEFT*6.5+UP*1),run_time = 4)
        
class Concept2_6(Scene):
    def construct(self):        
        #RIGHT ANGLE
        txt1 = Text("We can classify Angles based on the range in which they lie" , line_spacing=1   ,  slant=ITALIC , font_size=18 , color = WHITE)
        txt1.to_edge( UP , buff = 0.5   )
        txt1.to_edge( LEFT , buff = 0.5)
        txt4 = Text("Acute angle Lies between 0° & 90°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = RED).shift(UP*0.25 + LEFT*4.5)

        acup1 = Vector(direction=np.array([1.5*1.41*cos(PI/4).real,1.5*1.41*sin(PI/4).real,0])).set_color(color=[RED]).shift(LEFT*6.5+UP*1)
        acup2 = Vector(direction=[1.41*1.5,0,0]).set_color(color=[RED]).shift(LEFT*6.5+UP*1)
        angleacup = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI/4 , start_angle=0, color = RED,fill_opacity=0.5, stroke_width=0).shift(LEFT*6.5+UP*1)
        txt_theta = Tex(r"$\Theta$").set_color(RED).set_height(0.2).shift(LEFT*5.7+UP*1.3)
        txt3 = Tex(r"$0^{\circ}$ < $\Theta$ < 90$^{\circ}$ ").set_color(RED).set_height(0.2).shift(DOWN*0.3 + LEFT*4.5)
        self.add(txt1,acup1,acup2,angleacup,txt4,txt3,txt_theta)
        self.wait(2)
        theta_r = ValueTracker(PI/4)
        r1 = always_redraw(lambda : Vector(direction=np.array([1.5*1.41*cos(theta_r.get_value()).real,1.5*1.41*sin(theta_r.get_value()).real,0])).set_color(color=[GREEN]))
        r2 = Vector(direction=[1.5*1.41,0,0]).set_color(color=[GREEN])
        angler = always_redraw(lambda : AnnularSector(inner_radius=0, outer_radius=0.5, angle = theta_r.get_value()  , start_angle=0, color = GREEN,fill_opacity=0.5, stroke_width=0))
          
        angval_r = always_redraw(lambda :  Text(str(abs(round((180*(theta_r.get_value()))/PI,2)))+'°').set_height(0.3).shift(RIGHT*3))
        
        
        self.play(LaggedStart(FadeIn(r1) ,FadeIn(angler) ,FadeIn(r2)),FadeIn(angval_r))
        self.play(theta_r.animate.set_value(PI/2) , run_time = 3)
        
    
        txt5 = Text("Right angle is exactly 90°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = GREEN).shift(DOWN*0.75 + RIGHT*1.5)
        self.play(FadeIn(txt5))
        self.wait(5)
        txt_thetar = Tex(r"$\Theta$").set_color(GREEN).set_height(0.2).shift(RIGHT*0.8+UP*0.3)
        txt3r = Tex(r" $\Theta$ = 90$^{\circ}$ ").set_color(GREEN).set_height(0.2).shift(DOWN*1.3 + RIGHT*2)
        self.play(FadeIn(txt_thetar,txt3r))
        self.remove(angval_r)
        list_right  = Group(r1,r2,angler,txt5,txt_thetar,txt3r)
        self.play(list_right.animate.shift(LEFT*1.4+UP*1),run_time = 4)
        

class Concept2_7(Scene):
    def construct(self):  

        txt1 = Text("We can classify Angles based on the range in which they lie" , line_spacing=1   ,  slant=ITALIC , font_size=18 , color = WHITE)
        txt1.to_edge( UP , buff = 0.5   )
        txt1.to_edge( LEFT , buff = 0.5)
        txt4 = Text("Acute angle Lies between 0° & 90°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = RED).shift(UP*0.25 + LEFT*4.5)

        acup1 = Vector(direction=np.array([1.5*1.41*cos(PI/4).real,1.5*1.41*sin(PI/4).real,0])).set_color(color=[RED]).shift(LEFT*6.5+UP*1)
        acup2 = Vector(direction=[1.41*1.5,0,0]).set_color(color=[RED]).shift(LEFT*6.5+UP*1)
        angleacup = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI/4 , start_angle=0, color = RED,fill_opacity=0.5, stroke_width=0).shift(LEFT*6.5+UP*1)
        txt_theta = Tex(r"$\Theta$").set_color(RED).set_height(0.2).shift(LEFT*5.7+UP*1.3)
        txt3 = Tex(r"$0^{\circ}$ < $\Theta$ < 90$^{\circ}$ ").set_color(RED).set_height(0.2).shift(DOWN*0.3 + LEFT*4.5)
        self.add(txt1,acup1,acup2,angleacup,txt4,txt3,txt_theta)
        
       
        txt5 = Text("Right angle is exactly 90°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = GREEN).shift(UP*0.25 + RIGHT*0.1)

        r1 = Vector(direction=np.array([1.5*1.41*cos(PI/2).real,1.5*1.41*sin(PI/2).real,0])).set_color(color=[GREEN]).shift(LEFT*1.4+UP*1)
        r2 = Vector(direction=[1.41*1.5,0,0]).set_color(color=[GREEN]).shift(LEFT*1.4+UP*1)
        anglerp = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI/2 , start_angle=0, color = GREEN,fill_opacity=0.5, stroke_width=0).shift(LEFT*1.4+UP*1)
        txt_thetar = Tex(r"$\Theta$").set_color(GREEN).set_height(0.2).shift(LEFT*0.6+UP*1.3)
        txt3r = Tex(r" $\Theta$ = 90$^{\circ}$ ").set_color(GREEN).set_height(0.2).shift(DOWN*0.3 + RIGHT*0.6)
        self.add(r1,r2,anglerp,txt_thetar,txt3r,txt5)
        self.wait(2)
        # OBTUSE ANGLE
        theta_b = ValueTracker(PI/2)
        ob1 = always_redraw(lambda : Vector(direction=np.array([1.5*1.41*cos(theta_b.get_value()).real,1.5*1.41*sin(theta_b.get_value()).real,0])).shift(RIGHT*4+UP*1).set_color(color=[BLUE]))
        ob2 = Vector(direction=[1.5*1.41,0,0]).set_color(color=[BLUE]).shift(RIGHT*4+UP*1)
        angleob = always_redraw(lambda : AnnularSector(inner_radius=0, outer_radius=0.5, angle = theta_b.get_value()  , start_angle=0, color = BLUE,fill_opacity=0.5, stroke_width=0).shift(RIGHT*4+UP*1))
        angval_ob = always_redraw(lambda :  Text(str(abs(round((180*(theta_b.get_value()))/PI,2)))+'°').set_height(0.3).shift(RIGHT*4+DOWN*0.3))
        
        self.play(LaggedStart(FadeIn(ob1) ,FadeIn(ob2) ,FadeIn(angval_ob)),FadeIn(angleob))
        self.play(theta_b.animate.set_value(PI) , run_time = 3)
        txt6 = Text("Obtuse angle Lies between 90° and 180°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = BLUE).shift(UP*0.25 )
        txt6.to_edge(RIGHT, buff=0.5)
        self.play(FadeIn(txt6))
        self.wait(5)
        self.play(theta_b.animate.set_value(3*PI/4) , run_time = 3)
        self.wait(6)
        self.remove(angval_ob)
        txt_thetaop = Tex(r"$\Theta$").set_color(BLUE).set_height(0.2).shift(RIGHT*4.8+UP*1.3)
        txt3op = Tex(r"$90^{\circ}$ < $\Theta$ < 180$^{\circ}$ ").set_color(BLUE).set_height(0.2).shift(RIGHT*4+DOWN*0.3)
        self.play(FadeIn(txt_thetaop),FadeIn(txt3op))
        self.wait(8)
class Concept2_8(Scene):
    def construct(self):  

        txt1 = Text("We can classify Angles based on the range in which they lie" , line_spacing=1   ,  slant=ITALIC , font_size=18 , color = WHITE)
        txt1.to_edge( UP , buff = 0.5   )
        txt1.to_edge( LEFT , buff = 0.5)
        txt4 = Text("Acute angle Lies between 0° & 90°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = RED).shift(UP*0.25 + LEFT*4.5)

        acup1 = Vector(direction=np.array([1.5*1.41*cos(PI/4).real,1.5*1.41*sin(PI/4).real,0])).set_color(color=[RED]).shift(LEFT*6.5+UP*1)
        acup2 = Vector(direction=[1.41*1.5,0,0]).set_color(color=[RED]).shift(LEFT*6.5+UP*1)
        angleacup = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI/4 , start_angle=0, color = RED,fill_opacity=0.5, stroke_width=0).shift(LEFT*6.5+UP*1)
        txt_theta = Tex(r"$\Theta$").set_color(RED).set_height(0.2).shift(LEFT*5.7+UP*1.3)
        txt3 = Tex(r"$0^{\circ}$ < $\Theta$ < 90$^{\circ}$ ").set_color(RED).set_height(0.2).shift(DOWN*0.3 + LEFT*4.5)
        self.add(txt1,acup1,acup2,angleacup,txt4,txt3,txt_theta)
        
       
        txt5 = Text("Right angle is exactly 90°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = GREEN).shift(UP*0.25 + RIGHT*0.1)

        r1 = Vector(direction=np.array([1.5*1.41*cos(PI/2).real,1.5*1.41*sin(PI/2).real,0])).set_color(color=[GREEN]).shift(LEFT*1.4+UP*1)
        r2 = Vector(direction=[1.41*1.5,0,0]).set_color(color=[GREEN]).shift(LEFT*1.4+UP*1)
        anglerp = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI/2 , start_angle=0, color = GREEN,fill_opacity=0.5, stroke_width=0).shift(LEFT*1.4+UP*1)
        txt_thetar = Tex(r"$\Theta$").set_color(GREEN).set_height(0.2).shift(LEFT*0.6+UP*1.3)
        txt3r = Tex(r" $\Theta$ = 90$^{\circ}$ ").set_color(GREEN).set_height(0.2).shift(DOWN*0.3 + RIGHT*0.6)
        self.add(r1,r2,anglerp,txt_thetar,txt3r,txt5)

        txt6 = Text("Obtuse angle Lies between 90° and 180°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = BLUE).shift(UP*0.25 )
        txt6.to_edge(RIGHT, buff=0.5)
        
        ob1  = Vector(direction=np.array([1.5*1.41*cos(3*PI/4).real,1.5*1.41*sin(3*PI/4).real,0])).shift(RIGHT*4+UP*1).set_color(color=[BLUE])
        ob2 = Vector(direction=[2*1.41,0,0]).set_color(color=[BLUE]).shift(RIGHT*4+UP*1)
        angleob = AnnularSector(inner_radius=0, outer_radius=0.5, angle = 3*PI/4  , start_angle=0, color = BLUE,fill_opacity=0.5, stroke_width=0).shift(RIGHT*4+UP*1)
        txt_thetaop = Tex(r"$\Theta$").set_color(BLUE).set_height(0.2).shift(RIGHT*4.8+UP*1.3)
        txt3op = Tex(r"$90^{\circ}$ < $\Theta$ < 180$^{\circ}$ ").set_color(BLUE).set_height(0.2).shift(RIGHT*4+DOWN*0.3)
        self.add(ob1,ob2,angleob,txt_thetaop,txt3op,txt6)
        self.wait(2)
        theta_s = ValueTracker(3*PI/4)
        s1 = always_redraw(lambda : Vector(direction=np.array([1.5*1.41*cos(theta_s.get_value()).real,1.5*1.41*sin(theta_s.get_value()).real,0])).shift(LEFT*2+DOWN*3).set_color(color=[YELLOW]))
        s2 = Vector(direction=[1.5*1.41,0,0]).set_color(color=[YELLOW]).shift(LEFT*2+DOWN*3)
        angles = always_redraw(lambda : AnnularSector(inner_radius=0, outer_radius=0.5, angle = theta_s.get_value()  , start_angle=0, color = YELLOW,fill_opacity=0.5, stroke_width=0).shift(LEFT*2+DOWN*3))
          
        angval_s = always_redraw(lambda :  Text(str(abs(round((180*(theta_s.get_value()))/PI,2)))+'°').set_height(0.3).shift(LEFT*5+DOWN*3))
 

        
        self.play(LaggedStart(FadeIn(s1) ,FadeIn(angles) ,FadeIn(s2)),FadeIn(angval_s))
        self.play(theta_s.animate.set_value(PI) , run_time = 3)
        
    
        txt5 = Text("Straight angle is exactly 180°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = YELLOW)
        txt5.to_edge(LEFT , buff= 3.5)
        txt5.to_edge(DOWN , buff= 0.2)

        self.play(FadeIn(txt5))
        self.wait(5)
        txt_thetas = Tex(r"$\Theta$").set_color(YELLOW).set_height(0.2).shift(LEFT*1.5+DOWN*2.5)
        txt3s = Tex(r" $\Theta$ = 180$^{\circ}$ ").set_color(YELLOW_E).set_height(0.2).shift(LEFT*5+DOWN*3)
        
        self.remove(angval_s)
        self.play(FadeIn(txt_thetas,txt3s))
        self.wait(8)
class Concept2_9(Scene):
    def construct(self):  

        txt1 = Text("We can classify Angles based on the range in which they lie" , line_spacing=1   ,  slant=ITALIC , font_size=18 , color = WHITE)
        txt1.to_edge( UP , buff = 0.5   )
        txt1.to_edge( LEFT , buff = 0.5)
        txt4 = Text("Acute angle Lies between 0° & 90°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = RED).shift(UP*0.25 + LEFT*4.5)

        acup1 = Vector(direction=np.array([1.5*1.41*cos(PI/4).real,1.5*1.41*sin(PI/4).real,0])).set_color(color=[RED]).shift(LEFT*6.5+UP*1)
        acup2 = Vector(direction=[1.41*1.5,0,0]).set_color(color=[RED]).shift(LEFT*6.5+UP*1)
        angleacup = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI/4 , start_angle=0, color = RED,fill_opacity=0.5, stroke_width=0).shift(LEFT*6.5+UP*1)
        txt_theta = Tex(r"$\Theta$").set_color(RED).set_height(0.2).shift(LEFT*5.7+UP*1.3)
        txt3 = Tex(r"$0^{\circ}$ < $\Theta$ < 90$^{\circ}$ ").set_color(RED).set_height(0.2).shift(DOWN*0.3 + LEFT*4.5)
        self.add(txt1,acup1,acup2,angleacup,txt4,txt3,txt_theta)
        
       
        txt5 = Text("Right angle is exactly 90°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = GREEN).shift(UP*0.25 + RIGHT*0.1)

        r1 = Vector(direction=np.array([1.5*1.41*cos(PI/2).real,1.5*1.41*sin(PI/2).real,0])).set_color(color=[GREEN]).shift(LEFT*1.4+UP*1)
        r2 = Vector(direction=[1.41*1.5,0,0]).set_color(color=[GREEN]).shift(LEFT*1.4+UP*1)
        anglerp = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI/2 , start_angle=0, color = GREEN,fill_opacity=0.5, stroke_width=0).shift(LEFT*1.4+UP*1)
        txt_thetar = Tex(r"$\Theta$").set_color(GREEN).set_height(0.2).shift(LEFT*0.6+UP*1.3)
        txt3r = Tex(r" $\Theta$ = 90$^{\circ}$ ").set_color(GREEN).set_height(0.2).shift(DOWN*0.3 + RIGHT*0.6)
        self.add(r1,r2,anglerp,txt_thetar,txt3r,txt5)

        txt6 = Text("Obtuse angle Lies between 90° and 180°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = BLUE).shift(UP*0.25 )
        txt6.to_edge(RIGHT, buff=0.5)
        
        ob1  = Vector(direction=np.array([1.5*1.41*cos(3*PI/4).real,1.5*1.41*sin(3*PI/4).real,0])).shift(RIGHT*4+UP*1).set_color(color=[BLUE])
        ob2 = Vector(direction=[2*1.41,0,0]).set_color(color=[BLUE]).shift(RIGHT*4+UP*1)
        angleob = AnnularSector(inner_radius=0, outer_radius=0.5, angle = 3*PI/4  , start_angle=0, color = BLUE,fill_opacity=0.5, stroke_width=0).shift(RIGHT*4+UP*1)
        txt_thetaop = Tex(r"$\Theta$").set_color(BLUE).set_height(0.2).shift(RIGHT*4.8+UP*1.3)
        txt3op = Tex(r"$90^{\circ}$ < $\Theta$ < 180$^{\circ}$ ").set_color(BLUE).set_height(0.2).shift(RIGHT*4+DOWN*0.3)
        self.add(ob1,ob2,angleob,txt_thetaop,txt3op,txt6)
        txt7 = Text("Straight angle is exactly 180°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = YELLOW)
        txt7.to_edge(LEFT , buff= 3.5)
        txt7.to_edge(DOWN , buff= 0.2)
        
        s1  = Vector(direction=np.array([1.5*1.41*cos(PI).real,1.5*1.41*sin(PI).real,0])).shift(LEFT*2+DOWN*3).set_color(color=[YELLOW])
        s2 = Vector(direction=[1.5*1.41,0,0]).set_color(color=[YELLOW]).shift(LEFT*2+DOWN*3)
        angles = AnnularSector(inner_radius=0, outer_radius=0.5, angle = PI  , start_angle=0, color = YELLOW,fill_opacity=0.5, stroke_width=0).shift(LEFT*2+DOWN*3)
        txt_thetas = Tex(r"$\Theta$").set_color(YELLOW).set_height(0.2).shift(LEFT*1.5+DOWN*2.5)
        txt3s = Tex(r" $\Theta$ = 180$^{\circ}$ ").set_color(YELLOW_E).set_height(0.2).shift(LEFT*5+DOWN*3)
        self.add(s1,s2,angles,txt_thetas,txt3s,txt7)
        self.wait(2)
        theta_ref = ValueTracker(PI)
        ref1 = always_redraw(lambda : Vector(direction=np.array([1.5*1.41*cos(theta_ref.get_value()).real,1.5*1.41*sin(theta_ref.get_value()).real,0])).shift(RIGHT*3+DOWN*1.5).set_color(color=[PINK]))
        ref2 = Vector(direction=[1.5*1.41,0,0]).set_color(color=[PINK]).shift(RIGHT*3+DOWN*1.5)
        angleref = always_redraw(lambda : AnnularSector(inner_radius=0, outer_radius=0.5, angle = theta_ref.get_value()  , start_angle=0, color = PINK,fill_opacity=0.5, stroke_width=0).shift(RIGHT*3+DOWN*1.5))
          
        angval_ref = always_redraw(lambda :  Text(str(abs(round((180*(theta_ref.get_value()))/PI,2)))+'°').set_height(0.3).shift(RIGHT*5.5 + DOWN*3))

        
        self.play(LaggedStart(FadeIn(ref1) ,FadeIn(angleref) ,FadeIn(ref2)),FadeIn(angval_ref))
        self.play(theta_ref.animate.set_value(PI) , run_time = 3)
        
    
        txt5 = Text("Reflex angle Lies between 90° and 180°" , line_spacing=1   ,  slant=ITALIC , font_size=16 , color = PINK)
        txt5.to_edge(RIGHT , buff= 0.5)
        txt5.to_edge(DOWN , buff= 0.2)

        self.play(FadeIn(txt5))
        self.wait(5)
        self.play(theta_ref.animate.set_value(2*PI) , run_time = 3)
        self.wait(3)
        self.play(theta_ref.animate.set_value(7*PI/4) , run_time = 3)
        self.wait(3)
        txt_thetas = Tex(r"$\Theta$").set_color(PINK).set_height(0.2).shift(RIGHT*3.6+DOWN*1)
        txt3s = Tex(r" $180^{\circ}$ < $\Theta$ < 360$^{\circ}$  ").set_color(PINK).set_height(0.2).shift(RIGHT*6+DOWN*1)
        self.remove(angval_ref)
        self.play(FadeIn(txt_thetas,txt3s))
        self.wait(6)

            
C = Concept2_9()
C.construct()