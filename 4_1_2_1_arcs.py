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
                 angle_arc_text: str=None) -> tuple[Mobject, VGroup]:
    """
    Эта функция создает угол, состоящий из двух отрезков, точки их пересечения,
    дуги окружности маленького радиуса, которой обозначен угол и подписи рядом с этой дугой.
    Также привязывает апдейтерами все перечисленные объекты к положению опорной точки (angle_pivot_point).

    :param angle_measure: Градусная мера угла в радианах.
    :param angle_pivot_point: Опорная точка, центр угла будет расположен здесь.
    :param angle_rotation: Регулирует поворот первой стороны угла относительно горизонтального положения.
        По умолчанию одна из сторон угла расположена горизонтально, положение второй стороны угла
        получается поворотом против часовой стрелки на angle_measure от первой стороны.
    :param lines_length: Длина сторон угла.
    :param angle_color: Цвет угла (один для всех элементов).
    :param angle_arc_radius: Радиус дуги окружности, которой обозначен угол.
    :param angle_arc_text: Подпись рядом с дугой окружности. По умолчанию градусная мера угла.
    :return: Опорную точку, а также VGroup состоящую из остальных вышеперечисленных объектов.
    """

    # опорная точка, вокруг которой будем все строить
    pivot_point = Dot(angle_pivot_point, color=angle_color)

    # вершина угла
    center_dot = Dot(point=pivot_point.get_center(), color=angle_color)
    center_dot.add_updater(lambda x: x.move_to(pivot_point.get_center()))

    # первая сторона угла
    line1 = Line(start=pivot_point.get_center(),
                 end=(pivot_point.get_center() + np.sin(angle_rotation)*lines_length*UP +
                      np.cos(angle_rotation)*lines_length*RIGHT),
                 color=angle_color)
    line1.add_updater(lambda x: x.become(
        Line(start=pivot_point.get_center(),
             end=(pivot_point.get_center() + np.sin(angle_rotation)*lines_length*UP +
                 np.cos(angle_rotation)*lines_length*RIGHT),
             color=angle_color)
    ))

    # вторая сторона угла
    line2 = Line(start=pivot_point.get_center(),
                 end=(pivot_point.get_center() + np.sin(angle_rotation + angle_measure)*lines_length*UP +
                      np.cos(angle_rotation + angle_measure)*lines_length*RIGHT),
                 color=angle_color)
    line2.add_updater(lambda x: x.become(
        Line(start=pivot_point.get_center(),
             end=(pivot_point.get_center() + np.sin(angle_rotation + angle_measure) * lines_length * UP +
                  np.cos(angle_rotation + angle_measure) * lines_length * RIGHT),
             color=angle_color)
    ))

    # дуга обозначающая угол
    angle_arc = Angle(line1, line2, color=angle_color, radius=angle_arc_radius)
    angle_arc.add_updater(lambda x: x.become(
        Angle(line1, line2, color=angle_color, radius=angle_arc_radius)
    ))

    # подпишем градусную меру угла, в случае если подпись отсутствует
    if not angle_arc_text:
        angle_measure_degrees = np.rad2deg(angle_measure)
        angle_arc_text = f'{angle_measure_degrees:.0f}' + '^{\circ}'

    # подпись к дуге угла
    angle_measure_text = MathTex(angle_arc_text).move_to(
        (pivot_point.get_center() + np.sin(angle_rotation + angle_measure*0.5)*(angle_arc_radius + 0.5)*UP +
         np.cos(angle_rotation + angle_measure*0.5)*(angle_arc_radius + 0.5)*RIGHT)
    )
    angle_measure_text.add_updater(lambda x: x.move_to(
        (pivot_point.get_center() + np.sin(angle_rotation + angle_measure*0.5) * (angle_arc_radius + 0.5) * UP +
         np.cos(angle_rotation + angle_measure * 0.5) * (angle_arc_radius + 0.5) * RIGHT)
    ))

    result = VGroup(center_dot, line1, line2, angle_arc, angle_measure_text)
    return pivot_point, result


class Arcs(Scene):
    def construct(self):

        # система координат
        ax = Axes(x_range=[-1.5, 1.5], y_range=[-1.5, 1.5], x_length=7, y_length=7, color=R_WHITE,
                  axis_config={'tip_width': 0.2, 'tip_length': 0.4}).to_edge(LEFT)
        self.play(FadeIn(ax), run_time=3)

        # единичная окружность
        unit_circle = Circle.from_three_points(ax.c2p(-1, 0), ax.c2p(0, 1), ax.c2p(1, 0),
                                               color=R_RED)
        self.play(Write(unit_circle), run_time=3)

        #  угол альфа
        alpha_angle_measure = np.pi/3
        alpha_angle_pivot, positive_alpha_angle = create_angle(angle_measure=alpha_angle_measure,
                                                               angle_pivot_point=(3, 0, 0),
                                                               angle_arc_text='\\alpha')

        # отрисовка угла альфа
        self.play(Write(positive_alpha_angle[0]),
                  Write(positive_alpha_angle[1]),
                  Write(positive_alpha_angle[2]),
                  run_time=2)
        self.play(Write(positive_alpha_angle[3]), Write(positive_alpha_angle[4]), run_time=2)
        self.play(alpha_angle_pivot.animate.move_to(ax.c2p(0, 0)), run_time=3)
        positive_alpha_angle.clear_updaters()

        # отметили точки пересечения угла с окружностью
        y_zero_dot = Dot(ax.c2p(1, 0), color=R_GREEN)
        alpha_arc_dot = Dot(ax.c2p(np.cos(alpha_angle_measure), np.sin(alpha_angle_measure)), color=R_GREEN)
        self.play(Write(y_zero_dot), Write(alpha_arc_dot), run_time=2)
        self.play(positive_alpha_angle[3].animate.set_color(color=R_GREEN), run_time=3)

        # дуга альфа на окружности
        alpha_arc = Arc(radius=unit_circle.radius, start_angle=0, angle=alpha_angle_measure,
                        arc_center=unit_circle.get_center(), color=R_GREEN)
        self.play(FadeIn(alpha_arc), run_time=3)

        # подпись к дуге альфа на окружности
        alpha_arc_text = MathTex('\\alpha', color=R_GREEN).move_to(
            ax.c2p(
                np.cos(alpha_angle_measure / 2) * (1 + 0.15),
                np.sin(alpha_angle_measure / 2) * (1 + 0.15))
        )
        self.play(FadeIn(alpha_arc_text), run_time=3)

        # угол бета
        beta_angle_measure = np.pi / 4
        beta_angle_pivot, negative_beta_angle = create_angle(angle_measure=beta_angle_measure,
                                                             angle_pivot_point=(3, 0, 0),
                                                             angle_rotation=-beta_angle_measure,
                                                             angle_arc_text='\\beta')

        # отрисовка угла бета
        self.play(Write(negative_beta_angle[0]),
                  Write(negative_beta_angle[1]),
                  Write(negative_beta_angle[2]),
                  run_time=2)
        self.play(Write(negative_beta_angle[3]), Write(negative_beta_angle[4]), run_time=2)
        self.play(beta_angle_pivot.animate.move_to(ax.c2p(0, 0)), run_time=3)
        negative_beta_angle.clear_updaters()

        # отметили точки пересечения угла с окружностью
        y_zero_dot2 = Dot(ax.c2p(1, 0), color=R_BLUE)
        beta_arc_dot = Dot(ax.c2p(np.cos(-beta_angle_measure), np.sin(-beta_angle_measure)), color=R_BLUE)
        self.play(Write(y_zero_dot2), Write(beta_arc_dot), run_time=2)

        # замена надписи угла бета
        new_beta_text = MathTex('-\\beta', color=R_BLUE).move_to(negative_beta_angle[-1].get_center())
        self.play(Transform(negative_beta_angle[-1], new_beta_text),
                  negative_beta_angle[3].animate.set_color(color=R_BLUE), run_time=3)

        # дуга бета на окружности
        beta_arc = Arc(radius=unit_circle.radius,
                       start_angle=0,
                       angle=beta_angle_measure,
                       arc_center=unit_circle.get_center(),
                       color=R_BLUE).rotate(angle=-beta_angle_measure, about_point=unit_circle.get_center())
        self.play(FadeIn(beta_arc), run_time=3)

        # подпись к дуге бета на окружности
        beta_arc_text = MathTex('-\\beta', color=R_BLUE).move_to(
            ax.c2p(
                np.cos(-beta_angle_measure/2) * (1 + 0.15),
                np.sin(-beta_angle_measure/2) * (1 + 0.15))
        )
        self.play(FadeIn(beta_arc_text), run_time=3)

        self.wait(2)
