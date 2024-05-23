import reflex as rx
from PythonWeb.styles.styles import *

def link_button(title: str, subtitle: str, url: str, icon: str, icon_path: str = None) -> rx.Component:
    if icon_path is None:
        icon_component = rx.icon(
            tag=icon,
            width=Size.XLARGE.value,
            height=Size.XLARGE.value,
            margin=Size.MEDIUM.value,
            color=Color.BLACK.value,
        )
    else:
        icon_component = rx.image(
            src=icon_path,
            width=Size.XLARGE.value,
            height=Size.XLARGE.value,
            margin=Size.MEDIUM.value,
        )

    return rx.link(
        rx.button(
            rx.hstack(
                rx.box(icon_component),
                rx.vstack(
                    rx.text(title, style=button_title_style),
                    rx.text(subtitle, style=button_body_style),
                    spacing='0',
                ),
                width="100%",
                align_items="start"
            )
        ),
        href=url,
        is_external=True,
        width="100%",
    )
