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
                 angle_arc_radius: float=0.5) -> VGroup:
    line1 = Line(start=(0, 0, 0), end=lines_length*RIGHT, color=angle_color)
    line2 = Line(start=(0, 0, 0), end=np.sin(angle_measure)*lines_length*UP + np.cos(angle_measure)*lines_length*RIGHT,
                 color=angle_color)
    line1_dot = Dot(lines_length*RIGHT, color=angle_color)
    line2_dot = Dot(np.sin(angle_measure)*lines_length*UP + np.cos(angle_measure)*lines_length*RIGHT, color=angle_color)
    center_dot = Dot((0, 0, 0), color=angle_color)
    if angle_measure - np.pi/2:
        angle_arc = Angle(line1, line2, color=angle_color, radius=angle_arc_radius)
    else:
        angle_arc = RightAngle(line1, line2, color=angle_color)
    angle_measure_degrees = np.rad2deg(angle_measure)
    angle_measure_text = MathTex(f'{angle_measure_degrees:.0f}' + '^{\circ}').move_to(
        (np.cos(angle_measure/2)*(angle_arc_radius + 0.7), np.sin(angle_measure/2)*(angle_arc_radius + 0.7), 0)
    )
    result = VGroup(line1, line2, line1_dot, line2_dot, center_dot, angle_arc, angle_measure_text)
    return result


class AngleDemonstration(Scene):
    def construct(self):
        acute_angle1 = create_angle(angle_measure=np.pi/6).move_to((0, 0, 0))
        acute_angle2 = create_angle(angle_measure=np.pi/4).move_to((0, 0, 0))
        acute_angle3 = create_angle(angle_measure=np.pi/3).move_to((0, 0, 0))
        self.play(FadeIn(acute_angle1), run_time=2)
        self.play(acute_angle1.animate.scale(0.7).to_edge(UL), run_time=2)
        self.play(FadeIn(acute_angle2), run_time=2)
        self.play(acute_angle2.animate.scale(0.7).next_to(acute_angle1, DOWN, aligned_edge=LEFT), run_time=2)
        self.play(FadeIn(acute_angle3), run_time=2)
        self.play(acute_angle3.animate.scale(0.7).next_to(acute_angle2, DOWN, aligned_edge=LEFT), run_time=2)

        right_angle = create_angle(angle_measure=np.pi/2).move_to((0, 0, 0))
        self.play(FadeIn(right_angle), run_time=2)
        self.play(right_angle.animate.scale(0.7).to_edge(UP), run_time=2)

        obtuse_angle1 = create_angle(angle_measure=2*np.pi/3).move_to((0, 0, 0))
        obtuse_angle2 = create_angle(angle_measure=3*np.pi/4).move_to((0, 0, 0))
        obtuse_angle3 = create_angle(angle_measure=5*np.pi/6).move_to((0, 0, 0))
        self.play(FadeIn(obtuse_angle1), run_time=2)
        self.play(obtuse_angle1.animate.scale(0.7).to_edge(UR), run_time=2)
        self.play(FadeIn(obtuse_angle2), run_time=2)
        self.play(obtuse_angle2.animate.scale(0.7).next_to(obtuse_angle1, DOWN, aligned_edge=RIGHT), run_time=2)
        self.play(FadeIn(obtuse_angle3), run_time=2)
        self.play(obtuse_angle3.animate.scale(0.7).next_to(obtuse_angle2, DOWN, aligned_edge=RIGHT), run_time=2)

        straight_angle = create_angle(angle_measure=np.pi).move_to((0, 0, 0))
        self.play(FadeIn(straight_angle), run_time=2)
        self.play(straight_angle.animate.scale(0.7).move_to(DOWN), run_time=2)

        self.wait(2)
