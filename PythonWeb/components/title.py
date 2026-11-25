import reflex as rx
from PythonWeb.styles.styles import MONO
from PythonWeb.styles.colors import TextColor


def title(text: str) -> rx.Component:
    """Título de sección con estética de terminal: ~/texto"""
    return rx.heading(
        rx.text.span("~/", color=TextColor.PRIMARY.value),
        text,
        as_="h2",
        font_family=MONO,
        font_weight="700",
        font_size="1.6em",
        color=TextColor.BODY.value,
    )
