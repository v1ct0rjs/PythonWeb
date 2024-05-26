import reflex as rx
import datetime
from PythonWeb.styles.styles import *
from PythonWeb.styles.colors import Colors as Color

def footer() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.hstack(
                rx.link(
                    rx.image(
                        src="/python.svg",
                        width="100px",
                        padding_right=Size.XLARGE.value,
                        alt="Logo de Python, dos serpientes entrelazadas"
                    ),
                    href="https://www.python.org/",
                    is_external=True
                ),
                rx.link(
                rx.image(src="/Tux_Mono.png", width="60px", alt="Logo de Tux, la mascota de Linux un pinguino"),
                href="https://www.kernel.org/",
                is_external=True
                ),
                rx.link(
                rx.image(src="/Reflex_white.svg", width="150px", padding_left=Size.XLARGE.value, alt="Logo de reflex"),
                href="https://reflex.dev/",
                is_external=True
                ),
                align="center"
            )
        ),
        rx.text(f"2023 - {datetime.date.today().year} By Víctor Jiménez V1.1",
                font_size=Size.LARGE.value),
        align="center",
        color=TextColor.CONTENT.value,
        background_color=Color.BACKGROUND.value,
        font_family=Fonts.JETBRAINS_MONO.value,
    )