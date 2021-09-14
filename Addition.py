import manim from *

class Addition(Scene):
    def construct(self):
        expression = Tex("1257 + 894 = ", "?").scale(1.5)
        self.play(Write(expression))
        self.wait()
        self.play(expression.animate.to_corner(UL))
        self.wait()

        num1 = MathTex("1", "2", "5", "7", color=WHITE).scale(2)
        num2 = MathTex("8", "9", "4", color=WHITE).scale(2)
        ans  = MathTex("2", "1", "5", "1", color=WHITE).scale(2)
        line = Line(start=num1.get_left() + LEFT*2, end=num1.get_right(), color=WHITE)
        numbers = VGroup(num1, num2, line, ans).arrange(DOWN, aligned_edge = RIGHT, buff=0.5)
        plus_sign = MathTex("+").scale(2).next_to(num2, direction=LEFT, buff=1.5)

        # Create scene
        self.play(
            Write(num1),
            Write(num2),
            Write(plus_sign),
            Create(line),
        )
        self.wait()

        # ones
        ones_sum = MathTex("1", "1", color=WHITE).scale(2).move_to(ans[-1],aligned_edge=RIGHT)
        self.play(
            Indicate(num1[-1]),
            Indicate(num2[-1]),
        )
        self.wait()
        self.play(Write(ones_sum))
        self.wait()
        self.play(ones_sum[0].animate.next_to(num1[-2], direction=UP, buff=0.5).scale(0.8))

        # tens
        tens_sum = MathTex("1", "5", color=WHITE).scale(2).move_to(ans[-2],aligned_edge=RIGHT)
        self.play(
            Indicate(num1[-2]),
            Indicate(num2[-2]),
            Indicate(ones_sum[0]),
        )
        self.wait()
        self.play(Write(tens_sum))
        self.wait()
        self.play(tens_sum[0].animate.next_to(num1[-3], direction=UP, buff=0.5).scale(0.8))

        # hundreds
        hunds_sum = MathTex("1", "1", color=WHITE).scale(2).move_to(ans[-3],aligned_edge=RIGHT)
        self.play(
            Indicate(num1[-3]),
            Indicate(num2[-3]),
            Indicate(tens_sum[0]),
        )
        self.wait()
        self.play(Write(hunds_sum))
        self.wait()
        self.play(hunds_sum[0].animate.next_to(num1[-4], direction=UP, buff=0.5).scale(0.8))

        # thousands
        self.play(
            Indicate(num1[-4]),
            Indicate(hunds_sum[0]),
        )
        self.wait()
        self.play(Write(ans[0]))
        self.wait()

        # ending
        qmark_transform = Tex("2151", color=YELLOW).scale(1.5).move_to(expression[1], aligned_edge=LEFT)
        self.play(Circumscribe(ans, fade_out=True))
        self.wait()
        self.play(Transform(expression[-1], qmark_transform))
        self.wait()
