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


class SinStretch(Scene):
    def construct(self):

        # первый параметр в функции y = l*sin(kx)
        l = ValueTracker(value=1)

        # второй параметр в функции y = l*sin(kx)
        k = ValueTracker(value=1)

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

        # график y = sin(k*x)
        sin_graph_k = ax.plot(lambda x: np.sin(k.get_value()*x), x_range=[-3*np.pi, 3*np.pi], color=R_BLUE)
        self.play(FadeIn(sin_graph_k), run_time=3)

        # надпись функции, задающей график с параметром k
        sin_function_k = MathTex('y = \\sin(kx)', color=R_BLUE).to_edge(UR)
        self.play(Write(sin_function_k), run_time=3)
        k_note = MathTex('k = {:.2f}'.format(k.get_value()), color=R_BLUE).next_to(
            sin_function_k, direction=DOWN)

        # апдейтер для подписи параметра k
        k_note.add_updater(lambda x: x.become(
            MathTex('k = {:.2f}'.format(k.get_value()), color=R_BLUE).next_to(
                sin_function_k, direction=DOWN)
        ))
        self.play(FadeIn(k_note), run_time=2)

        # апдейтер для графика функции y = sin(kx)
        sin_graph_k.add_updater(lambda x: x.become(
            ax.plot(lambda y: np.sin(k.get_value()*y), x_range=[-3 * np.pi, 3 * np.pi], color=R_BLUE)
        ))

        # анимируем сдвиг графика функции y = sin(kx)
        self.play(k.animate.set_value(2), run_time=4, rate_func=linear)
        self.play(k.animate.set_value(0.25), run_time=6, rate_func=linear)

        # убираем апдейтеры и ненужные элементы
        k_note.clear_updaters()
        sin_graph_k.clear_updaters()
        self.play(FadeOut(sin_graph_k), FadeOut(k_note), FadeOut(sin_function_k), run_time=2)

        # график y = l*sin(x)
        sin_graph_l = ax.plot(lambda x: l.get_value()*np.sin(x), x_range=[-3 * np.pi, 3 * np.pi], color=R_GREEN)
        self.play(FadeIn(sin_graph_l), run_time=3)

        # надпись функции, задающей график с параметром l
        sin_function_l = MathTex('y = l\\sin(x)', color=R_GREEN).to_edge(UR)
        self.play(Write(sin_function_l), run_time=3)
        l_note = MathTex('l = {:.2f}'.format(l.get_value()), color=R_GREEN).next_to(
            sin_function_l, direction=DOWN)

        # апдейтер для подписи параметра l
        l_note.add_updater(lambda x: x.become(
            MathTex('l = {:.2f}'.format(l.get_value()), color=R_GREEN).next_to(
                sin_function_l, direction=DOWN)
        ))
        self.play(FadeIn(l_note), run_time=2)

        # апдейтер для графика функции y = lsin(x)
        sin_graph_l.add_updater(lambda x: x.become(
            ax.plot(lambda y: l.get_value()*np.sin(y), x_range=[-3 * np.pi, 3 * np.pi], color=R_GREEN)
        ))

        # анимируем сдвиг графика функции y = lsin(x)
        self.play(l.animate.set_value(2), run_time=4, rate_func=linear)
        self.play(l.animate.set_value(0.25), run_time=6, rate_func=linear)

        self.wait(2)