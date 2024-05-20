import reflex as rx
from PythonWeb.styles.styles import *
from PythonWeb.styles.colors import Colors as Color

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(title, font_weight="bold", color=TextColor.ORANGE.value),
        body, font_size=Size.MEDIUM.value, color=TextColor.GREY.value,
    )