import reflex as rx
import datetime
from PythonWeb.styles.styles import MONO
from PythonWeb.styles.colors import Colors as Color, TextColor
from PythonWeb.constants import APP_VERSION


def _logo(src: str, href: str, alt: str, height: str) -> rx.Component:
    return rx.link(
        rx.image(src=src, height=height, width="auto", alt=alt),
        href=href,
        is_external=True,
        opacity="0.55",
        _hover={"opacity": "1"},
        style={"filter": "grayscale(1)", "transition": "opacity .2s ease"},
    )


def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            _logo("/python.svg", "https://www.python.org/", "Logo de Python", "28px"),
            _logo("/Tux_Mono.png", "https://www.kernel.org/", "Logo de Tux, la mascota de Linux", "32px"),
            _logo("/Reflex_white.svg", "https://reflex.dev/", "Logo de Reflex", "20px"),
            spacing="6",
            align="center",
        ),
        rx.text(f"2023 – {datetime.date.today().year} · Víctor Jiménez · {APP_VERSION}",
                font_size="0.8em", font_family=MONO, color=TextColor.MUTED.value),
        align="center",
        spacing="4",
        width="100%",
        padding_y="2.5em",
        margin_top="3em",
        border_top=f"1px solid {Color.BORDER.value}",
    )
