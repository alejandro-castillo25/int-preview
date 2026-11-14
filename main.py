from typing import override

from manim import *

# -------------------------- Settings --------------------------
DARK_MODE = True


I_TEX = MathTex(r"\int_0^n x^2 \,\lceil x \rceil,\qquad n \in \mathbb Z^+")
I_FILL = 0.85
# 0.85

SHOW_HEADER = True
HEADER_TEX = MathTex(r"\text{Evaluar:}")
HEADER_SCALE = 1.8

SHOW_FOOTER = False
FOOTER_TEX = MathTex(
    r"C: \text{El segmento de recta de } z = 0 \, \text a \, z = 2 + i"
)
FOOTER_SCALE = 1.0

# ? light -> font is not fully BLACK, because then the animation wont play properly
COLORS: dict[str, dict[str, ManimColor]] = {
    "dark": {"bg": BLACK, "font": WHITE},
    "light": {"bg": WHITE, "font": ManimColor("#010101")},
}
# --------------------------------------------------------------


BG_COLOR = COLORS["dark"]["bg"] if DARK_MODE else COLORS["light"]["bg"]
FONT_COLOR = COLORS["dark"]["font"] if DARK_MODE else COLORS["light"]["font"]


config.background_color = BG_COLOR


class Int(Scene):
    @override
    def construct(self) -> None:
        header = HEADER_TEX.to_edge(UP, buff=0.5).set_color(FONT_COLOR).scale(HEADER_SCALE)
        footer = (
            FOOTER_TEX.to_edge(DOWN, buff=0.5).set_color(FONT_COLOR).scale(FOOTER_SCALE)
        )

        i = I_TEX.set_color(FONT_COLOR)
        i.set_width(config.frame_width * I_FILL)

        if SHOW_HEADER:
            self.play(Write(header))

        self.play(Write(i), run_time=2)

        if SHOW_FOOTER:
            self.play(Write(footer))

        self.wait(3.5)
