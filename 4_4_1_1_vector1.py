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
        ax = Axes(x_range=[-1.5, 1.5], y_range=[-1.5, 1.5], x_length=7, y_length=7, color=R_WHITE,
                  axis_config={'tip_width': 0.2, 'tip_length': 0.4})
        
        A_dot = Dot(ax.c2p(0, 0), color=R_GREEN)
        B_dot = Dot(ax.c2p(1, 0), color=R_GREEN)
        A_text = MathTex('A', font_size=30).move_to(ax.c2p(-0.1, 0.1))
        B_text = MathTex('B', font_size=30).move_to(ax.c2p(1.1, 0.1))
        self.play(Write(A_dot), Write(B_dot), Write(A_text), Write(B_text), run_time=1)
        arrow = Arrow(start=ax.c2p(0, 0), end=ax.c2p(1, 0), color=R_WHITE, buff=0)
        self.play(Write(arrow))

        length_line = Line(start=ax.c2p(0, 0.3), end=ax.c2p(1, 0.3), color=R_WHITE, buff=0)
        length_text = MathTex('L=|AB|', font_size=30).move_to(ax.c2p(0.5, 0.5))
        self.play(Write(length_line), Write(length_text), run_time=1)

        arrow = Arrow(start=ax.c2p(1, -0.3), end=ax.c2p(0, -0.3), color=R_WHITE, buff=0)
        A_text = MathTex('A', font_size=30).move_to(ax.c2p(-0.1, -0.2))
        B_text = MathTex('B', font_size=30).move_to(ax.c2p(1.1, -0.2))
        A_dot = Dot(ax.c2p(0, -0.3), color=R_GREEN)
        B_dot = Dot(ax.c2p(1, -0.3), color=R_GREEN)
        self.play(Write(arrow), Write(A_text), Write(B_text), Write(A_dot), Write(B_dot))

        self.wait()
