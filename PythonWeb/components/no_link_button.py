import reflex as rx
from PythonWeb.styles.styles import *

def no_link_button(title: str, subtitle: str) -> rx.Component:
    return rx.box(
            rx.hstack(
                    rx.image(
                        src='/cybersecurity-essentials.png',
                        width=Size.XXLARGE.value,
                        height=Size.XXLARGE.value,
                        margin=Size.MEDIUM.value,
                        alt="Sello de certificación Cisco"
                    ),
                rx.vstack(
                    rx.text(title, style=button_title_style, color=Color.PRIMARY.value),
                    rx.text(subtitle, style=button_body_style),
                    spacing='0',
                ),
                width="100%",
                align_items="center",
            ),
        style=no_button_style,
    )
