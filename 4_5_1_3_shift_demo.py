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


class ShiftDemo(Scene):
    def construct(self):

        # система координат
        ax_x_range = [-2*np.pi, 2*np.pi, np.pi/2]
        ax = Axes(x_range=ax_x_range, y_range=[-1.5, 1.5], x_length=8, y_length=7, color=R_WHITE,
                  axis_config={'tip_width': 0.2, 'tip_length': 0.4}).to_edge(LEFT)
        self.play(FadeIn(ax), run_time=3)

        # подписи к осям
        ax_labels = ax.get_axis_labels(MathTex('x'), MathTex('y'))
        self.play(Write(ax_labels), run_time=2)

        # подписи к оси x
        x_label_values = [-2, -1, 1, 2]
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

        # график y = cos(x)
        cos_graph = ax.plot(lambda x: np.cos(x), x_range=ax_x_range[0:2], color=R_WHITE)
        self.play(Write(cos_graph), run_time=3)

        # надпись функции, задающей график y = cos(x)
        cos_function_text = MathTex('y = \\cos(x)', font_size=45, color=R_WHITE).to_edge(UR)
        self.play(Write(cos_function_text), run_time=2)

        # график y = cos(x - a)
        a = ValueTracker(value=0)
        cos_graph_a = ax.plot(lambda x: np.cos(x - a.get_value()), x_range=ax_x_range[0:2], color=R_BLUE)
        self.play(FadeIn(cos_graph_a), run_time=3)

        # апдейтер для графика функции y = cos(x - a)
        cos_graph_a.add_updater(lambda x: x.become(
            ax.plot(lambda y: np.cos(y - a.get_value()), x_range=ax_x_range[0:2], color=R_BLUE)
        ))

        # анимируем сдвиг графика функции y = cos(x - a)
        self.play(a.animate.set_value(np.pi/6), run_time=3, rate_func=linear)

        # надпись функции, задающей график с параметром а
        cos_function_text_a = MathTex('y = \\cos \\left(x - \\dfrac{\\pi}{6} \\right)', font_size=45,
                                      color=R_BLUE).next_to(cos_function_text, DOWN, aligned_edge=RIGHT)
        self.play(Write(cos_function_text_a), run_time=3)
        self.wait(4)

        # уберем апдейтер графика
        cos_graph_a.clear_updaters()

        # график функции y = cos(k*(x - a))
        k = ValueTracker(value=1)
        cos_graph_k = ax.plot(lambda x: np.cos(k.get_value()*(x - a.get_value())), x_range=ax_x_range[0:2],
                                               color=R_GREEN)
        self.play(FadeIn(cos_graph_k), run_time=3)

        # апдейтер для графика функции y = cos(k*(x - a))
        cos_graph_k.add_updater(lambda x: x.become(
            ax.plot(lambda y: np.cos(k.get_value() * (y - a.get_value())), x_range=ax_x_range[0:2],
                    color=R_GREEN)
        ))

        # анимируем сдвиг графика функции y = cos(k*(x - a)), также уберем график y = cos(x)
        self.play(FadeOut(cos_graph), k.animate.set_value(2), run_time=3, rate_func=linear)

        # надпись функции, задающей график с параметром k
        cos_function_text_k = MathTex('y = \\cos \\left( 2\\left(x - \\dfrac{\\pi}{6} \\right) \\right)',
                                      font_size=45,
                                      color=R_GREEN).next_to(cos_function_text_a, DOWN, aligned_edge=RIGHT)
        self.play(Write(cos_function_text_k), run_time=3)
        self.wait(4)

        # уберем апдейтер графика
        cos_graph_k.clear_updaters()

        # график функции y = l*cos(k*(x - a))
        l = ValueTracker(value=1)
        cos_graph_l = ax.plot(lambda x: l.get_value()*np.cos(k.get_value() * (x - a.get_value())),
                              x_range=ax_x_range[0:2], color=R_ORANGE)
        self.play(FadeIn(cos_graph_l), run_time=3)

        # апдейтер для графика функции y = l*cos(k*(x - a))
        cos_graph_l.add_updater(lambda x: x.become(
            ax.plot(lambda y: l.get_value() * np.cos(k.get_value() * (y - a.get_value())),
                    x_range=ax_x_range[0:2], color=R_ORANGE)
        ))

        # анимируем сдвиг графика функции y = l*cos(k*(x - a)), также уберем график y = cos(x - a)
        self.play(FadeOut(cos_graph_a),l.animate.set_value(1/3), run_time=3, rate_func=linear)

        # надпись функции, задающей график с параметром l
        cos_function_text_l = MathTex(
            'y = \\dfrac{1}{3}\\cos \\left( 2\\left(x - \\dfrac{\\pi}{6} \\right) \\right)',
            font_size=45, color=R_ORANGE).next_to(cos_function_text_k, DOWN, aligned_edge=RIGHT
        )
        self.play(Write(cos_function_text_l), run_time=3)

        self.wait(5)