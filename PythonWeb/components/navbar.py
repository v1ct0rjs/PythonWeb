import reflex as rx
import PythonWeb.styles.styles as styles
from PythonWeb.styles.styles import Size
from PythonWeb.styles.colors import Colors as Color



def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("['V1cT0r', 'l1nuX3r0', 'PyTh0n1sta', 'D3v3l0p3r']",
                color=Color.PRIMARY.value,
                align="center",
                font_size=Size.MLARGE.value,

                ),
        style=styles.navbar_style,
    )
