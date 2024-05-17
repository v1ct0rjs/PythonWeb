import reflex as rx
from PythonWeb.styles.styles import *

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text.strong("Portfolio de Víctor Jiménez",
                color="black",
                align="center",
                font_size=Size.LARGE.value),
        position="sticky",
        bg="lightgray",
        padding_x=Size.SMALL.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0",
    )
