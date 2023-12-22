from manim import *
import math

class WriteStuff(Scene):
    def construct(self):
        example_text = Tex("The Gaussian Integral", tex_to_color_map={"text": YELLOW})
        example_tex = MathTex(
            "\int_{-\infty}^{\infty} e^{-x^2} \,dx = \sqrt{\pi}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.width = config["frame_width"] - 2 * LARGE_BUFF

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class GaussianIntegral(Scene):
    def construct(self):
        ax = Axes(x_range=(-5, 5), y_range=(0, 2))
        curve = ax.plot(lambda x: math.exp(-x*x), color= RED)
        area = ax.get_area(curve, x_range=(-1000000, 100000))
        example_tex = MathTex(
            "\int_{-\infty}^{\infty} e^{-x^2} \,dx = \sqrt{\pi}", font_size = 75
        )
        gauss = Tex("The Gaussian Integral", font_size= 100)
        author = Tex("A Brief Introduction")
        let = MathTex(
            "I = \int_{-\infty}^{\infty} e^{-x^2} \,dx", font_size = 75)
        double = MathTex(
            "I^2 = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-x^2 - y^2} \,dx\,dy", font_size = 75)
        convert = MathTex(
            "I^2 = \int_{0}^{\infty} \int_{0}^{2\pi} e^{-r^2} \,r\,d\\theta\,dt", font_size = 75
        )
        first_eval = MathTex("I^2 = 2\pi \int_{0}^{2\pi} e^{-r^2} \,r\,dr", font_size = 75)
        first_eval.shift(1.5 * UP)

        second_eval = MathTex(
            "I^2 = 0 - 2\pi(\\frac{-1}{2})", font_size = 75)
        second_eval.shift(1.5* DOWN)
        
        let.shift(1.5 * UP)
        double.shift(DOWN)

        third_eval = MathTex(
            "I^2 = \pi", font_size = 75)
        
        third_eval.shift(0.5 * UP)

        fourth_eval = MathTex(
            "\\therefore \hspace{2mm} I = \sqrt{\pi}", font_size = 75
        )
        fourth_eval.set_color(BLUE)
        fourth_eval.shift(1.5 * DOWN)

        group = VGroup(gauss, author)
        group.arrange(DOWN)
        group.width = config["frame_width"] - 2 * LARGE_BUFF

        self.play(Write(gauss))
        self.wait(1)
        self.play(Write(author))
        self.wait(1)
        self.play(FadeOut(gauss), FadeOut(author))
        self.wait(1)
        self.play(Write(example_tex))
        self.wait(2)
        self.play(FadeOut(example_tex))
        self.play(Create(ax), run_time=3)
        self.play(Create(curve) ,run_time = 3)
        self.play(FadeIn(area))
        self.wait(1)
        self.play(FadeOut(area), FadeOut(curve), FadeOut(ax))
        self.wait(1)
        self.play(Write(let))
        self.wait(2)
        self.play(Write(double))
        self.play(FadeOut(let), FadeOut(double))
        self.wait(2)
        self.play(Write(convert))
        self.wait(2)
        self.play(FadeOut(convert))
        self.wait(2)
        self.play(Write(first_eval))
        self.wait(2)
        self.play(Write(second_eval))
        self.wait(2)
        self.play(FadeOut(first_eval), FadeOut(second_eval))
        self.wait(1)
        self.play(Write(third_eval))
        self.wait(1)
        self.play(Write(fourth_eval))
        self.wait(1)
        self.play(FadeOut(third_eval), FadeOut(fourth_eval))

        