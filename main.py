from manim import *
import numpy as np


class Test(Scene):
    def construct(self):

        # трекер угла альфа нужен для анимации изменения этого угла
        alpha = ValueTracker(value=1)

        # трекер для доли диаметра маленькой дуги угла альфа по сравнению с радиусом единичной окружности,
        # нужен для анимации расширения этой арки до радиуса окружности
        alpha_arc_radius_scale = ValueTracker(value=0.2)

        # система координат
        ax = Axes(x_range=[-1.5, 1.5], y_range=[-1.5, 1.5], x_length=7, y_length=7,
                  axis_config={'tip_width': 0.2, 'tip_length': 0.4})
        self.play(FadeIn(ax), run_time=3)

        # единичная окружность
        unit_circle = Circle.from_three_points(ax.c2p(-1, 0), ax.c2p(0, 1), ax.c2p(1, 0),
                                               color=RED)
        self.play(Write(unit_circle), run_time=3)

        # точки (0, 0) и (1, 0) соответственно
        zero_dot = Dot(ax.c2p(0, 0))
        y_zero_dot = Dot(ax.c2p(1, 0))
        self.play(Write(y_zero_dot), Write(zero_dot), run_time=3)

        # линия, отсекающая угол альфа в положительном направлении
        positive_alpha_line = Line(start=ax.c2p(0, 0),
                                   end=ax.c2p(2*np.cos(alpha.get_value()), 2*np.sin(alpha.get_value())),
                                   color='#0099FF', buff=zero_dot.radius)
        # линия y=0
        y_zero_line = Line(start=ax.c2p(0, 0), end=ax.c2p(1, 0), color='#0099FF',
                           buff=zero_dot.radius)
        self.play(Write(positive_alpha_line), Write(y_zero_line), run_time=3)

        # дуга, обозначающая градусную меру угла альфа
        positive_alpha_arc = Arc(radius=alpha_arc_radius_scale.get_value() * unit_circle.radius, start_angle=0,
                                 angle=alpha.get_value()%(2*np.pi), arc_center=unit_circle.get_center(),
                                 color='#0099FF')
        self.play(Write(positive_alpha_arc), run_time=3)

        # подпись к дуге альфа
        positive_alpha_text = MathTex('\\alpha').move_to(
            ax.c2p(
                np.cos(alpha.get_value()%(2*np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15),
                np.sin(alpha.get_value()%(2*np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15)
            )
        )
        self.play(FadeIn(positive_alpha_text), run_time=3)

        # точка пересечения линии отсекающей угол альфа и единичной окружности
        positive_alpha_dot = Dot(ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value())))
        self.play(Write(positive_alpha_dot))

        # укорачиваем альфа линию до размера окружности
        self.play(positive_alpha_line.animate.become(
            Line(start=ax.c2p(0, 0), end=ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value())),
                 color='#0099FF', buff=zero_dot.radius)),
            run_time=3
        )

        # красим в белый все нарисованные элементы, кроме окружности.
        self.play(positive_alpha_arc.animate.set_color(WHITE),
                  positive_alpha_line.animate.set_color(WHITE),
                  y_zero_line.animate.set_color(WHITE),
                  run_time=3)

        # перпендикуляры, опущенные из точки на окружности, соответствующей углу альфа на оси x и y соответственно
        perpendicular_to_x_from_alpha_dot = Line(start=ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value())),
                                            end=ax.c2p(np.cos(alpha.get_value()), 0),
                                            color='#0099FF', buff=zero_dot.radius)
        perpendicular_to_y_from_alpha_dot = Line(start=ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value())),
                                            end=ax.c2p(0, np.sin(alpha.get_value())),
                                            color='#0099FF', buff=zero_dot.radius)

        # точки пересечения перпендикуляров с осями
        perpendicular_to_x_dot = Dot(ax.c2p(np.cos(alpha.get_value()), 0), color='#0099FF')
        perpendicular_to_y_dot = Dot(ax.c2p(0, np.sin(alpha.get_value())), color='#0099FF')



        # отрезки соответствующие синусу альфа и косинусу альфа
        sin_alpha = Line(start=ax.c2p(0, 0), end=ax.c2p(0, np.sin(alpha.get_value())),
                         color='#42F54B', buff=zero_dot.radius)
        cos_alpha = Line(start=ax.c2p(0, 0), end=ax.c2p(np.cos(alpha.get_value()), 0),
                         color='#BA34EB', buff=zero_dot.radius)

        # подписи для отрезков синуса и косинуса альфа
        sin_alpha_text = MathTex('\\sin{\\alpha}', color='#42F54B').next_to(sin_alpha, LEFT)
        cos_alpha_text = MathTex('\\cos{\\alpha}', color='#BA34EB').next_to(cos_alpha, DOWN)

        # рисуем один перпендикуляр и точку его пересечения с осью
        self.play(Write(perpendicular_to_x_from_alpha_dot), FadeIn(perpendicular_to_x_dot), run_time=3)
        # отмечаем отрезок, соответствующий тригонометрической функции, вместе с подписью
        self.play(Write(cos_alpha), FadeIn(cos_alpha_text), run_time=3)
        # то же самое для второго перпендикуляра
        self.play(Write(perpendicular_to_y_from_alpha_dot), FadeIn(perpendicular_to_y_dot), run_time=3)
        self.play(Write(sin_alpha), FadeIn(sin_alpha_text), run_time=3)

        # добавляем апдейтеры для анимации изменения угла альфа

        # апдейтер для линии угла альфа
        positive_alpha_line.add_updater(
            lambda x: x.become(
                Line(start=ax.c2p(0, 0),
                     end=ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value())),
                     buff=zero_dot.radius)
            )
        )

        # апдейтер для точки пересечения этой линии с окружностью
        positive_alpha_dot.add_updater(lambda x: x.move_to(
            ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value()))
        ))

        # апдейтер для дуги угла альфа
        positive_alpha_arc.add_updater(lambda x: x.become(
            Arc(radius=alpha_arc_radius_scale.get_value() * unit_circle.radius, start_angle=0,
                angle=alpha.get_value()%(2*np.pi), arc_center=unit_circle.get_center())
        ))

        # апдейтер для подписи дуги альфа
        positive_alpha_text.add_updater(lambda x: x.move_to(
            ax.c2p(
                np.cos(alpha.get_value()%(2*np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15),
                np.sin(alpha.get_value()%(2*np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15)
            )
        ))

        # апдейтер для х_перпендикуляра
        perpendicular_to_x_from_alpha_dot.add_updater(lambda x: x.become(
            Line(start=ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value())),
                 end=ax.c2p(np.cos(alpha.get_value()), 0),
                 color='#0099FF', buff=zero_dot.radius)
        ))

        # апдейтер для y_перпендикуляра
        perpendicular_to_y_from_alpha_dot.add_updater(lambda x: x.become(
            Line(start=ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value())),
                 end=ax.c2p(0, np.sin(alpha.get_value())),
                 color='#0099FF', buff=zero_dot.radius)
        ))

        # апдейтер для точки пересечения x_перпендикуляра с осью
        perpendicular_to_x_dot.add_updater(lambda x: x.move_to(ax.c2p(np.cos(alpha.get_value()), 0)))

        # апдейтер для точки пересечения y_перпендикуляра с осью
        perpendicular_to_y_dot.add_updater(lambda x: x.move_to(ax.c2p(0, np.sin(alpha.get_value()))))

        # апдейтер для линии косинуса альфа
        cos_alpha.add_updater(lambda x: x.become(
            Line(start=ax.c2p(0, 0), end=ax.c2p(np.cos(alpha.get_value()), 0),
                 color='#BA34EB', buff=zero_dot.radius)
        ))

        # апдейтер для линии синуса альфа
        sin_alpha.add_updater(lambda x: x.become(
            Line(start=ax.c2p(0, 0), end=ax.c2p(0, np.sin(alpha.get_value())),
                 color='#42F54B', buff=zero_dot.radius)
        ))

        # апдейтер для подписи косинуса
        cos_alpha_text.add_updater(lambda x: x.next_to(cos_alpha, DOWN))

        # апдейтер для подписи синуса
        sin_alpha_text.add_updater(lambda x: x.next_to(sin_alpha, LEFT))

        # анимация изменения улга альфа
        self.play(alpha.animate.set_value(2*np.pi + 1), run_time=18, rate_func=linear)

        # убираем апдейтеры
        objects_with_updaters = VGroup(positive_alpha_line, positive_alpha_dot, positive_alpha_arc,
                                       positive_alpha_text, perpendicular_to_x_from_alpha_dot, perpendicular_to_x_dot,
                                       perpendicular_to_y_from_alpha_dot, perpendicular_to_y_dot, cos_alpha, sin_alpha,
                                       cos_alpha_text, sin_alpha_text)
        objects_with_updaters.clear_updaters(recursive=True)

        # убираем лишние элементы, для следующей демонстрации
        self.play(FadeOut(sin_alpha_text), FadeOut(cos_alpha_text), FadeOut(sin_alpha), FadeOut(cos_alpha),
                  FadeOut(perpendicular_to_y_from_alpha_dot), FadeOut(perpendicular_to_x_from_alpha_dot),
                  FadeOut(perpendicular_to_y_dot), FadeOut(perpendicular_to_x_dot),
                  positive_alpha_line.animate.set_color(WHITE), run_time=2)

        # опускаем перпендикуляр на ось х, продлеваем его до пересечения с окружностью
        x_perpendicular = Line(start=ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value())),
                               end=ax.c2p(np.cos(alpha.get_value()), -np.sin(alpha.get_value())),
                               color='#42F54B', buff=positive_alpha_dot.radius)

        # точка пересечения перпендикуляра с окружностью
        negative_alpha_dot = Dot(ax.c2p(np.cos(alpha.get_value()), -np.sin(alpha.get_value())), color='#42F54B')

        self.play(Write(x_perpendicular), Write(negative_alpha_dot), run_time=3)

        # рисуем пометки, связанные с перпендикуляром: отмечаем прямой угол и равные отрезки
        x_perpendicular_ticks = VGroup(
            Line(start=ax.c2p(np.cos(alpha.get_value()) - 0.05, np.sin(alpha.get_value()) / 2),
                 end=ax.c2p(np.cos(alpha.get_value()) + 0.05, np.sin(alpha.get_value()) / 2)),
            Line(start=ax.c2p(np.cos(alpha.get_value()) - 0.05, -np.sin(alpha.get_value()) / 2),
                 end=ax.c2p(np.cos(alpha.get_value()) + 0.05, -np.sin(alpha.get_value()) / 2)),
            RightAngle(y_zero_line, x_perpendicular)
        )
        self.play(Write(x_perpendicular_ticks), run_time=2)

        # рисуем линию соответствующую дуге минус альфа
        negative_alpha_line = Line(start=ax.c2p(0, 0),
                                   end=ax.c2p(np.cos(alpha.get_value()), -np.sin(alpha.get_value())),
                                   color='#42F54B', buff=positive_alpha_dot.radius)
        self.play(Write(negative_alpha_line), run_time=3)

        # рисуем дугу, обозначающую градусную меру угла минус альфа
        negative_alpha_arc = Arc(radius=alpha_arc_radius_scale.get_value() * unit_circle.radius, start_angle=0,
                                 angle=alpha.get_value()%(2*np.pi), arc_center=unit_circle.get_center()).rotate(
            angle=-alpha.get_value(), about_point=unit_circle.get_center())

        # подпись к дуге минус альфа
        negative_alpha_text = MathTex('-\\alpha').move_to(
            ax.c2p(
                np.cos(alpha.get_value()%(2*np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15),
                -(np.sin(alpha.get_value()%(2*np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15))
            )
        )
        self.play(Write(negative_alpha_arc), FadeIn(negative_alpha_text), run_time=3)

        # убираем ненужные элементы для следующей демонстрации, все небелый элементы красим в белый
        self.play(FadeOut(x_perpendicular_ticks), FadeOut(x_perpendicular),
                  negative_alpha_line.animate.set_color(WHITE), negative_alpha_dot.animate.set_color(WHITE), run_time=2)

        # делаем анимация увеличения дуг минус альфа и альфа до размера окружности

        # апдейтер дуги альфа
        positive_alpha_arc.add_updater(lambda x: x.become(
            Arc(radius=alpha_arc_radius_scale.get_value() * unit_circle.radius, start_angle=0,
            angle=alpha.get_value() % (2 * np.pi), arc_center=unit_circle.get_center()
        )))

        # апдейтер дуги минус альфа
        negative_alpha_arc.add_updater(lambda x: x.become(
            Arc(radius=alpha_arc_radius_scale.get_value() * unit_circle.radius, start_angle=0,
                angle=alpha.get_value() % (2 * np.pi), arc_center=unit_circle.get_center()).rotate(
                angle=-alpha.get_value(), about_point=unit_circle.get_center())
        ))

        # апдейтер подписи дуги альфа
        positive_alpha_text.add_updater(lambda x: x.move_to(ax.c2p(
                np.cos(alpha.get_value() % (2 * np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15),
                np.sin(alpha.get_value() % (2 * np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15)
        )))

        # апдейтер подписи дуги минус альфа
        negative_alpha_text.add_updater(lambda x: x.move_to(ax.c2p(
            np.cos(alpha.get_value() % (2 * np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15),
            -(np.sin(alpha.get_value() % (2 * np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15))
        )))

        # меняем значения valuetracker'а. Собственно сама анимация
        self.play(alpha_arc_radius_scale.animate.set_value(1), run_time=4)

        # убираем апдейтеры
        objects_with_updaters = VGroup(positive_alpha_arc, negative_alpha_arc, positive_alpha_text,
                                       negative_alpha_text)
        objects_with_updaters.clear_updaters(recursive=True)

        # опустим перпендикуляр от точки, соответствующей дуги альфа на ось x
        self.play(Write(perpendicular_to_x_from_alpha_dot), FadeIn(perpendicular_to_x_dot), run_time=3)

        # отметим косинус альфа и подпишем его
        self.play(Write(cos_alpha), FadeIn(cos_alpha_text.set_color(color='#BA34EB')), run_time=3)

        # проводим перпендикуляр из точки минус альфа
        negative_alpha_x_perpendicular = Line(start=ax.c2p(np.cos(alpha.get_value()),
                                                           -np.sin(alpha.get_value())),
                                            end=ax.c2p(np.cos(alpha.get_value()), 0),
                                            color='#0099FF', buff=zero_dot.radius)
        self.play(Write(negative_alpha_x_perpendicular), run_time=2)

        # отметим и подпишем линию косинуса
        negative_alpha_cos_text = MathTex('\\cos(-\\alpha)').next_to(cos_alpha, UP).set_color(color='#BA34EB')
        self.play(FadeIn(negative_alpha_cos_text), run_time=2)

        # равенство отражающее четность косинуса
        cos_expression = MathTex('\\cos(\\alpha) = \\cos(-\\alpha)').to_edge(UR)
        self.play(FadeIn(cos_expression), run_time=3)

        # сделаем анимацию изменения угла альфа

        # апдейтер для линии угла альфа
        positive_alpha_line.add_updater(
            lambda x: x.become(
                Line(start=ax.c2p(0, 0),
                     end=ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value())),
                     buff=zero_dot.radius)
            )
        )

        # апдейтер для линии угла минус альфа
        negative_alpha_line.add_updater(lambda x: x.become(
            Line(start=ax.c2p(0, 0),
                 end=ax.c2p(np.cos(alpha.get_value()), -np.sin(alpha.get_value())),
                 buff=positive_alpha_dot.radius)
        ))

        # апдейтер для линии косинуса альфа
        cos_alpha.add_updater(lambda x: x.become(
            Line(start=ax.c2p(0, 0), end=ax.c2p(np.cos(alpha.get_value()), 0),
                 color='#BA34EB', buff=zero_dot.radius)
        ))

        # апдейтер для подписи косинус альфа
        cos_alpha_text.add_updater(lambda x: x.next_to(cos_alpha, DOWN))

        # апдейтер для подписи минус косинус альфа
        negative_alpha_cos_text.add_updater(lambda x: x.next_to(cos_alpha, UP))

        # апдейтер для альфа перпендикуляра
        perpendicular_to_x_from_alpha_dot.add_updater(lambda x: x.become(
            Line(start=ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value())),
                 end=ax.c2p(np.cos(alpha.get_value()), 0),
                 color='#0099FF', buff=zero_dot.radius)
        ))

        # апдейтер для минус альфа перпендикуляра
        negative_alpha_x_perpendicular.add_updater(lambda x: x.become(
            Line(start=ax.c2p(np.cos(alpha.get_value()),
                              -np.sin(alpha.get_value())),
                 end=ax.c2p(np.cos(alpha.get_value()), 0),
                 color='#0099FF', buff=zero_dot.radius)
        ))

        # апдейтер для точки пересечения перпендикуляров с осью
        perpendicular_to_x_dot.add_updater(lambda x: x.move_to(Dot(ax.c2p(np.cos(alpha.get_value()), 0))))

        # апдейтер для дуги альфа
        positive_alpha_arc.add_updater(lambda x: x.become(
            Arc(radius=alpha_arc_radius_scale.get_value() * unit_circle.radius, start_angle=0,
                angle=alpha.get_value() % (2 * np.pi), arc_center=unit_circle.get_center())
        ))

        # апдейтер для дуги минус альфа
        negative_alpha_arc.add_updater(lambda x: x.become(
            Arc(radius=alpha_arc_radius_scale.get_value() * unit_circle.radius, start_angle=0,
                angle=alpha.get_value() % (2 * np.pi), arc_center=unit_circle.get_center()).rotate(
                angle=-alpha.get_value(), about_point=unit_circle.get_center())
        ))

        # апдейтер для подписи к дуге альфа
        positive_alpha_text.add_updater(lambda x: x.move_to(ax.c2p(
            np.cos(alpha.get_value() % (2 * np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15),
            np.sin(alpha.get_value() % (2 * np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15)
        )))

        # апдейтер для подписи к дуге минус альфа
        negative_alpha_text.add_updater(lambda x: x.move_to(ax.c2p(
            np.cos(alpha.get_value() % (2 * np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15),
            -(np.sin(alpha.get_value() % (2 * np.pi) / 2) * (alpha_arc_radius_scale.get_value() + 0.15))
        )))

        # апдейтер для точки на окружности соответствующей дуге альфа
        positive_alpha_dot.add_updater(lambda x: x.move_to(
            ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value()))
        ))

        # апдейтер для точки на окружности соответствующей дуге минус альфа
        negative_alpha_dot.add_updater(lambda x: x.move_to(
            Dot(ax.c2p(np.cos(alpha.get_value()), -np.sin(alpha.get_value())))
        ))

        alpha.set_value(1)
        self.play(alpha.animate.set_value(3), rate_func=linear, run_time=4)
        self.play(alpha.animate.set_value(1), rate_func=linear, run_time=4)

        # уберем линии, относящиеся к косинусам
        self.play(FadeOut(cos_alpha_text),  FadeOut(negative_alpha_cos_text), Unwrite(cos_alpha),
                  Unwrite(perpendicular_to_x_from_alpha_dot), Unwrite(negative_alpha_x_perpendicular),
                  Unwrite(perpendicular_to_x_dot), run_time=2)
        self.wait(2)

        # отрисуем то же самое для синуса
        self.play(Write(perpendicular_to_y_from_alpha_dot), FadeIn(perpendicular_to_y_dot), run_time=2)
        self.play(Write(sin_alpha), FadeIn(sin_alpha_text.set_color(color='#42F54B')),run_time=2)

        # перпендикуляр минус альфа на ось y
        negative_alpha_y_perpendicular = Line(start=ax.c2p(np.cos(alpha.get_value()), -np.sin(alpha.get_value())),
                                            end=ax.c2p(0, -np.sin(alpha.get_value())),
                                            color='#0099FF', buff=zero_dot.radius)
        negative_alpha_y_perpendicular_dot = Dot(ax.c2p(0, -np.sin(alpha.get_value())), color='#0099FF')
        self.play(Write(negative_alpha_y_perpendicular), FadeIn(negative_alpha_y_perpendicular_dot), run_time=3)

        # синус минус альфа и подпись
        sin_negative_alpha = Line(start=ax.c2p(0, 0), end=ax.c2p(0, -np.sin(alpha.get_value())),
                         color='#BA34EB', buff=zero_dot.radius)
        sin_negative_alpha_text = (MathTex('\\sin(-\\alpha)', color='#BA34EB')
                                   .next_to(sin_negative_alpha, LEFT))
        self.play(Write(sin_negative_alpha), FadeIn(sin_negative_alpha_text), run_time=3)

        # равенство отражающее нечетность синуса
        sin_expression = MathTex('\\sin(\\alpha) = -\\sin(-\\alpha)').next_to(cos_expression, DOWN)
        self.play(FadeIn(sin_expression), run_time=3)

        # апдейтер для перпендикуляра на y из альфа
        perpendicular_to_y_from_alpha_dot.add_updater(lambda x: x.become(
            Line(start=ax.c2p(np.cos(alpha.get_value()), np.sin(alpha.get_value())),
                 end=ax.c2p(0, np.sin(alpha.get_value())),
                 color='#0099FF', buff=zero_dot.radius)
        ))

        # апдейтер для перпендикуляра на y из минус альфа
        negative_alpha_y_perpendicular.add_updater(lambda x: x.become(
            Line(start=ax.c2p(np.cos(alpha.get_value()), -np.sin(alpha.get_value())),
                 end=ax.c2p(0, -np.sin(alpha.get_value())),
                 color='#0099FF', buff=zero_dot.radius)
        ))

        # апдейтеры для точек пересечения перпендикуляров с осью y
        perpendicular_to_y_dot.add_updater(lambda x: x.move_to(ax.c2p(0, np.sin(alpha.get_value()))))
        negative_alpha_y_perpendicular_dot.add_updater(lambda x: x.move_to(
            ax.c2p(0, -np.sin(alpha.get_value()))
        ))

        # апдейтеры для линий синусов
        sin_alpha.add_updater(lambda x: x.become(
            Line(start=ax.c2p(0, 0), end=ax.c2p(0, np.sin(alpha.get_value())),
                 color='#42F54B', buff=zero_dot.radius)
        ))
        sin_negative_alpha.add_updater(lambda x: x.become(
            Line(start=ax.c2p(0, 0), end=ax.c2p(0, -np.sin(alpha.get_value())),
                 color='#BA34EB', buff=zero_dot.radius)
        ))

        # апдейтеры для подписей к синусам
        sin_alpha_text.add_updater(lambda x: x.next_to(sin_alpha, LEFT))
        sin_negative_alpha_text.add_updater(lambda x: x.next_to(sin_negative_alpha, LEFT))


        self.play(alpha.animate.set_value(3), rate_func=linear, run_time=4)
        self.play(alpha.animate.set_value(1), rate_func=linear, run_time=4)
        self.wait(3)