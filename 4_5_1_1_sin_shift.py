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


class SinShifts(Scene):
    def construct(self):

        # первый параметр в функции y = sin(x + a) + b
        a = ValueTracker(value=0)

        # второй параметр в функции y = sin(x + a) + b
        b = ValueTracker(value=0)

        # система координат
        ax_x_range = [-3*np.pi, 3*np.pi, np.pi/2]
        ax = Axes(x_range=ax_x_range, y_range=[-2, 2], x_length=12, y_length=7, color=R_WHITE,
                  axis_config={'tip_width': 0.2, 'tip_length': 0.4})
        self.play(FadeIn(ax), run_time=3)

        # подписи к осям
        ax_labels = ax.get_axis_labels(MathTex('x'), MathTex('y'))
        self.play(Write(ax_labels), run_time=2)

        # подписи к оси x
        x_label_values = [-3, -2, -1, 1, 2, 3]
        x_labels = VGroup()
        for value in x_label_values:
            text_string = ''
            if value < 0:
                text_string += '-'
            if abs(value) - 1:
                text_string += str(abs(value))
            text_string += '\\pi'
            text = MathTex(text_string, color=R_WHITE, font_size=32)
            text.next_to(mobject_or_point=ax.c2p(value*np.pi, 0), direction=DOWN)
            x_labels.add(text)
        self.play(FadeIn(x_labels), run_time=3)


        # график y = sin(x)
        sin_graph = ax.plot(lambda x: np.sin(x), x_range=[-3*np.pi, 3*np.pi], color=R_WHITE)
        self.play(Write(sin_graph), run_time=3)

        # надпись функции, задающей график y = sin(x)
        sin_function = MathTex('y = \\sin(x)', color=R_WHITE).to_edge(UL)
        self.play(Write(sin_function), run_time=2)

        # график y = sin(x - a)
        sin_graph_a = ax.plot(lambda x: np.sin(x - a.get_value()), x_range=[-3*np.pi, 3*np.pi], color=R_BLUE)
        self.play(FadeIn(sin_graph_a), run_time=3)

        # надпись функции, задающей график с параметром а
        sin_function_a = MathTex('y = \\sin(x - a)', color=R_BLUE).to_edge(UR)
        self.play(Write(sin_function_a), run_time=3)
        a_note = MathTex('a = {:.2f}'.format(a.get_value()), color=R_BLUE).next_to(
            sin_function_a, direction=DOWN)

        # апдейтер для подписи параметра а
        a_note.add_updater(lambda x: x.become(
            MathTex('a = {:.2f}'.format(a.get_value()), color=R_BLUE).next_to(
                sin_function_a, direction=DOWN)
        ))
        self.play(FadeIn(a_note), run_time=2)

        # апдейтер для графика функции y = sin(x - a)
        sin_graph_a.add_updater(lambda x: x.become(
            ax.plot(lambda y: np.sin(y - a.get_value()), x_range=[-3 * np.pi, 3 * np.pi], color=R_BLUE)
        ))

        # анимируем сдвиг графика функции y = sin(x - a)
        self.play(a.animate.set_value(3), run_time=4, rate_func=linear)
        self.play(a.animate.set_value(-3), run_time=6, rate_func=linear)

        # убираем апдейтеры и ненужные элементы
        a_note.clear_updaters()
        sin_graph_a.clear_updaters()
        self.play(FadeOut(sin_graph_a), FadeOut(a_note), FadeOut(sin_function_a), run_time=2)

        # график y = sin(x) + b
        sin_graph_b = ax.plot(lambda x: np.sin(x) + b.get_value(), x_range=[-3 * np.pi, 3 * np.pi], color=R_GREEN)
        self.play(FadeIn(sin_graph_b), run_time=3)

        # надпись функции, задающей график с параметром b
        sin_function_b = MathTex('y = \\sin(x) + b', color=R_GREEN).to_edge(UR)
        self.play(Write(sin_function_b), run_time=3)
        b_note = MathTex('b = {:.2f}'.format(b.get_value()), color=R_GREEN).next_to(
            sin_function_b, direction=DOWN)

        # апдейтер для подписи параметра b
        b_note.add_updater(lambda x: x.become(
            MathTex('b = {:.2f}'.format(b.get_value()), color=R_GREEN).next_to(
                sin_function_b, direction=DOWN)
        ))
        self.play(FadeIn(b_note), run_time=2)

        # апдейтер для графика функции y = sin(x) + b
        sin_graph_b.add_updater(lambda x: x.become(
            ax.plot(lambda y: np.sin(y) + b.get_value(), x_range=[-3 * np.pi, 3 * np.pi], color=R_GREEN)
        ))

        # анимируем сдвиг графика функции y = sin(x) + b
        self.play(b.animate.set_value(1), run_time=4, rate_func=linear)
        self.play(b.animate.set_value(-1), run_time=6, rate_func=linear)

        self.wait(2)