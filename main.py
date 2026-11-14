from typing import override

from manim import *

# -------------------------- Settings --------------------------
DARK_MODE = True


I_TEX = MathTex(r"\int_0^n x^2 \,\lceil x \rceil,\qquad n \in \mathbb Z^+")
I_FILL = 0.85
# 0.85

SHOW_TITLE = True
TITLE_TEX = MathTex(r"\text{Evaluar:}")
TITLE_SCALE = 1.8

SHOW_FOOTER = False
FOOTER_TEX = MathTex(
    r"C: \text{El segmento de recta de } z = 0 \, \text a \, z = 2 + i"
)
FOOTER_SCALE = 1.0

COLORS = {
    "dark": {
        "bg": WHITE,
        "font": BLACK
    },
    "light": {
        # ? Not fully BLACK, because then the animation wont play properly
        "bg": ManimColor("#010101"),
        "font": WHITE
    }
}
# --------------------------------------------------------------


BG_COLOR = COLORS["dark"]["bg"] if DARK_MODE else COLORS["light"]["bg"]
FONT_COLOR = COLORS["dark"]["font"] if DARK_MODE else COLORS["light"]["font"]


config.background_color = BG_COLOR


class Int(Scene):
    @override
    def construct(self) -> None:
        title = TITLE_TEX.to_edge(UP, buff=0.5).set_color(FONT_COLOR).scale(TITLE_SCALE)
        footer = (
            FOOTER_TEX.to_edge(DOWN, buff=0.5).set_color(FONT_COLOR).scale(FOOTER_SCALE)
        )

        i = I_TEX.set_color(FONT_COLOR)
        i.set_width(config.frame_width * I_FILL)

        if SHOW_TITLE:
            self.play(Write(title))

        self.play(Write(i), run_time=2)

        if SHOW_FOOTER:
            self.play(Write(footer))

        self.wait(3.5)
