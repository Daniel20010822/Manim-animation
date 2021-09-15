from manim import *

class EpicycloidScene(Scene):
    def construct(self):
        total_runtime = 6
        stable_circle_radius = 2
        moving_circle_radius = 0.4
        ratio = stable_circle_radius/moving_circle_radius

        def update_trace(trace):
            previous_trace = trace.copy()
            previous_trace.add_points_as_corners([dot.get_center()])
            trace.become(previous_trace)

        path = Circle(radius=stable_circle_radius+moving_circle_radius, stroke_opacity=0.2)
        stable_circle = Circle(radius=stable_circle_radius)
        moving_circle = Arc(radius=moving_circle_radius, start_angle=PI, angle=TAU).move_to(path.get_right())
        dot = Dot().move_to(moving_circle.get_start())
        trace = VMobject()
        trace.set_points_as_corners([moving_circle.get_start(), moving_circle.get_start()])
        trace.add_updater(update_trace)
        trace.set_color(YELLOW)

        description = MathTex("R : r = 5 : 1").to_corner(UL)
        R_line = Line(start=stable_circle.get_center(), end=stable_circle.get_right())
        R_tex  = MathTex("R").move_to(R_line, aligned_edge=DOWN)
        r_line = Line(start=moving_circle.get_center(), end=moving_circle.get_right())
        r_tex  = MathTex("r").move_to(r_line, aligned_edge=DOWN)
        R = VGroup(R_line, R_tex)
        r = VGroup(r_line, r_tex)

        moving_cir_animation = MoveAlongPath(moving_circle, path=path, run_time=total_runtime, rate_func=linear)
        moving_dot_animation = Succession(*[MoveAlongPath(dot, path=moving_circle, run_time=total_runtime/ratio, rate_func=linear) for i in range(int(ratio))])

        self.add(stable_circle, moving_circle, trace, dot, R, r)
        self.play(Write(description))
        self.wait()
        self.play(Unwrite(R), Unwrite(r))
        self.wait(0.5)
        self.play(AnimationGroup(moving_cir_animation, moving_dot_animation))
        self.wait(3)

