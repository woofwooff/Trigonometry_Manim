from manim import *
import numpy as np


# цвета, которые следует использовать
R_BLACK = '#0B0500'
R_WHITE = '#F5F1FA'
R_PURPLE = '#7C64DD'
R_ORANGE = '#FFAF60'
R_BLUE = '#5FC6FF'
R_RED = '#F9648F'
R_GREEN = '#5AE592'

# дефолтная ширина линий
DEFAULT_STROKE_WIDTH = 3


class TangentLine(Scene):
    def construct(self):
        ax = Axes(x_range=[-3, 3], y_range=[-3, 3], x_length=10, y_length=10, color=R_WHITE,
                  axis_config={'tip_width': 0.2, 'tip_length': 0.4})
        
        A_dot = Dot(ax.c2p(0, 0), color=R_GREEN)
        B_dot = Dot(ax.c2p(1, 0), color=R_GREEN)
        A_text = MathTex('A', font_size=30).move_to(ax.c2p(-0.1, 0.1))
        B_text = MathTex('B', font_size=30).move_to(ax.c2p(1.1, 0.1))
        self.play(Write(A_dot), Write(B_dot), Write(A_text), Write(B_text), run_time=1)
        arrow = Arrow(start=ax.c2p(0, 0), end=ax.c2p(1, 0), color=R_WHITE, buff=0)
        self.play(Write(arrow))
        
        C_dot = Dot(ax.c2p(1, 1), color=R_GREEN)
        C_text = MathTex('C', font_size=30).move_to(ax.c2p(1.1, 1.1))
        self.play(Write(C_dot), Write(C_text))
        arrow = Arrow(start=ax.c2p(0, 0), end=ax.c2p(1, 1), color=R_WHITE, buff=0)
        self.play(Write(arrow))

        sum_dot = Dot(ax.c2p(2, 1), color=R_GREEN)
        sum_text = MathTex('AB + AC', font_size=30).move_to(ax.c2p(1.6, 1.1))
        arrow = Arrow(start=ax.c2p(0, 0), end=ax.c2p(2, 1), color=R_WHITE, buff=0)
        self.play(Write(sum_dot), Write(sum_text), Write(C_text), Write(arrow))

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        line1 = Line(start=ax.c2p(-15, 1), end=ax.c2p(15, 1), color=R_WHITE, buff=0)
        line2 = Line(start=ax.c2p(-15, 0), end=ax.c2p(15, 0), color=R_WHITE, buff=0)
        self.play(Write(line1), Write(line2), run_time=1)

        A_dot = Dot(ax.c2p(0, 1), color=R_GREEN)
        B_dot = Dot(ax.c2p(2, 1), color=R_GREEN)
        A_text = MathTex('A', font_size=30).move_to(ax.c2p(0, 1.1))
        B_text = MathTex('B', font_size=30).move_to(ax.c2p(2.1, 1.1))
        C_dot = Dot(ax.c2p(0, 0), color=R_GREEN)
        D_dot = Dot(ax.c2p(3, 0), color=R_GREEN)
        C_text = MathTex('C', font_size=30).move_to(ax.c2p(0, 0.1))
        D_text = MathTex('D', font_size=30).move_to(ax.c2p(3, 0.1))
        self.play(Write(A_dot), Write(B_dot), Write(A_text), Write(B_text), Write(C_dot), Write(D_dot), Write(C_text), Write(D_text), run_time=1)
        arrow1 = Arrow(start=ax.c2p(0, 1), end=ax.c2p(2, 1), color=R_WHITE, buff=0)
        arrow2 = Arrow(start=ax.c2p(0, 0), end=ax.c2p(3, 0), color=R_WHITE, buff=0)
        self.play(Write(arrow1), Write(arrow2))

        C1_dot = Dot(ax.c2p(-2, 1), color=R_GREEN)
        D1_dot = Dot(ax.c2p(-3, 0), color=R_GREEN)
        C1_text = MathTex('C_1', font_size=30).move_to(ax.c2p(-2, 1.1))
        D1_text = MathTex('D_1', font_size=30).move_to(ax.c2p(-3, 0.1))
        self.play(Write(C1_dot), Write(D1_dot), Write(D1_text), Write(C1_text), run_time=1)
        arrow1 = Arrow(start=ax.c2p(0, 1), end=ax.c2p(-2, 1), color=R_WHITE, buff=0)
        arrow2 = Arrow(start=ax.c2p(0, 0), end=ax.c2p(-3, 0), color=R_WHITE, buff=0)
        self.play(Write(arrow1), Write(arrow2))

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        arrow1 = Arrow(start=ax.c2p(0, 0), end=ax.c2p(1, 0), color=R_WHITE, buff=0)
        arrow2 = Arrow(start=ax.c2p(0, -0.5), end=ax.c2p(2, -0.5), color=R_WHITE, buff=0)
        arrow3 = Arrow(start=ax.c2p(0, -1), end=ax.c2p(-2, -1), color=R_WHITE, buff=0)
        self.play(Write(arrow1), Write(arrow2), Write(arrow3))
        
        arrow1_text = MathTex('\\vec{a}', font_size=30).move_to(ax.c2p(0.5, 0.1))
        arrow2_text = MathTex('\\vec{2a}', font_size=30).move_to(ax.c2p(1, -0.4))
        arrow3_text = MathTex('\\vec{-2a}', font_size=30).move_to(ax.c2p(-1, -0.9))
        self.play(Write(arrow1_text), Write(arrow2_text), Write(arrow3_text))
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        arrow1 = Arrow(start=ax.c2p(0, 0), end=ax.c2p(1, 1), color=R_WHITE, buff=0)
        arrow2 = Arrow(start=ax.c2p(0, 0), end=ax.c2p(-1, 1), color=R_WHITE, buff=0)
        arrow3 = Arrow(start=ax.c2p(0, -1), end=ax.c2p(2, 0), color=R_RED, buff=0)
        self.play(Write(arrow1), Write(arrow2), Write(arrow3))
        
        arrow1_text = MathTex('\\vec{a}', font_size=30).move_to(ax.c2p(0.6, 0.9))
        arrow2_text = MathTex('\\vec{b}', font_size=30).move_to(ax.c2p(-1.1, 1))
        arrow3_text = MathTex('\\vec{a}-\\vec{b}', font_size=30).move_to(ax.c2p(1, -0.3))
        self.play(Write(arrow1_text), Write(arrow2_text), Write(arrow3_text))
        self.play(*[FadeOut(mob) for mob in self.mobjects])




        self.wait()
