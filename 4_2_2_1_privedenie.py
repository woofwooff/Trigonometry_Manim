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

        pi2_dot = Dot(ax.c2p(0, 1), color=R_GREEN)
        pi_dot = Dot(ax.c2p(-1, 0), color=R_RED)
        pi32_dot = Dot(ax.c2p(0, -1), color=R_GREEN)
        pi22_dot = Dot(ax.c2p(1, 0), color=R_RED)
        self.play(Write(pi_dot), Write(pi22_dot), run_time=1)

        pi2_text = MathTex('\\frac{\\pi}{2}', font_size=30).move_to(ax.c2p(0.3, 1.2))
        pi_text = MathTex('\\pi', font_size=30).move_to(ax.c2p(-1.1, 0.1))
        pi32_text = MathTex('\\frac{3\\pi}{2}', font_size=30).move_to(ax.c2p(-0.3, -1.2))
        pi22_text = MathTex('2\\pi', font_size=30).move_to(ax.c2p(1.1, 0.1))

        self.play(Write(pi_text), Write(pi22_text), run_time=0.5)

        arrow = Arrow(start=ax.c2p(0, 0), end=ax.c2p(1, 0), buff=0)
        self.add(arrow)
        self.play(arrow.animate.scale(-1, about_edge=LEFT), run_time=2)

        Dontchange_text = Text('Не меняется', font_size=20, color=R_WHITE).move_to(
            ax.c2p(0.5, 0.2)
        )

        self.play(Write(Dontchange_text), run_time=1)

        self.play(FadeOut(arrow), FadeOut(Dontchange_text), FadeOut(pi_dot), FadeOut(pi22_dot), FadeOut(pi22_text), FadeOut(pi_text), run_time=1)

        self.play(Write(pi2_dot), Write(pi32_dot), run_time=1)
        self.play(Write(pi2_text), Write(pi32_text), run_time=0.5)

        arrow = Arrow(start=ax.c2p(0, 0), end=ax.c2p(0, 1), buff=0)
        self.add(arrow)
        self.play(arrow.animate.scale(-1, about_edge=DOWN), run_time=2)

        change_text = Text('Меняется', font_size=20, color=R_WHITE).move_to(
            ax.c2p(0.5, 0.2)
        )
        self.play(Write(change_text), run_time=1)

        self.wait(1)

        self.play(FadeOut(arrow), FadeOut(change_text), FadeOut(pi2_dot), FadeOut(pi32_dot), FadeOut(pi2_text), FadeOut(pi32_text), run_time=1)

        pik_text = MathTex('\\frac{\\pi}{2}k', font_size=30).move_to(ax.c2p(-1.2, 0.2))
        pik_dot = Dot(ax.c2p(-1, 0), color=R_RED)

        self.play(Write(pik_dot), Write(pik_text), run_time=1)

        sector = Sector(radius=2.35, start_angle=PI, angle=PI/2, color=BLUE, fill_color=R_BLUE, fill_opacity=0.5)

        self.play(Create(sector))

        change_text = Text('Знак Ф', font_size=20, color=R_GREEN).move_to(
            ax.c2p(-0.3, -0.3)
        )
        self.play(Write(change_text), run_time=1)

        self.wait()
