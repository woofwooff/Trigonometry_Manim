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

class Picture_4_5_2_2(Scene):
    def construct(self):
        # Первая сцена
        self.arcsin_scene()
        # self.wait(2)
        # self.clear()
        
        # Вторая сцена
        # self.arccos_scene()

    def arcsin_scene(self):
        # Система координат
        ax_x_range = [-2*np.pi, 2*np.pi, np.pi/2]
        ay_y_range = [-2.5, 2.5]
        ax = Axes(x_range=ax_x_range, y_range=ay_y_range, x_length=13, y_length=7, color=R_WHITE,
                axis_config={'tip_width': 0.2, 'tip_length': 0.4})
        self.play(FadeIn(ax), run_time=3)

        # Подписи к осям
        ax_labels = ax.get_axis_labels(MathTex('x'), MathTex('y'))
        self.play(Write(ax_labels), run_time=2)

        # График синуса
        sin_graph = ax.plot(lambda x: np.sin(x), x_range=ax_x_range[0:2], color=R_WHITE)
        self.play(Write(sin_graph), run_time=3)

        # Вертикальные прямые
        line_01 = Line(
            start = ax @ (-np.pi/2, ay_y_range[0]),
            end = ax @ (-np.pi/2, ay_y_range[-1]),
            color = R_WHITE,
            stroke_width = DEFAULT_STROKE_WIDTH
        )

        line_02 = Line(
            start = ax @ (np.pi/2, ay_y_range[0]),
            end = ax @ (np.pi/2, ay_y_range[-1]),
            color = R_WHITE,
            stroke_width = DEFAULT_STROKE_WIDTH
        )

        line_label_01 = MathTex("-\\frac{\\pi}{2}").next_to(
            ax @ (-np.pi/2, 0), DL, buff=0.2
        )

        line_label_02 = MathTex("\\frac{\\pi}{2}").next_to(
            ax @ (np.pi/2, 0), DR, buff=0.2
        )

        self.play(Write(line_01), run_time=2)
        self.play(Write(line_label_01), run_time=2)
        self.play(Write(line_02), run_time=2)
        self.play(Write(line_label_02), run_time=2)

        # acsin(y)
        y_value = ValueTracker(1)

        dot = Dot(color=R_RED, radius=0.08).move_to(ax @ (np.arcsin(0.8), 0))

        horizontal_line = ax.get_horizontal_line(ax @ (np.arcsin(0.8), 0), color=R_ORANGE)

        arcsin_text = MathTex(f"\\arcsin(y) = {np.arcsin(0.8):.2f}", color=R_RED).next_to(horizontal_line, DOWN)

        const_horizontal_line = Line(
            start= ax @ (ax_x_range[0], np.arcsin(0.8)),
            end= ax @ (ax_x_range[1], np.arcsin(0.8)),
            color=R_GREEN,
            stroke_width=DEFAULT_STROKE_WIDTH,
        )

        def find_intersections(y):
            solutions = []
            x = -2*np.pi

            while x <= 2*np.pi:
                try:
                    if np.isclose(np.sin(x), y, atol=0.01):
                        solutions.append(x)
                except:
                    pass
                x += 0.01
            return solutions
        
        intersection_dots = VGroup(*[
            Dot(
                ax @ (x, np.arcsin(0.8)),
                color=R_RED,
                radius=0.08,
            ) for x in find_intersections(np.arcsin(0.8))
        ])

        self.play(Write(const_horizontal_line), Write(intersection_dots), run_time=3)

        self.play(Create(dot), Create(horizontal_line), run_time=6)
        self.play(Write(arcsin_text), run_time=4)
        self.wait(0.1)  # Короткая пауза для фиксации кадра
        self.add(Dot().set_opacity(0))  # Невидимая точка для принудительного рендера

    def arccos_scene(self):
        # Система координат
        ax_x_range = [-2*np.pi, 2*np.pi, np.pi/2]
        ay_y_range = [-2.5, 2.5]
        ax = Axes(x_range=ax_x_range, y_range=ay_y_range, x_length=13, y_length=7, color=R_WHITE,
                axis_config={'tip_width': 0.2, 'tip_length': 0.4})
        self.play(FadeIn(ax), run_time=3)

        # Подписи к осям
        ax_labels = ax.get_axis_labels(MathTex('x'), MathTex('y'))
        self.play(Write(ax_labels), run_time=2)

        # График косинуса
        cos_graph = ax.plot(lambda x: np.cos(x), x_range=ax_x_range[0:2], color=R_WHITE)
        self.play(Write(cos_graph), run_time=3)

        # Вертикальные прямые
        line = Line(
            start = ax @ (np.pi, ay_y_range[0]),
            end = ax @ (np.pi, ay_y_range[-1]),
            color = R_WHITE,
            stroke_width = DEFAULT_STROKE_WIDTH
        )

        line_label = MathTex("\\pi").next_to(
            ax @ (np.pi, 0), DR, buff=0.2
        )

        self.play(Write(line), run_time=2)
        self.play(Write(line_label), run_time=2)

        # arccos(x)
        x_value = ValueTracker(1)

        dot = Dot(color=R_RED, radius=0.08).move_to(ax @ (np.arccos(0.8), 0))

        horizontal_line = ax.get_vertical_line(ax @ (np.arccos(0.8), 0), color=R_ORANGE)
        
        arccos_text = MathTex(f"\\arccos(x) = {np.arccos(0.8):.2f}", color=R_RED).next_to(horizontal_line, DOWN)

        const_horizontal_line = Line(
            start= ax @ (ax_x_range[0], np.arccos(0.8)),
            end= ax @ (ax_x_range[1], np.arccos(0.8)),
            color=R_GREEN,
            stroke_width=DEFAULT_STROKE_WIDTH,
        )

        def find_intersections(y):
            solutions = []
            x = -2*np.pi

            while x <= 2*np.pi:
                try:
                    if np.isclose(np.cos(x), y, atol=0.01):
                        solutions.append(x)
                except:
                    pass
                x += 0.01
            return solutions
        
        intersection_dots = VGroup(*[
            Dot(
                ax @ (x, np.arccos(0.8)),
                color=R_RED,
                radius=0.08,
            ) for x in find_intersections(np.arccos(0.8))
        ])

        self.play(Write(const_horizontal_line), Write(intersection_dots), run_time=3)

        self.play(Create(dot), Create(horizontal_line), run_time=6)
        self.play(Write(arccos_text), run_time=4)
        self.wait(0.1)  # Короткая пауза для фиксации кадра
        self.add(Dot().set_opacity(0))  # Невидимая точка для принудительного рендера
        