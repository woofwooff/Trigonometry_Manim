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

class Picture_4_5_2_5(Scene):
    def construct(self):
        # Система координат
        ax_x_range = [-2*np.pi, 2*np.pi, np.pi/2]
        ay_y_range = [-1.5, 3.5]
        ax = Axes(x_range=ax_x_range, y_range=ay_y_range, x_length=13, y_length=7, color=R_WHITE,
                axis_config={'tip_width': 0.2, 'tip_length': 0.4})
        self.play(FadeIn(ax), run_time=3)

        # Подписи к осям
        ax_labels = ax.get_axis_labels(MathTex('x'), MathTex('y'))
        self.play(Write(ax_labels), run_time=2)

        labels = VGroup()

        labels.add(MathTex("-\\pi").next_to(ax @ (-np.pi, 0), DOWN).scale(0.7))
        labels.add(MathTex("-1").next_to(ax @ (-1, 0), DOWN).scale(0.7))
        labels.add(MathTex("1").next_to(ax @ (1, 0), DOWN).scale(0.7))
        labels.add(MathTex("\\pi").next_to(ax @ (np.pi, 0), DOWN).scale(0.7))
        labels.add(MathTex("\\pi").next_to(ax @ (0, np.pi), LEFT).scale(0.7))
        labels.add(MathTex("1").next_to(ax @ (0, 1), LEFT).scale(0.7))
        labels.add(MathTex("-1").next_to(ax @ (0, -1), RIGHT).scale(0.7))
        labels.add(MathTex("-\\pi").next_to(ax @ (0, -np.pi), RIGHT).scale(0.7))

        self.play(Write(labels))

        # График арккосинуса
        arccos_graph = ax.plot(lambda x: np.arccos(x), x_range=[-1, 1], color=R_RED)
        self.play(Write(arccos_graph), run_time=3)
        arccos_label = ax.get_graph_label(arccos_graph, MathTex('y = arccos(x)'), x_val=-1, direction=DL + 0.9 * DOWN)
        self.play(Write(arccos_label), run_time=2)

        # График y = x
        classic_graph = ax.plot(lambda x: x, x_range=[-2, 2], color=R_GREEN)
        dashed_classic = DashedVMobject(classic_graph, num_dashes=50, color=WHITE)
        self.play(Write(dashed_classic), run_time=3)
        classic_label = ax.get_graph_label(classic_graph, MathTex('y = x'), x_val=2)
        self.play(Write(classic_label), run_time=2)

        arccos_graph_reversed = ax.plot(lambda y: np.cos(y), x_range=[0, np.pi], color=R_PURPLE)
        self.play(Write(arccos_graph_reversed), run_time=3)

        dot1 = Dot(color=R_ORANGE, radius=0.08).move_to(ax @ (-1, np.arccos(-1)))
        dot2 = Dot(color=R_ORANGE, radius=0.08).move_to(ax @ (np.pi, np.cos(np.pi)))

        line_1 = ax.get_lines_to_point(dot1.get_center(), color=R_ORANGE)
        line_2 = ax.get_lines_to_point(dot2.get_center(), color=R_ORANGE)
        self.play(Write(line_1), Write(dot1), Write(line_2), Write(dot2), run_time=3)

        self.wait(0.1)  # Короткая пауза для фиксации кадра
        self.add(Dot().set_opacity(0))  # Невидимая точка для принудительного рендера