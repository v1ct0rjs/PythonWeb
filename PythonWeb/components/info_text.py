import reflex as rx
from PythonWeb.styles.styles import *

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(title, font_weight="bold", color="blue"),
        body, font_size=Size.MEDIUM.value, color="black",
    )