from manim import *

class TitleScene(Scene):
    def construct(self):
        title = Text("Logic Gates").scale(2)
        self.add(title)
        self.wait()
        self.play(FadeOut(title))
        self.wait()



class LogicGates(Scene):
    def construct(self):
        # AND
        and_uphor  = Line(start = [0,1,0], end = [-1,1,0])
        and_lowhor = Line(start = [0,-1,0], end = [-1,-1, 0])
        and_ver    = Line(start = [-1,1,0], end = [-1,-1,0])
        and_arc    = Arc(radius = 1.0, start_angle = -PI/2 , angle = PI)
        and_text = Text("AND").shift(DOWN*2)
        AND_gate = Group(and_uphor, and_lowhor, and_ver, and_arc, and_text)
        self.play(
            Create(and_uphor),
            Create(and_lowhor),
            Create(and_ver),
            Create(and_arc),
            run_time = 1,
        )
        self.play(Write(and_text))
        self.add(AND_gate)
        self.wait()
        self.play(AND_gate.animate.move_to([-6,2,0]).scale(0.6))
        self.wait()

        # OR
        or_uparc = ArcBetweenPoints(start = [-1,-1,0], end = [1,0,0], angle = PI/4)
        or_lowarc = ArcBetweenPoints(start = [-1,1,0], end = [1,0,0], angle = -PI/4)
        or_leftarc = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3)
        or_text = Text("OR").shift(DOWN*2)
        OR_gate = Group(or_uparc, or_lowarc, or_leftarc, or_text)
        self.play(
            Create(or_uparc),
            Create(or_lowarc),
            Create(or_leftarc),
            run_time = 1,
        )
        self.play(Write(or_text))
        self.add(OR_gate)
        self.wait()
        self.play(OR_gate.animate.move_to([-3,2,0]).scale(0.6))
        self.wait()

        # NOT
        not_tri = Polygon([1 - np.sqrt(3),1,0],[1 - np.sqrt(3),-1,0],[1,0,0], color = WHITE)
        not_cir = Circle(radius = 0.2, color = WHITE).move_to([1.2,0,0])
        not_text = Text("NOT").shift(DOWN*2)
        NOT_gate = Group(not_tri, not_cir, not_text)
        self.play(
            Create(not_tri),
            Create(not_cir),
            run_time = 1,
        )
        self.play(Write(not_text))
        self.add(NOT_gate)
        self.wait()
        self.play(NOT_gate.animate.move_to([3,2,0]).scale(0.6))
        self.wait()

        # BUFFER
        buf_tri = Polygon([1 - np.sqrt(3),1,0],[1 - np.sqrt(3),-1,0],[1,0,0], color = WHITE)
        buf_text = Text("BUFFER").shift(DOWN*2)
        BUFFER = Group(buf_tri, buf_text)
        self.play(
            Create(buf_tri),
            run_time = 1,
        )
        self.play(Write(buf_text))
        self.add(BUFFER)
        self.wait()
        self.play(BUFFER.animate.move_to([6,2,0]).scale(0.6))
        self.wait()

        # NAND
        nand_uphor  = Line(start = [0,1,0], end = [-1,1,0])
        nand_lowhor = Line(start = [0,-1,0], end = [-1,-1, 0])
        nand_ver    = Line(start = [-1,1,0], end = [-1,-1,0])
        nand_arc    = Arc(radius = 1.0, start_angle = -PI/2 , angle = PI)
        nand_cir    = Circle(radius = 0.2, color = WHITE).move_to([1.2,0,0])
        nand_text   = Text("NAND").shift(DOWN*2)
        NAND_gate   = Group(nand_uphor, nand_lowhor, nand_ver, nand_arc, nand_cir, nand_text)
        self.play(
            Create(nand_uphor),
            Create(nand_lowhor),
            Create(nand_ver),
            Create(nand_arc),
            Create(nand_cir),
            run_time = 1,
        )
        self.play(Write(nand_text))
        self.add(NAND_gate)
        self.wait()
        self.play(NAND_gate.animate.move_to([-6,-2,0]).scale(0.6))
        self.wait()

        # NOR
        nor_uparc = ArcBetweenPoints(start = [-1,-1,0], end = [1,0,0], angle = PI/4)
        nor_lowarc = ArcBetweenPoints(start = [-1,1,0], end = [1,0,0], angle = -PI/4)
        nor_leftarc = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3)
        nor_cir    = Circle(radius = 0.2, color = WHITE).move_to([1.2,0,0])
        nor_text = Text("NOR").shift(DOWN*2)
        NOR_gate = Group(nor_uparc, nor_lowarc, nor_leftarc, nor_cir, nor_text)
        self.play(
            Create(nor_uparc),
            Create(nor_lowarc),
            Create(nor_leftarc),
            Create(nor_cir),
            run_time = 1,
        )
        self.play(Write(nor_text))
        self.add(NOR_gate)
        self.wait()
        self.play(NOR_gate.animate.move_to([-3,-2,0]).scale(0.6))
        self.wait()

        # XOR
        xor_uparc = ArcBetweenPoints(start = [-1,-1,0], end = [1,0,0], angle = PI/4)
        xor_lowarc = ArcBetweenPoints(start = [-1,1,0], end = [1,0,0], angle = -PI/4)
        xor_leftarc = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3)
        xor_leftarc2 = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3).shift(LEFT*0.2)
        xor_text = Text("XOR").shift(DOWN*2)
        XOR_gate = Group(xor_uparc, xor_lowarc, xor_leftarc, xor_leftarc2, xor_text)
        self.play(
            Create(xor_uparc),
            Create(xor_lowarc),
            Create(xor_leftarc),
            Create(xor_leftarc2),
            run_time = 1,
        )
        self.play(Write(xor_text))
        self.add(XOR_gate)
        self.wait()
        self.play(XOR_gate.animate.move_to([3,-2,0]).scale(0.6))
        self.wait()

        # XNOR
        xnor_uparc = ArcBetweenPoints(start = [-1,-1,0], end = [1,0,0], angle = PI/4)
        xnor_lowarc = ArcBetweenPoints(start = [-1,1,0], end = [1,0,0], angle = -PI/4)
        xnor_leftarc = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3)
        xnor_leftarc2 = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3).shift(LEFT*0.2)
        xnor_cir = Circle(radius = 0.2, color = WHITE).move_to([1.2,0,0])
        xnor_text = Text("XNOR").shift(DOWN*2)
        XNOR_gate = Group(xnor_leftarc, xnor_leftarc2, xnor_uparc, xnor_lowarc, xnor_cir, xnor_text)
        self.play(
            Create(xnor_uparc),
            Create(xnor_lowarc),
            Create(xnor_leftarc),
            Create(xnor_leftarc2),
            Create(xnor_cir),
            run_time = 1,
        )
        self.play(Write(xnor_text))
        self.add(XNOR_gate)
        self.wait()
        self.play(XNOR_gate.animate.move_to([6,-2,0]).scale(0.6))
        self.wait(3)
        self.play(
            FadeOut(AND_gate),
            FadeOut(OR_gate),
            FadeOut(NOT_gate),
            FadeOut(BUFFER),
            FadeOut(NAND_gate),
            FadeOut(NOR_gate),
            FadeOut(XOR_gate),
            FadeOut(XNOR_gate),
        )
        self.wait()



class AndGate(Scene):
    def construct(self):

        # Create AND gate
        and_uphor  = Line(start = [0,1,0], end = [-1,1,0])
        and_lowhor = Line(start = [0,-1,0], end = [-1,-1, 0])
        and_ver    = Line(start = [-1,1,0], end = [-1,-1,0])
        and_arc    = Arc(radius = 1.0, start_angle = -PI/2 , angle = PI)
        self.play(Create(and_lowhor), Create(and_uphor), Create(and_ver), Create(and_arc))

        # Create input and output wires
        wireA = Line(start = [-1,0.7,0], end = [-2,0.7,0])
        wireB = Line(start = [-1,-0.7,0], end = [-2,-0.7,0])
        wireO = Line(start = [1,0,0], end = [2,0,0])
        AND_gate = Group(and_lowhor, and_uphor, and_ver, and_arc, wireA, wireB, wireO)
        self.play(Create(wireA), Create(wireB), Create(wireO))
        self.add(AND_gate)
        self.play(ApplyMethod(AND_gate.shift, LEFT*3))

        # wire values
        oneA  = Text("1", color = RED).next_to(wireA.get_end(), direction = LEFT)
        zeroA = Text("0").next_to(wireA.get_end(), direction = LEFT)
        oneB  = Text("1", color = RED).next_to(wireB.get_end(), direction = LEFT)
        zeroB = Text("0").next_to(wireB.get_end(), direction = LEFT)
        oneB_2  = oneB.copy()
        zeroB_2 = zeroB.copy()
        oneO  = Text("1", color = RED).next_to(wireO.get_end(), direction = RIGHT)
        zeroO = Text("0").next_to(wireO.get_end(), direction = RIGHT)
        textA = Text("A", color = BLUE).next_to(zeroA, direction = LEFT)
        textB = Text("B", color = BLUE).next_to(zeroB, direction = LEFT)
        textO = Text("O", color = BLUE_D).next_to(zeroO, direction = RIGHT)
        self.play(Write(textA), Write(textB), Write(textO))
        self.play(Write(zeroA), Write(zeroB), Write(zeroO))

        # Truth table
        AND_table = Table(
            [
            ["0","0","0"],
            ["0","1","0"],
            ["1","0","0"],
            ["1","1","1"]
            ],
            col_labels = [Text("A", color = BLUE), Text("B", color = BLUE), Text("O", color = BLUE_D)],
            include_outer_lines = True,
        ).shift(RIGHT*4)
        self.play(Create(AND_table), run_time = 1)
        self.wait()

        # 00
        self.play(Indicate(AND_table.get_rows()[1][0:3]), run_time = 1)
        self.wait()

        # 01
        self.play(
            ApplyMethod(wireB.set_color, RED, run_time = 0.1),
            ReplacementTransform(zeroB, oneB, run_time = 0.1),
            Indicate(AND_table.get_rows()[2][0:3], run_time = 1),
        )
        self.wait()

        # 10
        self.play(
            ApplyMethod(wireA.set_color, RED, run_time = 0.1),
            ApplyMethod(wireB.set_color, WHITE, run_time = 0.1),
            ReplacementTransform(zeroA, oneA, run_time = 0.1),
            ReplacementTransform(oneB, zeroB_2, run_time = 0.1),
            Indicate(AND_table.get_rows()[3][0:3], run_time = 1),
        )
        self.wait()

        # 11
        self.play(
            ApplyMethod(wireB.set_color, RED, run_time = 0.1),
            ApplyMethod(wireO.set_color, RED, run_time = 0.1),
            ReplacementTransform(zeroB_2, oneB_2, run_time = 0.1),
            ReplacementTransform(zeroO, oneO, run_time = 0.1),
            Indicate(AND_table.get_rows()[4][0:3], run_time = 1),
        )
        self.wait()

        self.play(
            Uncreate(AND_table),
            Uncreate(and_arc),
            Uncreate(and_lowhor),
            Uncreate(and_uphor),
            Uncreate(and_ver),
            Uncreate(wireA),
            Uncreate(wireB),
            Uncreate(wireO),
            Uncreate(textA),
            Uncreate(textB),
            Uncreate(textO),
            Uncreate(oneA),
            Uncreate(oneB_2),
            Uncreate(oneO),
        )
        self.wait()



class OrGate(Scene):
    def construct(self):

        # Create OR gate
        or_uparc = ArcBetweenPoints(start = [-1,-1,0], end = [1,0,0], angle = PI/4)
        or_lowarc = ArcBetweenPoints(start = [-1,1,0], end = [1,0,0], angle = -PI/4)
        or_leftarc = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3)
        self.play(Create(or_uparc), Create(or_lowarc), Create(or_leftarc))

        # Create input and output wires
        wireA = Line(start = [-0.88,0.7,0], end = [-2,0.7,0])
        wireB = Line(start = [-0.88,-0.7,0], end = [-2,-0.7,0])
        wireO = Line(start = [1,0,0], end = [2,0,0])
        OR_gate = Group(or_uparc, or_lowarc, or_leftarc, wireA, wireB, wireO)
        self.play(Create(wireA), Create(wireB), Create(wireO))
        self.add(OR_gate)
        self.play(ApplyMethod(OR_gate.shift, LEFT*3))

        # wire values
        oneA  = Text("1", color = RED).next_to(wireA.get_end(), direction = LEFT)
        zeroA = Text("0").next_to(wireA.get_end(), direction = LEFT)
        oneB  = Text("1", color = RED).next_to(wireB.get_end(), direction = LEFT)
        zeroB = Text("0").next_to(wireB.get_end(), direction = LEFT)
        oneB_2  = oneB.copy()
        zeroB_2 = zeroB.copy()
        oneO  = Text("1", color = RED).next_to(wireO.get_end(), direction = RIGHT)
        zeroO = Text("0").next_to(wireO.get_end(), direction = RIGHT)
        textA = Text("A", color = BLUE).next_to(zeroA, direction = LEFT)
        textB = Text("B", color = BLUE).next_to(zeroB, direction = LEFT)
        textO = Text("O", color = BLUE_D).next_to(zeroO, direction = RIGHT)
        self.play(Write(textA), Write(textB), Write(textO))
        self.play(Write(zeroA), Write(zeroB), Write(zeroO))

        # Truth table
        OR_table = Table(
            [
            ["0","0","0"],
            ["0","1","1"],
            ["1","0","1"],
            ["1","1","1"]
            ],
            col_labels = [Text("A", color = BLUE), Text("B", color = BLUE), Text("O", color = BLUE_D)],
            include_outer_lines = True,
        ).shift(RIGHT*4)
        self.play(Create(OR_table), run_time = 1)
        self.wait()

        # 00
        self.play(Indicate(OR_table.get_rows()[1][0:3]), run_time = 1)
        self.wait()

        # 01
        self.play(
            ApplyMethod(wireB.set_color, RED, run_time = 0.1),
            ApplyMethod(wireO.set_color, RED, run_time = 0.1),
            ReplacementTransform(zeroB, oneB, run_time = 0.1),
            ReplacementTransform(zeroO, oneO, run_time = 0.1),
            Indicate(OR_table.get_rows()[2][0:3], run_time = 1),
        )
        self.wait()

        # 10
        self.play(
            ApplyMethod(wireA.set_color, RED, run_time = 0.1),
            ApplyMethod(wireB.set_color, WHITE, run_time = 0.1),
            ReplacementTransform(zeroA, oneA, run_time = 0.1),
            ReplacementTransform(oneB, zeroB_2, run_time = 0.1),
            Indicate(OR_table.get_rows()[3][0:3], run_time = 1),
        )
        self.wait()

        # 11
        self.play(
            ApplyMethod(wireB.set_color, RED, run_time = 0.1),
            ReplacementTransform(zeroB_2, oneB_2, run_time = 0.1),
            Indicate(OR_table.get_rows()[4][0:3], run_time = 1),
        )
        self.wait()

        self.play(
            Uncreate(OR_table),
            Uncreate(or_leftarc),
            Uncreate(or_lowarc),
            Uncreate(or_uparc),
            Uncreate(wireA),
            Uncreate(wireB),
            Uncreate(wireO),
            Uncreate(textA),
            Uncreate(textB),
            Uncreate(textO),
            Uncreate(oneA),
            Uncreate(oneB_2),
            Uncreate(oneO),
        )
        self.wait()



class NotGate(Scene):
    def construct(self):

        # Create NOT Gate
        not_tri = Polygon([1 - np.sqrt(3),1,0],[1 - np.sqrt(3),-1,0],[1,0,0], color = WHITE)
        not_cir = Circle(radius = 0.2, color = WHITE).move_to([1.2,0,0])
        self.play(Create(not_tri), Create(not_cir))

        # Create input and output wires
        wireA = Line(start = [1 - np.sqrt(3), 0,0], end = [-2,0,0])
        wireO = Line(start = [1.4,0,0], end = [2,0,0], color = RED)
        NOT_gate = Group(not_tri, not_cir, wireA, wireO)
        self.play(Create(wireA), Create(wireO))
        self.add(NOT_gate)
        self.play(ApplyMethod(NOT_gate.shift, LEFT*3))

        # wire values
        oneA  = Text("1", color = RED).next_to(wireA.get_end(), direction = LEFT)
        zeroA = Text("0").next_to(wireA.get_end(), direction = LEFT)
        oneO  = Text("1", color = RED).next_to(wireO.get_end(), direction = RIGHT)
        zeroO = Text("0").next_to(wireO.get_end(), direction = RIGHT)
        textA = Text("A", color = BLUE).next_to(zeroA, direction = LEFT)
        textO = Text("O", color = BLUE_D).next_to(zeroO, direction = RIGHT)
        self.play(Write(textA), Write(textO))
        self.play(Write(zeroA), Write(oneO))

        # Truth table
        NOT_table = Table(
            [
            ["0","1"],
            ["1","0"]
            ],
            col_labels = [Text("A", color = BLUE), Text("O", color = BLUE_D)],
            include_outer_lines = True,
        ).shift(RIGHT*4)
        self.play(Create(NOT_table), run_time = 1)
        self.wait()

        # 0
        self.play(Indicate(NOT_table.get_rows()[1][0:2]), run_time = 1)
        self.wait()

        # 1
        self.play(
            ApplyMethod(wireA.set_color, RED  , run_time = 0.1),
            ApplyMethod(wireO.set_color, WHITE, run_time = 0.1),
            ReplacementTransform(zeroA, oneA, run_time = 0.1),
            ReplacementTransform(oneO, zeroO, run_time = 0.1),
            Indicate(NOT_table.get_rows()[2][0:2], run_time = 1),
        )
        self.wait()

        self.play(
            Uncreate(NOT_table),
            Uncreate(not_tri),
            Uncreate(not_cir),
            Uncreate(wireA),
            Uncreate(wireO),
            Uncreate(textA),
            Uncreate(textO),
            Uncreate(oneA),
            Uncreate(zeroO),
        )
        self.wait()



class Buffer(Scene):
    def construct(self):

        # Create BUFFER
        buff_tri = Polygon([1 - np.sqrt(3),1,0],[1 - np.sqrt(3),-1,0],[1,0,0], color = WHITE)
        self.play(Create(buff_tri))

        # Create input and output wires
        wireA = Line(start = [1 - np.sqrt(3), 0,0], end = [-2,0,0])
        wireO = Line(start = [1,0,0], end = [2,0,0])
        BUFFER = Group(buff_tri, wireA, wireO)
        self.play(Create(wireA), Create(wireO))
        self.add(BUFFER)
        self.play(ApplyMethod(BUFFER.shift, LEFT*3))

        # wire values
        oneA  = Text("1", color = RED).next_to(wireA.get_end(), direction = LEFT)
        zeroA = Text("0").next_to(wireA.get_end(), direction = LEFT)
        oneO  = Text("1", color = RED).next_to(wireO.get_end(), direction = RIGHT)
        zeroO = Text("0").next_to(wireO.get_end(), direction = RIGHT)
        textA = Text("A", color = BLUE).next_to(zeroA, direction = LEFT)
        textO = Text("O", color = BLUE_D).next_to(zeroO, direction = RIGHT)
        self.play(Write(textA), Write(textO))
        self.play(Write(zeroA), Write(zeroO))

        # Truth table
        BUFFER_table = Table(
            [
            ["0","0"],
            ["1","1"]
            ],
            col_labels = [Text("A", color = BLUE), Text("O", color = BLUE_D)],
            include_outer_lines = True,
        ).shift(RIGHT*4)
        self.play(Create(BUFFER_table), run_time = 1)
        self.wait()

        # 0
        self.play(Indicate(BUFFER_table.get_rows()[1][0:2]), run_time = 1)
        self.wait()

        # 1
        self.play(
            ApplyMethod(wireA.set_color, RED  , run_time = 0.1),
            ApplyMethod(wireO.set_color, RED, run_time = 0.1),
            ReplacementTransform(zeroA, oneA, run_time = 0.1),
            ReplacementTransform(zeroO, oneO, run_time = 0.1),
            Indicate(BUFFER_table.get_rows()[2][0:2], run_time = 1),
        )
        self.wait()

        self.play(
            Uncreate(BUFFER_table),
            Uncreate(buff_tri),
            Uncreate(wireA),
            Uncreate(wireO),
            Uncreate(textA),
            Uncreate(textO),
            Uncreate(oneA),
            Uncreate(oneO),
        )
        self.wait()



class NandGate(Scene):
    def construct(self):


        # And
        and_uphor  = Line(start = [0,1,0], end = [-1,1,0]).shift(LEFT*2)
        and_lowhor = Line(start = [0,-1,0], end = [-1,-1, 0]).shift(LEFT*2)
        and_ver    = Line(start = [-1,1,0], end = [-1,-1,0]).shift(LEFT*2)
        and_arc    = Arc(radius = 1.0, start_angle = -PI/2 , angle = PI).shift(LEFT*2)
        # Not
        not_tri = Polygon([1 - np.sqrt(3),1,0],[1 - np.sqrt(3),-1,0],[1,0,0], color = WHITE).shift(RIGHT*2)
        not_cir = Circle(radius = 0.2, color = WHITE).move_to([1.2,0,0]).shift(RIGHT*2)
        plus_sign = Text("+")
        self.play(
            Create(and_lowhor),
            Create(and_uphor),
            Create(and_ver),
            Create(and_arc),
            Create(not_tri),
            Create(not_cir),
            FadeIn(plus_sign),
        )
        self.wait()
        self.play(
            Uncreate(not_tri, run_time = 0.2),
            ApplyMethod(and_lowhor.shift, RIGHT*2),
            ApplyMethod(and_uphor.shift, RIGHT*2),
            ApplyMethod(and_ver.shift, RIGHT*2),
            ApplyMethod(and_arc.shift, RIGHT*2),
            ApplyMethod(not_cir.shift, LEFT*2),
            FadeOut(plus_sign, run_time = 0.2),
        )
        self.wait()


        # Create input and output wires
        wireA = Line(start = [-1,0.7,0], end = [-2,0.7,0])
        wireB = Line(start = [-1,-0.7,0], end = [-2,-0.7,0])
        wireO = Line(start = [1.4,0,0], end = [2,0,0], color = RED)
        NAND_gate = Group(and_lowhor, and_uphor, and_ver, and_arc, not_cir, wireA, wireB, wireO)
        self.play(Create(wireA), Create(wireB), Create(wireO))
        self.add(NAND_gate)
        self.play(ApplyMethod(NAND_gate.shift, LEFT*3))

        # wire values
        oneA  = Text("1", color = RED).next_to(wireA.get_end(), direction = LEFT)
        zeroA = Text("0").next_to(wireA.get_end(), direction = LEFT)
        oneB  = Text("1", color = RED).next_to(wireB.get_end(), direction = LEFT)
        zeroB = Text("0").next_to(wireB.get_end(), direction = LEFT)
        oneB_2  = oneB.copy()
        zeroB_2 = zeroB.copy()
        oneO  = Text("1", color = RED).next_to(wireO.get_end(), direction = RIGHT)
        zeroO = Text("0").next_to(wireO.get_end(), direction = RIGHT)
        textA = Text("A", color = BLUE).next_to(zeroA, direction = LEFT)
        textB = Text("B", color = BLUE).next_to(zeroB, direction = LEFT)
        textO = Text("O", color = BLUE_D).next_to(zeroO, direction = RIGHT)
        self.play(Write(textA), Write(textB), Write(textO))
        self.play(Write(zeroA), Write(zeroB), Write(oneO))

        # Truth table
        NAND_table = Table(
            [
            ["0","0","1"],
            ["0","1","1"],
            ["1","0","1"],
            ["1","1","0"]
            ],
            col_labels = [Text("A", color = BLUE), Text("B", color = BLUE), Text("O", color = BLUE_D)],
            include_outer_lines = True,
        ).shift(RIGHT*4)
        self.play(Create(NAND_table), run_time = 1)
        self.wait()

        # 00
        self.play(Indicate(NAND_table.get_rows()[1][0:3]), run_time = 1)
        self.wait()

        # 01
        self.play(
            ApplyMethod(wireB.set_color, RED  , run_time = 0.1),
            ReplacementTransform(zeroB, oneB, run_time = 0.1),
            Indicate(NAND_table.get_rows()[2][0:3], run_time = 1),
        )
        self.wait()

        # 10
        self.play(
            ApplyMethod(wireA.set_color, RED, run_time = 0.1),
            ApplyMethod(wireB.set_color, WHITE, run_time = 0.1),
            ReplacementTransform(zeroA, oneA, run_time = 0.1),
            ReplacementTransform(oneB, zeroB_2, run_time = 0.1),
            Indicate(NAND_table.get_rows()[3][0:3], run_time = 1),
        )
        self.wait()

        # 11
        self.play(
            ApplyMethod(wireB.set_color, RED, run_time = 0.1),
            ApplyMethod(wireO.set_color, WHITE, run_time = 0.1),
            ReplacementTransform(zeroB_2, oneB_2, run_time = 0.1),
            ReplacementTransform(oneO, zeroO, run_time = 0.1),
            Indicate(NAND_table.get_rows()[4][0:3], run_time = 1),
        )
        self.wait()

        self.play(
            Uncreate(NAND_table),
            Uncreate(and_arc),
            Uncreate(and_lowhor),
            Uncreate(and_uphor),
            Uncreate(and_ver),
            Uncreate(not_cir),
            Uncreate(wireA),
            Uncreate(wireB),
            Uncreate(wireO),
            Uncreate(textA),
            Uncreate(textB),
            Uncreate(textO),
            Uncreate(oneA),
            Uncreate(oneB_2),
            Uncreate(zeroO),
        )
        self.wait()



class NorGate(Scene):
    def construct(self):

        # Or
        or_uparc = ArcBetweenPoints(start = [-1,-1,0], end = [1,0,0], angle = PI/4).shift(LEFT*2)
        or_lowarc = ArcBetweenPoints(start = [-1,1,0], end = [1,0,0], angle = -PI/4).shift(LEFT*2)
        or_leftarc = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3).shift(LEFT*2)
        # Not
        not_tri = Polygon([1 - np.sqrt(3),1,0],[1 - np.sqrt(3),-1,0],[1,0,0], color = WHITE).shift(RIGHT*2)
        not_cir = Circle(radius = 0.2, color = WHITE).move_to([1.2,0,0]).shift(RIGHT*2)
        plus_sign = Text("+")
        self.play(
            Create(or_uparc),
            Create(or_lowarc),
            Create(or_leftarc),
            Create(not_tri),
            Create(not_cir),
            FadeIn(plus_sign),
        )
        self.wait()
        self.play(
            Uncreate(not_tri, run_time = 0.2),
            ApplyMethod(or_uparc.shift, RIGHT*2),
            ApplyMethod(or_lowarc.shift, RIGHT*2),
            ApplyMethod(or_leftarc.shift, RIGHT*2),
            ApplyMethod(not_cir.shift, LEFT*2),
            FadeOut(plus_sign, run_time = 0.2),
        )
        self.wait()


        # Create input and output wires
        wireA = Line(start = [-0.88,0.7,0], end = [-2,0.7,0])
        wireB = Line(start = [-0.88,-0.7,0], end = [-2,-0.7,0])
        wireO = Line(start = [1.4,0,0], end = [2,0,0], color = RED)
        NOR_gate = Group(or_lowarc, or_uparc, or_leftarc, not_cir, wireA, wireB, wireO)
        self.play(Create(wireA), Create(wireB), Create(wireO))
        self.add(NOR_gate)
        self.play(ApplyMethod(NOR_gate.shift, LEFT*3))

        # wire values
        oneA  = Text("1", color = RED).next_to(wireA.get_end(), direction = LEFT)
        zeroA = Text("0").next_to(wireA.get_end(), direction = LEFT)
        oneB  = Text("1", color = RED).next_to(wireB.get_end(), direction = LEFT)
        zeroB = Text("0").next_to(wireB.get_end(), direction = LEFT)
        oneB_2  = oneB.copy()
        zeroB_2 = zeroB.copy()
        oneO  = Text("1", color = RED).next_to(wireO.get_end(), direction = RIGHT)
        zeroO = Text("0").next_to(wireO.get_end(), direction = RIGHT)
        textA = Text("A", color = BLUE).next_to(zeroA, direction = LEFT)
        textB = Text("B", color = BLUE).next_to(zeroB, direction = LEFT)
        textO = Text("O", color = BLUE_D).next_to(zeroO, direction = RIGHT)
        self.play(Write(textA), Write(textB), Write(textO))
        self.play(Write(zeroA), Write(zeroB), Write(oneO))

        # Truth table
        NOR_table = Table(
            [
            ["0","0","1"],
            ["0","1","0"],
            ["1","0","0"],
            ["1","1","0"]
            ],
            col_labels = [Text("A", color = BLUE), Text("B", color = BLUE), Text("O", color = BLUE_D)],
            include_outer_lines = True,
        ).shift(RIGHT*4)
        self.play(Create(NOR_table), run_time = 1)
        self.wait()

        # 00
        self.play(Indicate(NOR_table.get_rows()[1][0:3]), run_time = 1)
        self.wait()

        # 01
        self.play(
            ApplyMethod(wireB.set_color, RED  , run_time = 0.1),
            ApplyMethod(wireO.set_color, WHITE, run_time = 0.1),
            ReplacementTransform(zeroB, oneB, run_time = 0.1),
            ReplacementTransform(oneO, zeroO, run_time = 0.1),
            Indicate(NOR_table.get_rows()[2][0:3], run_time = 1),
        )
        self.wait()

        # 10
        self.play(
            ApplyMethod(wireA.set_color, RED, run_time = 0.1),
            ApplyMethod(wireB.set_color, WHITE, run_time = 0.1),
            ReplacementTransform(zeroA, oneA, run_time = 0.1),
            ReplacementTransform(oneB, zeroB_2, run_time = 0.1),
            Indicate(NOR_table.get_rows()[3][0:3], run_time = 1),
        )
        self.wait()

        # 11
        self.play(
            ApplyMethod(wireB.set_color, RED, run_time = 0.1),
            ReplacementTransform(zeroB_2, oneB_2, run_time = 0.1),
            Indicate(NOR_table.get_rows()[4][0:3], run_time = 1),
        )
        self.wait()

        self.play(
            Uncreate(NOR_table),
            Uncreate(or_leftarc),
            Uncreate(or_lowarc),
            Uncreate(or_uparc),
            Uncreate(not_cir),
            Uncreate(wireA),
            Uncreate(wireB),
            Uncreate(wireO),
            Uncreate(textA),
            Uncreate(textB),
            Uncreate(textO),
            Uncreate(oneA),
            Uncreate(oneB_2),
            Uncreate(zeroO),
        )
        self.wait()



class XorGate(Scene):
    def construct(self):
        # Create XOR gate
        xor_uparc = ArcBetweenPoints(start = [-1,-1,0], end = [1,0,0], angle = PI/4)
        xor_lowarc = ArcBetweenPoints(start = [-1,1,0], end = [1,0,0], angle = -PI/4)
        xor_leftarc = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3)
        xor_leftarc2 = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3).shift(LEFT*0.2)
        self.play(Create(xor_uparc), Create(xor_lowarc), Create(xor_leftarc), Create(xor_leftarc2))

        # Create input and output wires
        wireA = Line(start = [-1.08,0.7,0], end = [-2,0.7,0])
        wireB = Line(start = [-1.08,-0.7,0], end = [-2,-0.7,0])
        wireO = Line(start = [1,0,0], end = [2,0,0])
        XOR_gate = Group(xor_uparc, xor_lowarc, xor_leftarc, xor_leftarc2, wireA, wireB, wireO)
        self.play(Create(wireA), Create(wireB), Create(wireO))
        self.add(XOR_gate)
        self.play(ApplyMethod(XOR_gate.shift, LEFT*3))

        # wire values
        oneA  = Text("1", color = RED).next_to(wireA.get_end(), direction = LEFT)
        zeroA = Text("0").next_to(wireA.get_end(), direction = LEFT)
        oneB  = Text("1", color = RED).next_to(wireB.get_end(), direction = LEFT)
        zeroB = Text("0").next_to(wireB.get_end(), direction = LEFT)
        oneB_2  = oneB.copy()
        zeroB_2 = zeroB.copy()
        oneO  = Text("1", color = RED).next_to(wireO.get_end(), direction = RIGHT)
        zeroO = Text("0").next_to(wireO.get_end(), direction = RIGHT)
        zeroO_2 = zeroO.copy()
        textA = Text("A", color = BLUE).next_to(zeroA, direction = LEFT)
        textB = Text("B", color = BLUE).next_to(zeroB, direction = LEFT)
        textO = Text("O", color = BLUE_D).next_to(zeroO, direction = RIGHT)
        self.play(Write(textA), Write(textB), Write(textO))
        self.play(Write(zeroA), Write(zeroB), Write(zeroO))

        # Truth table
        XOR_table = Table(
            [
            ["0","0","0"],
            ["0","1","1"],
            ["1","0","1"],
            ["1","1","0"]
            ],
            col_labels = [Text("A", color = BLUE), Text("B", color = BLUE), Text("O", color = BLUE_D)],
            include_outer_lines = True,
        ).shift(RIGHT*4)
        self.play(Create(XOR_table), run_time = 1)
        self.wait()

        # 00
        self.play(Indicate(XOR_table.get_rows()[1][0:3]), run_time = 1)
        self.wait()

        # 01
        self.play(
            ApplyMethod(wireB.set_color, RED, run_time = 0.1),
            ApplyMethod(wireO.set_color, RED, run_time = 0.1),
            ReplacementTransform(zeroB, oneB, run_time = 0.1),
            ReplacementTransform(zeroO, oneO, run_time = 0.1),
            Indicate(XOR_table.get_rows()[2][0:3], run_time = 1),
        )
        self.wait()

        # 10
        self.play(
            ApplyMethod(wireA.set_color, RED, run_time = 0.1),
            ApplyMethod(wireB.set_color, WHITE, run_time = 0.1),
            ReplacementTransform(zeroA, oneA, run_time = 0.1),
            ReplacementTransform(oneB, zeroB_2, run_time = 0.1),
            Indicate(XOR_table.get_rows()[3][0:3], run_time = 1),
        )
        self.wait()

        # 11
        self.play(
            ApplyMethod(wireB.set_color, RED  , run_time = 0.1),
            ApplyMethod(wireO.set_color, WHITE, run_time = 0.1),
            ReplacementTransform(zeroB_2, oneB_2, run_time = 0.1),
            ReplacementTransform(oneO, zeroO_2, run_time = 0.1),
            Indicate(XOR_table.get_rows()[4][0:3], run_time = 1),
        )
        self.wait()

        self.play(
            Uncreate(XOR_table),
            Uncreate(xor_leftarc),
            Uncreate(xor_leftarc2),
            Uncreate(xor_lowarc),
            Uncreate(xor_uparc),
            Uncreate(wireA),
            Uncreate(wireB),
            Uncreate(wireO),
            Uncreate(textA),
            Uncreate(textB),
            Uncreate(textO),
            Uncreate(oneA),
            Uncreate(oneB_2),
            Uncreate(zeroO_2),
        )
        self.wait()



class XnorGate(Scene):
    def construct(self):

        # Xor
        xor_uparc = ArcBetweenPoints(start = [-1,-1,0], end = [1,0,0], angle = PI/4).shift(LEFT*2)
        xor_lowarc = ArcBetweenPoints(start = [-1,1,0], end = [1,0,0], angle = -PI/4).shift(LEFT*2)
        xor_leftarc = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3).shift(LEFT*2)
        xor_leftarc2 = ArcBetweenPoints(start = [-1,1,0], end = [-1,-1,0], angle = -PI/3).shift(LEFT*2.2)
        # Not
        not_tri = Polygon([1 - np.sqrt(3),1,0],[1 - np.sqrt(3),-1,0],[1,0,0], color = WHITE).shift(RIGHT*2)
        not_cir = Circle(radius = 0.2, color = WHITE).move_to([1.2,0,0]).shift(RIGHT*2)
        plus_sign = Text("+")
        self.play(
            Create(xor_uparc),
            Create(xor_lowarc),
            Create(xor_leftarc),
            Create(xor_leftarc2),
            Create(not_tri),
            Create(not_cir),
            FadeIn(plus_sign),
        )
        self.wait()
        self.play(
            Uncreate(not_tri, run_time = 0.2),
            ApplyMethod(xor_uparc.shift, RIGHT*2),
            ApplyMethod(xor_lowarc.shift, RIGHT*2),
            ApplyMethod(xor_leftarc.shift, RIGHT*2),
            ApplyMethod(xor_leftarc2.shift, RIGHT*2),
            ApplyMethod(not_cir.shift, LEFT*2),
            FadeOut(plus_sign, run_time = 0.2),
        )
        self.wait()


        # Create input and output wires
        wireA = Line(start = [-1.08,0.7,0], end = [-2,0.7,0])
        wireB = Line(start = [-1.08,-0.7,0], end = [-2,-0.7,0])
        wireO = Line(start = [1.4,0,0], end = [2,0,0], color = RED)
        NOR_gate = Group(xor_lowarc, xor_uparc, xor_leftarc, xor_leftarc2, not_cir, wireA, wireB, wireO)
        self.play(Create(wireA), Create(wireB), Create(wireO))
        self.add(NOR_gate)
        self.play(ApplyMethod(NOR_gate.shift, LEFT*3))

        # wire values
        oneA  = Text("1", color = RED).next_to(wireA.get_end(), direction = LEFT)
        zeroA = Text("0").next_to(wireA.get_end(), direction = LEFT)
        oneB  = Text("1", color = RED).next_to(wireB.get_end(), direction = LEFT)
        zeroB = Text("0").next_to(wireB.get_end(), direction = LEFT)
        oneB_2  = oneB.copy()
        zeroB_2 = zeroB.copy()
        oneO  = Text("1", color = RED).next_to(wireO.get_end(), direction = RIGHT)
        oneO_2  = oneO.copy()
        zeroO = Text("0").next_to(wireO.get_end(), direction = RIGHT)
        textA = Text("A", color = BLUE).next_to(zeroA, direction = LEFT)
        textB = Text("B", color = BLUE).next_to(zeroB, direction = LEFT)
        textO = Text("O", color = BLUE_D).next_to(zeroO, direction = RIGHT)
        self.play(Write(textA), Write(textB), Write(textO))
        self.play(Write(zeroA), Write(zeroB), Write(oneO))

        # Truth table
        XNOR_table = Table(
            [
            ["0","0","1"],
            ["0","1","0"],
            ["1","0","0"],
            ["1","1","1"]
            ],
            col_labels = [Text("A", color = BLUE), Text("B", color = BLUE), Text("O", color = BLUE_D)],
            include_outer_lines = True,
        ).shift(RIGHT*4)
        self.play(Create(XNOR_table), run_time = 1)
        self.wait()

        # 00
        self.play(Indicate(XNOR_table.get_rows()[1][0:3]), run_time = 1)
        self.wait()

        # 01
        self.play(
            ApplyMethod(wireB.set_color, RED  , run_time = 0.1),
            ApplyMethod(wireO.set_color, WHITE, run_time = 0.1),
            ReplacementTransform(zeroB, oneB, run_time = 0.1),
            ReplacementTransform(oneO, zeroO, run_time = 0.1),
            Indicate(XNOR_table.get_rows()[2][0:3], run_time = 1),
        )
        self.wait()

        # 10
        self.play(
            ApplyMethod(wireA.set_color, RED, run_time = 0.1),
            ApplyMethod(wireB.set_color, WHITE, run_time = 0.1),
            ReplacementTransform(zeroA, oneA, run_time = 0.1),
            ReplacementTransform(oneB, zeroB_2, run_time = 0.1),
            Indicate(XNOR_table.get_rows()[3][0:3], run_time = 1),
        )
        self.wait()

        # 11
        self.play(
            ApplyMethod(wireB.set_color, RED, run_time = 0.1),
            ApplyMethod(wireO.set_color, RED, run_time = 0.1),
            ReplacementTransform(zeroB_2, oneB_2, run_time = 0.1),
            ReplacementTransform(zeroO, oneO_2, run_time = 0.1),
            Indicate(XNOR_table.get_rows()[4][0:3], run_time = 1),
        )
        self.wait()

        self.play(
            Uncreate(XNOR_table),
            Uncreate(xor_leftarc2),
            Uncreate(xor_leftarc),
            Uncreate(xor_lowarc),
            Uncreate(xor_uparc),
            Uncreate(not_cir),
            Uncreate(wireA),
            Uncreate(wireB),
            Uncreate(wireO),
            Uncreate(textA),
            Uncreate(textB),
            Uncreate(textO),
            Uncreate(oneA),
            Uncreate(oneB_2),
            Uncreate(oneO_2),
        )
        self.wait()
