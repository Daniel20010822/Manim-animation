from manim import *

class ParabolaScene(Scene):
    def construct(self):
        # (x-h)^2 = 4c(y-k)
        c = 3
        h = 0
        k = 0
        
        # Used in x_range: x_range = [startvalue, endvalue]
        # Detect whether y exceed config["frame_x_radius"] when x is config["frame_x_radius"], so that the center of the circle doesn't go out of the screen.
        startvalue = max(-np.sqrt(4*abs(c)*(config["frame_y_radius"]-k))+h, -config["frame_x_radius"])
        endvalue = min(np.sqrt(4*abs(c)*(config["frame_y_radius"]-k))+h, config["frame_x_radius"])
        e = ValueTracker(startvalue)
        plane = NumberPlane(
            faded_line_ratio=2,
            background_line_style = {
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0.5,
            },
            axis_config = {
                "stroke_opacity": 0,
            },
        )

        # y = (x-h)^2/4c + k
        parabola = FunctionGraph(lambda x: ((x-h)**2)/(4*c) + k, color=WHITE)
        directrix = Line(start=[-config["frame_x_radius"], k-c, 0], end=[config["frame_x_radius"], k - c, 0])
        focus = Dot(point=[h, k+c, 0], color=RED)

        moving_dot = always_redraw(lambda: Dot(point=[e.get_value(), ((e.get_value()-h)**2)/(4*c) + k, 0]))
        dot_to_directrix = always_redraw(lambda: DashedLine(start=moving_dot.get_center(), end=[e.get_value(), k-c, 0], stroke_opacity=0.5))
        dot_to_focus = always_redraw(lambda: DashedLine(start=moving_dot.get_center(), end=focus.get_center(), stroke_opacity=0.5))
        circle = always_redraw(lambda: Circle(radius=((e.get_value()-h)**2)/(4*c) + k - (k-c), stroke_opacity=0.8).move_to(moving_dot))

        self.add(plane)
        self.add(parabola, directrix, focus)
        self.wait()
        self.add(moving_dot, dot_to_directrix, dot_to_focus, circle)
        self.play(e.animate.set_value(endvalue), run_time=10, rate_func=linear)
        self.wait()

# The animation of changing the previous parabola to the current one.
class ParabolaChangingScene(Scene):
    def construct(self):
        c = ValueTracker(1)
        h = ValueTracker(0)
        k = ValueTracker(-1)

        plane = NumberPlane(
            faded_line_ratio=2,
            background_line_style = {
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0.5,
            },
            axis_config = {
                "stroke_opacity": 0,
            },
        )

        parabola = always_redraw(lambda: FunctionGraph(lambda x: ((x-h.get_value())**2)/(4*c.get_value()) + k.get_value(), color=WHITE))
        directrix = always_redraw(lambda: Line(start=[-config["frame_x_radius"], k.get_value() - c.get_value(), 0], end=[config["frame_x_radius"], k.get_value() - c.get_value(), 0]))
        focus = always_redraw(lambda: Dot(point=[h.get_value(), k.get_value()+c.get_value(), 0], color=RED))

        self.add(plane, parabola, directrix, focus)
        self.play(c.animate.set_value(3), k.animate.set_value(0), run_time=2)
        self.wait()
