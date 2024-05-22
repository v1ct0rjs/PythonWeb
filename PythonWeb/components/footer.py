import reflex as rx
import datetime
from PythonWeb.styles.styles import *
from PythonWeb.styles.colors import Colors as Color

def footer() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.hstack(
                rx.image(
                    src="python.svg",
                    width="100px",
                    padding_right=Size.XLARGE.value),  # Aumenta este valor para más espacio
                rx.image(src="Tux_Mono.png", width="60px"),
                rx.image(src="Reflex_white.svg", width="150px", padding_left=Size.XLARGE.value),
                align="center"
            )
        ),
        rx.text(f"2023 - {datetime.date.today().year} By Víctor Jiménez version 1.0",
                font_size=Size.LARGE.value),
        align="center",
        color=TextColor.CONTENT.value,
        background_color=Color.BACKGROUND.value,
        font_family=Fonts.JETBRAINS_MONO.value,
    )
