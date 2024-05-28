import reflex as rx
import PythonWeb.styles.styles as styles
from PythonWeb.styles.styles import Size
from PythonWeb.styles.colors import Colors as Color
from PythonWeb.routes import Route
from PythonWeb.components.ant_components import float_button


def navbar(text: str) -> rx.Component:
    return rx.hstack(
        rx.link(
        rx.text(text,
                color=Color.PRIMARY.value,
                align="center",
                font_size=Size.MLARGE.value,
                ),
        href=Route.INDEX.value,
        ),
        #float_button(),
        style=styles.navbar_style,
    )
