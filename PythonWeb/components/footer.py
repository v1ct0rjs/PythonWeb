import reflex as rx
import datetime
from PythonWeb.styles.styles import *
from PythonWeb.styles.colors import Colors as Color

def footer() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.hstack(
                rx.image(
                    src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
                    width="150px",
                    padding_right=Size.XXLARGE.value),  # Aumenta este valor para más espacio
                rx.image(src="cybersecurity-essentials.png", width="150px", padding_right=Size.XXLARGE.value),
                rx.image(src="Tux_Mono.png", width="85px"),
                align="center"
            )
        ),
        rx.text(f"2023 - {datetime.date.today().year} Portfolio By Víctor Jiménez version 1.0",
                font_size=Size.LARGE.value),
        align="center",
        color=TextColor.CONTENT.value,
        background_color=Color.BACKGROUND.value,
        font_family=Fonts.JETBRAINS_MONO.value,
    )
