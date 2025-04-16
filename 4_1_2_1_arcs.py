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
                 lines_length: float=3,
                 angle_color: str=R_WHITE,
                 angle_arc_radius: float=0.5,
                 angle_arc_text: str=None) -> VGroup:
    center_dot = Dot((0, 0, 0), color=angle_color)

    line1 = Line(start=center_dot.get_center(),
                 end=center_dot.get_center() + lines_length*RIGHT,
                 color=angle_color)
    line1.add_updater(lambda x: x.become(
        Line(start=center_dot.get_center(),
             end=center_dot.get_center() + lines_length*RIGHT,
             color=angle_color)
    ))

    line2 = Line(start=center_dot.get_center(),
                 end=center_dot.get_center() + np.sin(angle_measure)*lines_length*UP +
                     np.cos(angle_measure)*lines_length*RIGHT,
                 color=angle_color)
    line2.add_updater(lambda x: x.become(
        Line(start=center_dot.get_center(),
             end=center_dot.get_center() + np.sin(angle_measure) * lines_length * UP +
                 np.cos(angle_measure) * lines_length * RIGHT,
             color=angle_color)
    ))

    angle_arc = Angle(line1, line2, color=angle_color, radius=angle_arc_radius)
    angle_arc.add_updater(lambda x: x.become(
        Angle(line1, line2, color=angle_color, radius=angle_arc_radius)
    ))

    if not angle_arc_text:
        angle_measure_degrees = np.rad2deg(angle_measure)
        angle_arc_text = f'{angle_measure_degrees:.0f}' + '^{\circ}'

    angle_measure_text = MathTex(angle_arc_text).move_to(
        (center_dot.get_x() + np.cos(angle_measure/2)*(angle_arc_radius + 0.5),
         center_dot.get_y() + np.sin(angle_measure/2)*(angle_arc_radius + 0.5), 0)
    )
    angle_measure_text.add_updater(lambda x: x.move_to(
        (center_dot.get_x() + np.cos(angle_measure / 2) * (angle_arc_radius + 0.5),
         center_dot.get_y() + np.sin(angle_measure / 2) * (angle_arc_radius + 0.5), 0)
    ))

    result = VGroup(center_dot, line1, line2, angle_arc, angle_measure_text)
    return result


class OddSinEvenCos(Scene):
    def construct(self):

        alpha_angle_measure = np.pi/3
        # система координат
        ax = Axes(x_range=[-1.5, 1.5], y_range=[-1.5, 1.5], x_length=7, y_length=7, color=R_WHITE,
                  axis_config={'tip_width': 0.2, 'tip_length': 0.4}).to_edge(LEFT)
        self.play(FadeIn(ax), run_time=3)

        # единичная окружность
        unit_circle = Circle.from_three_points(ax.c2p(-1, 0), ax.c2p(0, 1), ax.c2p(1, 0),
                                               color=R_RED)
        self.play(Write(unit_circle), run_time=3)

        #  угол альфа
        positive_alpha_angle = create_angle(angle_measure=alpha_angle_measure, angle_arc_text='\\alpha').to_edge(RIGHT)

        self.play(Write(positive_alpha_angle[0]), run_time=1)
        self.play(Write(positive_alpha_angle[1]), Write(positive_alpha_angle[2]), run_time=2)
        self.play(Write(positive_alpha_angle[3]), Write(positive_alpha_angle[4]), run_time=2)
        self.play(positive_alpha_angle[0].animate.move_to(ax.c2p(0, 0)), run_time=3)
        positive_alpha_angle.clear_updaters()

        y_zero_dot = Dot(ax.c2p(1, 0), color=R_GREEN)
        alpha_arc_dot = Dot(ax.c2p(np.cos(alpha_angle_measure), np.sin(alpha_angle_measure)), color=R_GREEN)
        self.play(Write(y_zero_dot), Write(alpha_arc_dot), run_time=2)
        self.play(positive_alpha_angle[3].animate.set_color(color=R_GREEN), run_time=3)

        alpha_arc = Arc(radius=unit_circle.radius, start_angle=0, angle=alpha_angle_measure,
                        arc_center=unit_circle.get_center(), color=R_GREEN)
        self.play(Write(alpha_arc), run_time=3)

        self.wait(2)