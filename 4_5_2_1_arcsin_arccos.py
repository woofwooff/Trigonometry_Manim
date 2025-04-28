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


def create_angle(angle_measure: float,
                 angle_pivot_point: tuple[float, float, float] = (0, 0, 0),
                 angle_rotation: float=0,
                 lines_length: float=3,
                 angle_color: str=R_WHITE,
                 angle_arc_radius: float=0.5,
                 include_arc_text: bool=True,
                 angle_arc_text: str=None) -> VGroup:
    """
    Эта функция создает угол, состоящий из двух отрезков, точки их пересечения, двух точек на концах этих отрезков,
    дуги окружности маленького радиуса, которой обозначен угол и подписи рядом с этой дугой.


    :param angle_measure: Градусная мера угла в радианах.
    :param angle_pivot_point: Опорная точка, центр угла будет расположен здесь.
    :param angle_rotation: Регулирует поворот первой стороны угла относительно горизонтального положения.
        По умолчанию одна из сторон угла расположена горизонтально, положение второй стороны угла
        получается поворотом против часовой стрелки на angle_measure от первой стороны.
    :param lines_length: Длина сторон угла.
    :param angle_color: Цвет угла (один для всех элементов).
    :param angle_arc_radius: Радиус дуги окружности, которой обозначен угол.
    :param include_arc_text: Позволяет регулировать наличие подписи угла. По умолчанию подпись есть.
    :param angle_arc_text: Подпись рядом с дугой окружности. По умолчанию градусная мера угла.
    :return: VGroup состоящую из всех вышеперечисленных объектов.
    """

    # вершина угла
    center_dot = Dot(point=angle_pivot_point, color=angle_color)

    # первая сторона угла
    line1 = Line(start=angle_pivot_point,
                 end=(angle_pivot_point + np.sin(angle_rotation)*lines_length*UP +
                      np.cos(angle_rotation)*lines_length*RIGHT),
                 color=angle_color)

    # точка на конце первой стороны
    line1_dot = Dot((angle_pivot_point + np.sin(angle_rotation)*lines_length*UP +
                      np.cos(angle_rotation)*lines_length*RIGHT), color=angle_color)

    # вторая сторона угла
    line2 = Line(start=angle_pivot_point,
                 end=(angle_pivot_point + np.sin(angle_rotation + angle_measure)*lines_length*UP +
                      np.cos(angle_rotation + angle_measure)*lines_length*RIGHT),
                 color=angle_color)

    # точка на конце второй стороны
    line2_dot = Dot((angle_pivot_point + np.sin(angle_rotation + angle_measure)*lines_length*UP +
                      np.cos(angle_rotation + angle_measure)*lines_length*RIGHT), color=angle_color)

    # дуга обозначающая угол
    angle_arc = Angle(line1, line2, color=angle_color, radius=angle_arc_radius)

    result = VGroup(center_dot, line1, line2, line1_dot, line2_dot, angle_arc)

    if include_arc_text:
        # подпишем градусную меру угла, в случае если подпись отсутствует
        if not angle_arc_text:
            angle_measure_degrees = np.rad2deg(angle_measure)
            angle_arc_text = f'{angle_measure_degrees:.0f}' + '^{\circ}'

        # подпись к дуге угла
        angle_measure_text = MathTex(angle_arc_text, color=angle_color).move_to(
            (angle_pivot_point + np.sin(angle_rotation + angle_measure*0.5)*(angle_arc_radius + 0.5)*UP +
             np.cos(angle_rotation + angle_measure*0.5)*(angle_arc_radius + 0.5)*RIGHT)
        )
        result.add(angle_measure_text)

    return result


class ArcsinArccos(Scene):
    def construct(self):

        # система координат
        ax = Axes(x_range=[-1.5, 1.5], y_range=[-1.5, 1.5], x_length=7, y_length=7, color=R_WHITE,
                  axis_config={'tip_width': 0.2, 'tip_length': 0.4})
        self.play(FadeIn(ax), run_time=3)

        # единичная окружность
        unit_circle = Circle.from_three_points(ax.c2p(-1, 0), ax.c2p(0, 1), ax.c2p(1, 0),
                                               color=R_RED)
        self.play(Write(unit_circle), run_time=3)

        # горизонтальная линия
        y_value = 0.67
        horizontal_line = ax.plot(lambda x: y_value, x_range=[-1.5, 1.5], color=R_WHITE)
        self.play(Write(horizontal_line), run_time=3)

        # подпись к горизонтальной линии
        horizontal_line_text = MathTex('y = {}'.format(y_value)).next_to(horizontal_line.get_right(), UP)
        self.play(FadeIn(horizontal_line_text), run_time=3)

        # линия соответствующая синусу на оси y и точки на её концах
        zero_zero_dot = Dot(ax.c2p(0, 0), color=R_GREEN)
        y_sin_dot = Dot(ax.c2p(0, y_value), color=R_GREEN)
        y_sin_line = Line(start=ax.c2p(0, 0), end=ax.c2p(0, y_value), color=R_GREEN)
        self.play(Write(y_sin_line), Write(zero_zero_dot), Write(y_sin_dot), run_time=3)

        # нарисуем несколько углов с подходящим синусом угла
        lines_length = float(ax.c2p(1, 0)[0]) - float(ax.c2p(0, 0)[0])

        # первый угол
        first_angle_measure = np.arcsin(y_value)
        first_angle = create_angle(angle_measure=first_angle_measure,
                                   lines_length=lines_length,
                                   angle_arc_text='\\alpha',
                                   angle_arc_radius=lines_length,
                                   angle_color=R_ORANGE)
        self.play(Write(first_angle[0]),
                  Write(first_angle[1]),
                  Write(first_angle[2]),
                  Write(first_angle[3]),
                  Write(first_angle[4]),
                  run_time=3)
        self.play(Write(first_angle[5]), Write(first_angle[6]), run_time=3)

        # второй угол
        second_angle_measure = np.pi - np.arcsin(y_value)
        second_angle = create_angle(angle_measure=second_angle_measure,
                                    lines_length=lines_length,
                                    angle_arc_text='\\beta',
                                    angle_arc_radius=lines_length,
                                    angle_color=R_PURPLE)
        self.play(Write(second_angle[0]),
                  Write(second_angle[1]),
                  Write(second_angle[2]),
                  Write(second_angle[3]),
                  Write(second_angle[4]),
                  run_time=3)
        self.play(Write(second_angle[5]), Write(second_angle[6]), run_time=3)

        # третий угол
        third_angle_measure = np.pi + np.arcsin(y_value)
        third_angle = create_angle(angle_measure=third_angle_measure,
                                   angle_rotation=np.pi - np.arcsin(y_value),
                                   lines_length=lines_length,
                                   angle_arc_text='\\gamma',
                                   angle_arc_radius=lines_length,
                                   angle_color=R_BLUE)
        self.play(Write(third_angle[0]),
                  Write(third_angle[1]),
                  Write(third_angle[2]),
                  Write(third_angle[3]),
                  Write(third_angle[4]),
                  run_time=3)
        self.play(Write(third_angle[5]), Write(third_angle[6]), run_time=3)

        # надпись arcsin y = ?
        arcsin_text_1 = MathTex('y = \\sin(\\alpha) = \\sin(\\beta) = \\sin(\\gamma)',
                              color=R_WHITE, font_size=40).to_edge(UL)
        arcsin_text_2 = MathTex('\\arcsin(y) = ???', font_size=45).next_to(arcsin_text_1, DOWN, aligned_edge=LEFT)
        self.play(Write(arcsin_text_1), run_time=3)
        self.wait(2)
        self.play(Write(arcsin_text_2), run_time=3)
        self.wait(2)

        # уберем лишние элементы
        self.play(FadeOut(first_angle), FadeOut(second_angle), FadeOut(third_angle),
                  FadeOut(zero_zero_dot), FadeOut(y_sin_dot), FadeOut(y_sin_line), run_time=3)

        # выделим дугу, соответствующую области значений арксинуса
        arcsin_values = create_angle(angle_measure=np.pi,
                                     angle_rotation=-np.pi/2,
                                     lines_length=lines_length,
                                     angle_arc_radius=lines_length,
                                     angle_color=R_GREEN,
                                     include_arc_text=False)
        self.play(Write(arcsin_values[0]),
                  Write(arcsin_values[1]),
                  Write(arcsin_values[2]),
                  Write(arcsin_values[3]),
                  Write(arcsin_values[4]),
                  run_time=3)
        self.play(Write(arcsin_values[5]), run_time=3)
        self.wait(4)

        # отметим границы нарисованной дуги
        top_mark = MathTex('\\dfrac{\\pi}{2}', color=R_WHITE, font_size=40).next_to(
            ax.c2p(0, 1), UR
        )
        bottom_mark = MathTex('-\\dfrac{\\pi}{2}', color=R_WHITE, font_size=40).next_to(
            ax.c2p(0, -1), DR
        )
        self.play(Write(top_mark), Write(bottom_mark), run_time=3)

        # отметим арксинус x и подпишем x = alpha
        self.play(FadeIn(first_angle), run_time=3)
        arcsin_conclusion = MathTex('\\arcsin(y) = \\alpha', color=R_ORANGE).next_to(
            ax.c2p(1, 0), DR, aligned_edge=LEFT
        )
        self.play(Write(arcsin_conclusion), run_time=3)

        # уберем всё ненужное
        self.play(FadeOut(arcsin_text_1), FadeOut(arcsin_text_2), FadeOut(top_mark), FadeOut(bottom_mark),
                  FadeOut(arcsin_values), FadeOut(arcsin_conclusion), FadeOut(first_angle), FadeOut(horizontal_line),
                  FadeOut(horizontal_line_text), run_time=3)
        self.wait(3)

        # теперь то же самое для косинуса

        # вертикальная линия
        x_value = 0.53
        vertical_line = Line(start=ax.c2p(x_value, -1.5), end=ax.c2p(x_value, 1.5), color=R_WHITE)
        self.play(Write(vertical_line), run_time=3)

        # подпись к вертикальной линии
        vertical_line_text = MathTex('x = {}'.format(x_value)).next_to(vertical_line.get_top(), DR)
        self.play(FadeIn(vertical_line_text), run_time=3)

        # линия соответствующая косинусу на оси x и точки на её концах
        zero_zero_dot = Dot(ax.c2p(0, 0), color=R_GREEN)
        x_cos_dot = Dot(ax.c2p(x_value, 0), color=R_GREEN)
        x_cos_line = Line(start=ax.c2p(0, 0), end=ax.c2p(x_value, 0), color=R_GREEN)
        self.play(Write(x_cos_line), Write(zero_zero_dot), Write(x_cos_dot), run_time=3)

        # нарисуем несколько углов с подходящим косинусом угла
        lines_length = float(ax.c2p(1, 0)[0]) - float(ax.c2p(0, 0)[0])

        # первый угол, также уберем линию, выделяющую косинус
        cos_first_angle_measure = np.arccos(x_value)
        cos_first_angle = create_angle(angle_measure=cos_first_angle_measure,
                                   lines_length=lines_length,
                                   angle_arc_text='\\alpha',
                                   angle_arc_radius=lines_length,
                                   angle_color=R_ORANGE)
        self.play(Write(cos_first_angle[0]),
                  Write(cos_first_angle[1]),
                  Write(cos_first_angle[2]),
                  Write(cos_first_angle[3]),
                  Write(cos_first_angle[4]),
                  FadeOut(zero_zero_dot),
                  FadeOut(x_cos_dot),
                  FadeOut(x_cos_line),
                  run_time=3)
        self.play(Write(cos_first_angle[5]), Write(cos_first_angle[6]), run_time=3)

        # второй угол
        cos_second_angle_measure = 2*np.pi - np.arccos(x_value)
        cos_second_angle = create_angle(angle_measure=cos_second_angle_measure,
                                    lines_length=lines_length,
                                    angle_arc_text='\\beta',
                                    angle_arc_radius=lines_length,
                                    angle_color=R_PURPLE)
        self.play(Write(cos_second_angle[0]),
                  Write(cos_second_angle[1]),
                  Write(cos_second_angle[2]),
                  Write(cos_second_angle[3]),
                  Write(cos_second_angle[4]),
                  run_time=3)
        self.play(Write(cos_second_angle[5]), Write(cos_second_angle[6]), run_time=3)

        # третий угол
        cos_third_angle_measure = np.arccos(x_value)
        cos_third_angle = create_angle(angle_measure=cos_third_angle_measure,
                                   angle_rotation=-np.arccos(x_value),
                                   lines_length=lines_length,
                                   angle_arc_text='\\gamma',
                                   angle_arc_radius=lines_length,
                                   angle_color=R_BLUE)
        self.play(Write(cos_third_angle[0]),
                  Write(cos_third_angle[1]),
                  Write(cos_third_angle[2]),
                  Write(cos_third_angle[3]),
                  Write(cos_third_angle[4]),
                  run_time=3)
        self.play(Write(cos_third_angle[5]), Write(cos_third_angle[6]), run_time=3)

        # надпись arccos x = ?
        arccos_text_1 = MathTex('x = \\cos(\\alpha) = \\cos(\\beta) = \\cos(\\gamma)',
                                color=R_WHITE, font_size=40).to_edge(UL)
        arccos_text_2 = MathTex('\\arccos(x) = ???', font_size=45).next_to(arcsin_text_1, DOWN,
                                                                           aligned_edge=LEFT)
        self.play(Write(arccos_text_1), run_time=3)
        self.wait(2)
        self.play(Write(arccos_text_2), run_time=3)
        self.wait(2)

        # уберем лишние элементы
        self.play(FadeOut(cos_first_angle), FadeOut(cos_second_angle), FadeOut(cos_third_angle),
                  FadeOut(zero_zero_dot), FadeOut(x_cos_dot), FadeOut(x_cos_line), run_time=3)

        # выделим дугу, соответствующую области значений арккосинуса
        arccos_values = create_angle(angle_measure=np.pi,
                                     lines_length=lines_length,
                                     angle_arc_radius=lines_length,
                                     angle_color=R_GREEN,
                                     include_arc_text=False)
        self.play(Write(arccos_values[0]),
                  Write(arccos_values[1]),
                  Write(arccos_values[2]),
                  Write(arccos_values[3]),
                  Write(arccos_values[4]),
                  run_time=3)
        self.play(Write(arccos_values[5]), run_time=3)
        self.wait(4)

        # отметим границы нарисованной дуги
        left_mark = MathTex('\\pi', color=R_WHITE, font_size=40).next_to(
            ax.c2p(-1, 0), UL
        )
        right_mark = MathTex('0', color=R_WHITE, font_size=40).next_to(
            ax.c2p(1, 0), UR
        )
        self.play(Write(left_mark), Write(right_mark), run_time=3)

        # отметим арккосинус x и подпишем x = alpha
        self.play(FadeIn(cos_first_angle), run_time=3)
        arccos_conclusion = MathTex('\\arccos(x) = \\alpha', color=R_ORANGE).next_to(
            ax.c2p(1, 0), DR, aligned_edge=LEFT
        )
        self.play(Write(arccos_conclusion), run_time=3)
        self.wait(3)
