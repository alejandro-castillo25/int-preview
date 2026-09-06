from typing import override

from manim import *

# -------------------------- Settings --------------------------
DARK_MODE = True
I_FILL = 0.75

SHOW_TITLE = False
TITLE_TEX = MathTex(r"\text{Evaluar:}")
TITLE_SCALE = 1.0

SHOW_FOOTER = False
FOOTER_TEX = MathTex(
    r"\text{Sabiendo que:}\quad \text{erf}(x)= \frac 2 {\sqrt \pi } \int_0^x e^{-t^2}\,dt"
)
FOOTER_SCALE = 1.0

# --------------------------------------------------------------


FONT_COLOR = WHITE if DARK_MODE else ManimColor("#010101")
BG_COLOR = BLACK if DARK_MODE else WHITE


config.background_color = BG_COLOR


class Int(Scene):
    @override
    def construct(self) -> None:
        title = TITLE_TEX.to_edge(UP, buff=0.5).set_color(FONT_COLOR).scale(TITLE_SCALE)
        footer = (
            FOOTER_TEX.to_edge(DOWN, buff=0.5).set_color(FONT_COLOR).scale(FOOTER_SCALE)
        )

        i = MathTex(r"\Re(f(z))\qquad\Im(f(z))", color=FONT_COLOR)
        i.set_width(config.frame_width * I_FILL)

        if SHOW_TITLE:
            self.play(Write(title))

        self.play(Write(i), run_time=2)

        if SHOW_FOOTER:
            self.play(Write(footer))

        self.wait(3.5)
