import reflex as rx
import PythonWeb.styles.styles as styles
from PythonWeb.styles.styles import Size



def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("Portfolio de Víctor Jiménez",
                color="black",
                align="center",
                font_size=Size.MLARGE.value,

                ),
        style=styles.navbar_style,
    )
