import reflex as rx
import PythonWeb.styles.styles as styles
from PythonWeb.styles.styles import Size
from PythonWeb.styles.colors import Colors as Color



def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("V1c+0r, l1nu><3r0 y py+h0n1s+a",
                color=Color.PRIMARY.value,
                align="center",
                font_size=Size.MLARGE.value,

                ),
        style=styles.navbar_style,
    )
