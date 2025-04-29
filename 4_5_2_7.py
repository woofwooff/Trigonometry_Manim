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

class Picture_4_5_2_7(Scene):
    def construct(self):
        # Система координат
        ax_x_range = [-2*np.pi, 2*np.pi, np.pi/2]
        ay_y_range = [-np.pi, np.pi]
        ax = Axes(x_range=ax_x_range, y_range=ay_y_range, x_length=13, y_length=7, color=R_WHITE,
                axis_config={'tip_width': 0.2, 'tip_length': 0.4})
        self.play(FadeIn(ax), run_time=3)

        # Подписи к осям
        ax_labels = ax.get_axis_labels(MathTex('x'), MathTex('y'))
        self.play(Write(ax_labels), run_time=2)

        labels = VGroup()

        labels.add(MathTex("\\pi").next_to(ax @ (np.pi, 0), DOWN).scale(0.7))
        labels.add(MathTex("\\pi").next_to(ax @ (0, np.pi), LEFT).scale(0.7))

        self.play(Write(labels))

        # График арккотангенса
        def arccot(x):
            return np.pi / 2 - np.arctan(x)

        def cot(x):
            return 1 / np.tan(x) if np.abs(np.sin(x)) > 1e-6 else np.nan

        arcctan_graph = ax.plot(arccot, x_range=[-np.pi, np.pi], color=R_RED)
        self.play(Write(arcctan_graph), run_time=3)
        arcctan_label = ax.get_graph_label(arcctan_graph, MathTex('y = arcctan(x)'), x_val=-1, direction=DL + 0.9 * DOWN + 0.9 * LEFT)
        self.play(Write(arcctan_label), run_time=2)

        # График y = x
        classic_graph = ax.plot(lambda x: x, x_range=[-2, 2], color=R_GREEN)
        dashed_classic = DashedVMobject(classic_graph, num_dashes=50, color=WHITE)
        self.play(Write(dashed_classic), run_time=3)
        classic_label = ax.get_graph_label(classic_graph, MathTex('y = x'), x_val=2)
        self.play(Write(classic_label), run_time=2)

        arcctan_graph_reversed = ax.plot(cot, x_range=[0.3, 2.9], color=R_PURPLE)
        self.play(Write(arcctan_graph_reversed), run_time=3)

        x_positions = [np.pi]
        y_positions = [np.pi]

        dashed_vert_lines = [
        DashedLine(
            start=ax @ (x, -2*np.pi),
            end=ax @ (x, 2*np.pi),
            color=R_ORANGE,
        ) for x in x_positions
        ]
        
        dashed_horiz_lines = [
        DashedLine(
            start=ax @ (-2*np.pi, y),
            end=ax @ (2*np.pi, y),
            color=R_ORANGE,
        ) for y in y_positions
        ]

        self.play(*[Create(line) for line in dashed_vert_lines])
        self.play(*[Create(line) for line in dashed_horiz_lines])

        self.wait(0.1)  # Короткая пауза для фиксации кадра
        self.add(Dot().set_opacity(0))  # Невидимая точка для принудительного рендера