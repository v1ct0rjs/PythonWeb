import reflex as rx
import PythonWeb.styles.styles as styles
from PythonWeb.styles.styles import Size
from PythonWeb.styles.colors import Colors as Color
from PythonWeb.routes import Route
from PythonWeb.model.Live import Live


def navbar(text: str, live=Live(is_live=False, live_tittle='', live_user='')) -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.text(text,
                    color=Color.PRIMARY.value,
                    align="center",
                    font_size=Size.MLARGE.value,
                    ),
            href=Route.INDEX.value,
        ),
        rx.hstack(
            rx.cond(
                live.is_live,
                rx.link(
                    rx.image(
                        src="/twitch.svg",
                        color=Color.PRIMARY.value,
                        width=Size.XXLARGE.value,
                        height=Size.XXLARGE.value,
                        margin_top='-10px',
                        margin_right=Size.MEDIUM.value,
                        class_name="blink",
                    ),
                    href="https://www.twitch.tv/dj_10tacle",
                    is_external=True,
                )
            ),
            justify_content="end",
            margin_left="auto",
        ),
        style=styles.navbar_style,
    )