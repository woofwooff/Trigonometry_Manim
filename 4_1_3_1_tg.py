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
        self.play(FadeIn(ax), run_time=1)

        unit_circle = Circle.from_three_points(ax.c2p(-1, 0), ax.c2p(0, 1), ax.c2p(1, 0),
                                               color=R_RED)
        self.play(Write(unit_circle), run_time=1)

        zero_dot = Dot(ax.c2p(0, 0), color=R_WHITE)
        zero_text = MathTex('M', color=R_WHITE).move_to(
            ax.c2p(0.707, 0.9)
        )
        M_dot = Dot(ax.c2p(0.707, 0.707), color=R_WHITE)
        M_text = MathTex('O', color=R_WHITE).move_to(
            ax.c2p(-0.2, -0.2)
        )
        self.play(Write(M_dot), Write(zero_dot), FadeIn(zero_text), FadeIn(M_text), run_time=1)

        tg_line = Line(start=ax.c2p(0, 0), end=ax.c2p(1.5, 1.5), color=R_BLUE)
        self.play(Write(tg_line), run_time=1)

        x_coord_line = Line(start=ax.c2p(0.707, 0.707), end=ax.c2p(0.707, 0), color=R_BLUE)
        y_coord_line = Line(start=ax.c2p(0.707, 0.707), end=ax.c2p(0, 0.707), color=R_BLUE)
        self.play(Write(x_coord_line), Write(y_coord_line), run_time=1)
        x_coord_text = MathTex('x', color=R_WHITE).move_to(
            ax.c2p(0.707, -0.2)
        )
        y_coord_text = MathTex('y', color=R_WHITE).move_to(
            ax.c2p(-0.2, 0.707)
        )
        self.play(Write(x_coord_text), Write(y_coord_text), run_time=0.5)

        bisect_line = Line(start=ax.c2p(1, -2), end=ax.c2p(1, 2), color=R_BLUE)
        bisect_point_ox = Dot(ax.c2p(1, 0), color=R_WHITE)
        bisect_point_tg = Dot(ax.c2p(1, 1), color=R_WHITE)
        self.play(Write(bisect_line), Write(bisect_point_ox), 
                  Write(bisect_point_tg), run_time=1)

        color_line = Line(start=ax.c2p(1, 0), end=ax.c2p(1, 1), color=R_GREEN)
        self.play(FadeIn(color_line), run_time=1.5)

        M_text = MathTex('\\tan{\\alpha}', color=R_WHITE).move_to(
            ax.c2p(1.3, 0.5)
        )
        self.play(FadeIn(M_text), run_time=1)


