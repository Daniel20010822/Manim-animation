from manim import *

class CircleIllusion(Scene):
    def construct(self):
        bg_circle_radius = 3
        origin_point = np.array([-3,0,0])
        period = 4
        revolution = 2*PI

        # Dot moving around the circle(rotating_dot).
        phase = ValueTracker(0*DEGREES)
        rdot = always_redraw(lambda: Dot(point=[bg_circle_radius*np.cos(phase.get_value())-3,bg_circle_radius*np.sin(phase.get_value()),0], color=RED))
        rdot_vect_length = np.sqrt((rdot.get_center()[0] - origin_point[0])**2 + (rdot.get_center()[1] - origin_point[1])**2)

        # Background Circle
        bg_circle = Circle(radius=bg_circle_radius, color=WHITE, stroke_opacity=0.5).move_to(origin_point)
        imaginary_circle = Circle(radius=bg_circle_radius/2).shift(LEFT*1.5)
        imaginary_circle_path = Circle(radius=bg_circle_radius/2).shift(LEFT*3)

        # Creating paths that dots follow
        path_angles = np.arange(0*DEGREES, 180*DEGREES, 22.5*DEGREES)
        paths = VGroup()
        for angle in path_angles:
            paths.add(Line(start=[bg_circle_radius,0,0], end=[-bg_circle_radius,0,0], stroke_opacity=0.3).rotate_about_origin(angle).move_to(origin_point))


        # By projecting rdot on every path will create S.H.M.
        def SHM_on_path0():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[0])
            scalar = rdot_vect_length*np.cos(phase.get_value()-path_angles[0])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot0 = always_redraw(SHM_on_path0)

        def SHM_on_path1():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[1])
            scalar = rdot_vect_length*np.cos(phase.get_value()-path_angles[1])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot1 = always_redraw(SHM_on_path1)

        def SHM_on_path2():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[2])
            scalar = rdot_vect_length*np.cos(phase.get_value()-path_angles[2])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot2 = always_redraw(SHM_on_path2)

        def SHM_on_path3():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[3])
            scalar = rdot_vect_length*np.cos(phase.get_value()-path_angles[3])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot3 = always_redraw(SHM_on_path3)

        def SHM_on_path4():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[4])
            scalar = rdot_vect_length*np.cos(phase.get_value()-path_angles[4])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot4 = always_redraw(SHM_on_path4)

        def SHM_on_path5():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[5])
            scalar = rdot_vect_length*np.cos(phase.get_value()-path_angles[5])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot5 = always_redraw(SHM_on_path5)

        def SHM_on_path6():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[6])
            scalar = rdot_vect_length*np.cos(phase.get_value()-path_angles[6])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot6 = always_redraw(SHM_on_path6)

        def SHM_on_path7():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[7])
            scalar = rdot_vect_length*np.cos(phase.get_value()-path_angles[7])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot7 = always_redraw(SHM_on_path7)

        dots = VGroup(dot0, dot1, dot2, dot3, dot4, dot5, dot6, dot7)

        # Show the projection of rdot on every path
        projection0 = always_redraw(lambda: DashedLine(start=rdot.get_center(), end=dot0.get_center(), color=RED, stroke_opacity=0.5))
        projection1 = always_redraw(lambda: DashedLine(start=rdot.get_center(), end=dot1.get_center(), color=RED, stroke_opacity=0.5))
        projection2 = always_redraw(lambda: DashedLine(start=rdot.get_center(), end=dot2.get_center(), color=RED, stroke_opacity=0.5))
        projection3 = always_redraw(lambda: DashedLine(start=rdot.get_center(), end=dot3.get_center(), color=RED, stroke_opacity=0.5))
        projection4 = always_redraw(lambda: DashedLine(start=rdot.get_center(), end=dot4.get_center(), color=RED, stroke_opacity=0.5))
        projection5 = always_redraw(lambda: DashedLine(start=rdot.get_center(), end=dot5.get_center(), color=RED, stroke_opacity=0.5))
        projection6 = always_redraw(lambda: DashedLine(start=rdot.get_center(), end=dot6.get_center(), color=RED, stroke_opacity=0.5))
        projection7 = always_redraw(lambda: DashedLine(start=rdot.get_center(), end=dot7.get_center(), color=RED, stroke_opacity=0.5))

        projections = VGroup(projection0, projection1, projection2, projection3, projection4, projection5, projection6, projection7)

        # Subtitles
        subtitles = VGroup(
                   Text("????????????????????????"), #0
            VGroup(Text("?????????????????????"), Text("?????????????????????")).arrange(DOWN), #1
                   Text("???????????????????????????"), #2
            VGroup(Text("???????????????????????????"), Text("???????????????")).arrange(DOWN), #3
            VGroup(Text("???????????????????????????"), Text("??????????????????")).arrange(DOWN), #4
            VGroup(Text("???????????????????????????"), Text("???????????????????????????"), Text("???????????????????????????"), Text("????????????")).arrange(DOWN), #5
            VGroup(Text("????????????????????????"), Text("????????????")).arrange(DOWN), #6
            VGroup(Text("???????????????????????????"), Text("?????????????????????")).arrange(DOWN), #7
            VGroup(Text("????????????????????????"), Text("?????????????????????")).arrange(DOWN), #8
            VGroup(Text("???????????????????????????"), Text("?????????????????????")).arrange(DOWN), #9
            VGroup(Text("???????????????????????????"), Text("??????????????????")).arrange(DOWN), #10
            VGroup(Text("??????????????????"), Text("???????????????")).arrange(DOWN), #11
            VGroup(Text("?????????????????????"), Text("???????????????")).arrange(DOWN), #12
        )
        subtitles.scale(0.8)
        subtitles.shift(RIGHT*config["frame_x_radius"]/2)


        # part 1
        self.add(bg_circle)
        self.play(FadeIn(subtitles[0]))
        self.wait()
        self.play(FadeIn(dots), run_time=2)
        self.wait()
        self.play(phase.animate.increment_value(3*revolution), run_time=3*period, rate_func=linear)
        self.wait()
        
        # part 2
        self.play(
            ReplacementTransform(subtitles[0], subtitles[1]),
            FadeIn(imaginary_circle),
        )
        self.wait()
        self.play(
            MoveAlongPath(imaginary_circle, imaginary_circle_path),
            phase.animate.increment_value(revolution),
            run_time=2*period,
            rate_func=linear,
        )
        self.wait()
        self.play(
            ReplacementTransform(subtitles[1], subtitles[2]),
            FadeOut(imaginary_circle),
        )
        self.wait()
        
        # part 3
        self.play(AnimationGroup(*[FadeIn(path) for path in paths], lag_ratio=0.5, run_time=period))
        self.wait()
        self.play(ReplacementTransform(subtitles[2], subtitles[3]))
        self.wait()
        self.play(phase.animate.increment_value(2*revolution), run_time=2*period, rate_func=linear)
        self.wait()
        
        # part 4
        self.play(ReplacementTransform(subtitles[3], subtitles[4]), FadeIn(rdot))
        self.wait(2)
        self.play(ReplacementTransform(subtitles[4], subtitles[5]), FadeIn(projections))
        self.wait(3)
        self.play(ReplacementTransform(subtitles[5], subtitles[6]))
        self.wait()
        self.play(phase.animate.increment_value(2*revolution), run_time=4*period, rate_func=linear)
        self.wait()
        self.play(
            ReplacementTransform(subtitles[6], subtitles[7]),
            FadeOut(paths[1:8]),
            FadeOut(projections[1:8]),
            FadeOut(dots[1:8]),
        )
        self.wait(2)
        
        # part 5
        self.play(ReplacementTransform(subtitles[7], subtitles[8]))
        self.play(phase.animate.increment_value(revolution), run_time=2*period, rate_func=linear)
        self.wait()
        self.play(
            ReplacementTransform(subtitles[8], subtitles[9]),
            FadeOut(paths[0]), FadeOut(projections[0]), FadeOut(dots[0]),
            FadeIn(paths[1]), FadeIn(projections[1]), FadeIn(dots[1]),
        )
        self.play(phase.animate.increment_value(revolution), run_time=2*period, rate_func=linear)
        self.wait()
        self.play(
            ReplacementTransform(subtitles[9], subtitles[10]),
            FadeOut(paths[1]), FadeOut(projections[1]), FadeOut(dots[1]),
            FadeIn(paths[2]), FadeIn(projections[2]), FadeIn(dots[2]),
        )
        self.play(phase.animate.increment_value(revolution), run_time=2*period, rate_func=linear)
        self.wait()
        self.play(
            ReplacementTransform(subtitles[10], subtitles[11]),
            FadeOut(paths[2]), FadeOut(projections[2]), FadeOut(dots[2]),
            FadeIn(paths[3]), FadeIn(projections[3]), FadeIn(dots[3]),
        )
        self.play(phase.animate.increment_value(revolution), run_time=2*period, rate_func=linear)
        self.wait()
        self.play(
            FadeOut(paths[3]), FadeOut(projections[3]), FadeOut(dots[3]),
            FadeIn(paths[4]), FadeIn(projections[4]), FadeIn(dots[4]),
        )
        self.play(phase.animate.increment_value(revolution), run_time=2*period, rate_func=linear)
        self.wait()
        self.play(
            ReplacementTransform(subtitles[11], subtitles[12]),
            FadeOut(paths[4]),
            FadeOut(dots[4]),
            FadeOut(projections[4]),
            FadeOut(rdot),
        )
        self.wait(2)
        self.play(FadeIn(paths), FadeIn(dots))
        self.wait()
        self.play(phase.animate.increment_value(3*revolution), run_time=3*period, rate_func=linear)
        self.wait()
        self.play(FadeOut(paths), FadeOut(dots), FadeOut(bg_circle), FadeOut(subtitles[12]))
        self.wait()



