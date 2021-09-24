from manim import *

class KmapScene(Scene):
    def construct(self):
        # Truth Table
        TopLeftEntry = VGroup(
            Tex("x", "y", font_size=DEFAULT_FONT_SIZE).shift(DOWN*0.6),
            Tex("z", "w", font_size=DEFAULT_FONT_SIZE).shift(RIGHT*0.6),
        )
        Kmap = IntegerTable(
            [[1,1,1,0],
             [1,1,1,0],
             [0,1,1,1],
             [0,1,1,1]],
            row_labels=[MathTex("0", "0"), MathTex("0", "1"), MathTex("1", "1"), MathTex("1", "0")],
            col_labels=[MathTex("0", "0"), MathTex("0", "1"), MathTex("1", "1"), MathTex("1", "0")],
            v_buff=1.0,
            h_buff=1.0,
            top_left_entry=TopLeftEntry,
        ).shift(LEFT*3)

        # Expressions
        expression = MathTex("f(x,y,z,w)=\\Sigma m(0,1,3,4,5,7,9,10,11,13,14,15)")
        expression_simp = MathTex("x'z'", "+", "xz", "+", "w").shift(RIGHT*(config["frame_x_radius"]+Kmap.get_right())/2).scale(1.5)

        # Ones to be surrounded
        frame1_group = VGroup(Kmap.get_entries_without_labels()[0:2], Kmap.get_entries_without_labels()[4:6])
        frame2_group = VGroup(Kmap.get_entries_without_labels()[1:3], Kmap.get_entries_without_labels()[5:7], Kmap.get_entries_without_labels()[9:11], Kmap.get_entries_without_labels()[13:15])
        frame3_group = VGroup(Kmap.get_entries_without_labels()[10:12], Kmap.get_entries_without_labels()[14:16])
        frame1 = SurroundingRectangle(VGroup(frame1_group), color=RED, buff=0.3).round_corners(radius=0.2)
        frame2 = SurroundingRectangle(VGroup(frame2_group), color=RED, buff=0.3).round_corners(radius=0.2)
        frame3 = SurroundingRectangle(VGroup(frame3_group), color=RED, buff=0.3).round_corners(radius=0.2)


        self.play(Write(expression))
        self.wait(3)
        self.play(FadeOut(expression))
        self.wait()
        self.play(Kmap.create(), run_time=5)
        self.wait(3)

        self.play(Create(frame1))
        self.wait()
        self.play(Indicate(TopLeftEntry[0][0]), Indicate(Kmap.get_labels()[5][0]), Indicate(Kmap.get_labels()[6][0]))
        self.wait()
        self.play(Indicate(TopLeftEntry[1][0]), Indicate(Kmap.get_labels()[1][0]), Indicate(Kmap.get_labels()[2][0]))
        self.wait()
        self.play(Write(expression_simp[0]))
        self.wait(3)

        self.play(Create(frame2))
        self.wait()
        self.play(Indicate(TopLeftEntry[1][1]), Indicate(Kmap.get_labels()[2][1]), Indicate(Kmap.get_labels()[3][1]))
        self.wait()
        self.play(Write(expression_simp[4]))
        self.wait(3)

        self.play(Create(frame3))
        self.wait()
        self.play(Indicate(TopLeftEntry[0][0]), Indicate(Kmap.get_labels()[7][0]), Indicate(Kmap.get_labels()[8][0]))
        self.wait()
        self.play(Indicate(TopLeftEntry[1][0]), Indicate(Kmap.get_labels()[3][0]), Indicate(Kmap.get_labels()[4][0]))
        self.wait()
        self.play(Write(expression_simp[2]))
        self.wait()

        self.play(Write(expression_simp[1]), Write(expression_simp[3]), FadeOut(frame1), FadeOut(frame2), FadeOut(frame3), FadeOut(Kmap))
        self.play(expression_simp.animate.move_to(ORIGIN))
        self.wait(3)
