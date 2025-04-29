from manim import *


R_BLACK = '#0B0500'
R_WHITE = '#F5F1FA'
R_PURPLE = '#7C64DD'
R_ORANGE = '#FFAF60'
R_BLUE = '#5FC6FF'
R_RED = '#F9648F'
R_GREEN = '#5AE592'

class RightTriangle(Scene):
    def construct(self):
        # Создаем вершины треугольника
        A = np.array([2, -1, 0])
        B = np.array([-2, -1, 0])
        C = np.array([2, 1, 0])

        # Создаем треугольник
        triangle = Polygon(A, B, C, color=R_WHITE)
        
        # Рисуем прямой угол (квадратик в вершине C)
        right_angle = Square(side_length=0.4, color=R_WHITE).move_to([1.8, -0.8, 0])
        right_angle.set_fill(R_BLUE, opacity=0.5)
        
        # Подписываем стороны
        hypotenuse_label = MathTex("n").move_to(
            Line(B, C).get_center() + rotate_vector(UP, Line(B, C).get_angle()) * 0.5
        )
        side_b_label = MathTex("m").next_to(Line(A, C), RIGHT)
        
        # Подписываем углы
        angle_C_arc1 = Angle(
            Line(C, B),
            Line(C, A),
            radius=0.7,
            color=R_RED,
        )
        angle_C_arc2 = Angle(
            Line(C, B),
            Line(C, A),
            radius=0.9,
            color=R_RED,
        )
        angle_C_label = MathTex(r"\beta").next_to(
            angle_C_arc1.point_from_proportion(0.5),
            DL,
            buff=0.2,
        )
        angle_B_arc = Angle(
            Line(B, A),
            Line(B, C),
            radius=0.6,
            other_angle=False,
            color=R_ORANGE,
        )
        angle_B_label = MathTex(r"\alpha").next_to(
            angle_B_arc.point_from_proportion(0.5),
            UR + 0.98 * DOWN + 0.7 * RIGHT,
            buff=0.15,
        )
        
        # Анимация
        self.play(Create(triangle))
        self.play(FadeIn(right_angle))
        self.play(Write(angle_B_arc), Write(angle_C_arc1), Write(angle_C_arc2), run_time=3)
        
        # Подписи сторон
        self.play(Write(hypotenuse_label), run_time=3)
        self.play(Write(side_b_label), run_time=3)
        
        # Подписи углов
        self.play(Write(angle_C_label), run_time=3)
        self.play(Write(angle_B_label), run_time=3)
        self.wait(0.1)  # Короткая пауза для фиксации кадра
        self.add(Dot().set_opacity(0))  # Невидимая точка для принудительного рендера